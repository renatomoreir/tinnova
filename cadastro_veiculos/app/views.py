from flask import Blueprint, abort, request, jsonify
from .models import Veiculo
from .database import db
from .utils import marca_valida
from datetime import datetime, timedelta
from sqlalchemy import func


bp = Blueprint('api', __name__)


@bp.route("/", methods=["GET"])
def listar_veiculos():
    """
    Manipula a requisição GET para o endpoint raiz ("/") e retorna uma lista JSON com todos os veículos.

    Retorna:
        Response: Um array JSON contendo dicionários com as seguintes chaves para cada veículo:
            - id (int): Identificador único do veículo.
            - marca (str): Marca do veículo.
            - modelo (str): Modelo do veículo.
            - ano (int): Ano de fabricação do veículo.
            - descricao (str): Descrição do veículo.
            - vendido (bool): Indica se o veículo foi vendido.
            - created (datetime): Data de criação do registro do veículo.
            - updated (datetime): Data da última atualização do registro do veículo.
    """
    veiculos = Veiculo.query.all()
    return jsonify([{
        "id": v.id,
        "marca": v.marca,
        "modelo": v.modelo,
        "ano": v.ano,
        "descricao": v.descricao,
        "vendido": v.vendido,
        "created": v.created,
        "updated": v.updated
    } for v in veiculos])


@bp.route("/", methods=["POST"])
def criar_veiculo():
    """
    Endpoint para criar um novo veículo.
    Método: POST
    Rota: "/"
    Request JSON:
        {
            "modelo": str,      # Nome do modelo do veículo
            "marca": str,       # Nome da marca do veículo
            "ano": int,         # Ano de fabricação do veículo
            "descricao": str,   # Descrição do veículo
            "vendido": bool     # (Opcional) Indica se o veículo foi vendido (default: False)
        }
    Respostas:
        201 Created:
            {
                "id": int   # ID do veículo criado
            }
        400 Bad Request:
            {
                "message": "Marca inválida."
            }
    Descrição:
        Cria um novo registro de veículo no banco de dados. Todos os campos de string são convertidos para minúsculas.
        Valida se a marca informada é válida antes de criar o registro.
    """
    data = {k.lower(): v.lower() if isinstance(v, str) else v for k, v in request.json.items()}
    if not marca_valida(data.get("marca")):
        abort(400, description="Marca inválida.")
    
    veiculo = Veiculo(
        modelo=data.get("modelo"),
        marca=data.get("marca"),
        ano=data.get("ano"),
        descricao=data.get("descricao"),
        vendido=bool(data.get("vendido", False)),
        created=datetime.utcnow(),
        updated=datetime.utcnow()
    )
    db.session.add(veiculo)
    db.session.commit()
    return jsonify({"id": veiculo.id}), 201


@bp.route("/<int:id>", methods=["GET"])
def get_veiculo(id):
    """
    Recupera um veículo pelo seu ID.

    Args:
        id (int): O identificador único do veículo.

    Retorna:
        Response: Uma resposta JSON contendo os dados do veículo, se encontrado.

    Lança:
        404: Se nenhum veículo com o ID fornecido for encontrado.
    """
    veiculo = Veiculo.query.get_or_404(id)
    return jsonify(veiculo.to_dict())

@bp.route("/<int:id>", methods=["PUT"])
def update_veiculo(id):
    """
    Atualiza um registro de veículo existente pelo seu ID.

    Este endpoint recebe um payload JSON com qualquer subconjunto dos campos permitidos
    ('modelo', 'marca', 'ano', 'descricao', 'vendido') e atualiza os atributos correspondentes
    do veículo. O campo 'updated' é atualizado para o horário UTC atual.
    Se o veículo com o ID fornecido não existir, retorna erro 404.

    Args:
        id (int): O ID do veículo a ser atualizado.

    Retorna:
        Response: Uma representação JSON do veículo atualizado.

    Lança:
        404: Se o veículo com o ID especificado não existir.
    """
    data = request.get_json()
    veiculo = Veiculo.query.get_or_404(id)
    allowed_fields = {"modelo", "marca", "ano", "descricao", "vendido"}
    for key in allowed_fields:
        if key in data:
            setattr(veiculo, key, data[key])
    veiculo.updated = datetime.utcnow()
    db.session.commit()
    return jsonify(veiculo.to_dict())


@bp.route("/<int:id>", methods=["PATCH"])
def patch_veiculo(id):
    """
    Manipula requisições HTTP PATCH para atualizar campos específicos de um veículo.

    Args:
        id (int): O identificador único do veículo a ser atualizado.

    Corpo da Requisição (JSON):
        Conjunto parcial ou completo dos seguintes campos:
            - modelo (str): O modelo do veículo.
            - marca (str): A marca do veículo.
            - ano (int): O ano do veículo.
            - descricao (str): A descrição do veículo.
            - vendido (bool): O status de venda do veículo.

    Retorna:
        Response: Uma representação JSON do veículo atualizado.

    Lança:
        404: Se o veículo com o ID fornecido não existir.
    """
    data = request.get_json()
    veiculo = Veiculo.query.get_or_404(id)
    allowed_fields = {"modelo", "marca", "ano", "descricao", "vendido"}
    for key, value in data.items():
        if key in allowed_fields:
            setattr(veiculo, key, value)
    veiculo.updated = datetime.utcnow()
    db.session.commit()
    return jsonify(veiculo.to_dict())


@bp.route("/<int:id>", methods=["DELETE"])
def delete_veiculo(id):
    """
    Remove um registro de veículo do banco de dados pelo seu ID.

    Args:
        id (int): O identificador único do veículo a ser removido.

    Retorna:
        Response: Uma resposta JSON com mensagem de sucesso e código HTTP 200 se a exclusão for bem-sucedida.
                    Se o veículo com o ID fornecido não existir, retorna erro 404.
    """
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    return jsonify({"message": "Veículo deletado com sucesso."}), 200

@bp.route("/nao-vendidos", methods=["GET"])
def nao_vendidos():
    """
    Endpoint para obter todos os veículos que ainda não foram vendidos.

    Retorna:
        Response: Um array JSON contendo os detalhes de todos os veículos onde 'vendido' é False.
    """
    veiculos = Veiculo.query.filter_by(vendido=False).all()
    return jsonify([v.to_dict() for v in veiculos])


@bp.route("/vendidos", methods=["GET"])
def vendidos():
    """
    Endpoint para obter todos os veículos marcados como vendidos.

    Retorna:
        Response: Um array JSON contendo os dados serializados de todos os veículos
        onde o atributo 'vendido' é True.
    """
    veiculos = Veiculo.query.filter_by(vendido=True).all()
    return jsonify([v.to_dict() for v in veiculos])


@bp.route("/distribuicao-decada", methods=["GET"])
def distribuicao_decada():
    """
    Endpoint para obter a distribuição de veículos por década.

    Busca todos os veículos no banco de dados, agrupa-os pela década do ano de fabricação,
    e retorna um objeto JSON onde as chaves são as décadas (ex: "1990s") e os valores são
    as quantidades de veículos fabricados em cada década.

    Retorna:
        Response: Uma resposta JSON contendo a distribuição de veículos por década.
    """
    veiculos = Veiculo.query.all()
    result = {}
    for v in veiculos:
        decada = f"{(v.ano // 10) * 10}s"
        result[decada] = result.get(decada, 0) + 1
    return jsonify(result)


@bp.route("/distribuicao-fabricante", methods=["GET"])
def distribuicao_marca():
    """
    Endpoint para obter a distribuição de veículos por fabricante.

    Retorna:
        JSON: Um dicionário onde as chaves são os nomes das marcas (marca) e os valores são o total de veículos para cada marca.
    """
    result = db.session.query(Veiculo.marca, func.count(Veiculo.id)).group_by(Veiculo.marca).all()
    return jsonify({marca: total for marca, total in result})


@bp.route("/ultimos", methods=["GET"])
def ultimos_cadastrados():
    """
    Endpoint para obter veículos cadastrados nos últimos 7 dias.

    Retorna:
        Resposta JSON: Uma lista de dicionários, cada um contendo os campos 'id', 'modelo' e 'created'
        para veículos cujo campo 'created' está dentro dos últimos 7 dias.
    """
    sete_dias = datetime.utcnow() - timedelta(days=7)
    veiculos = Veiculo.query.filter(Veiculo.created >= sete_dias).all()
    return jsonify([{"id": v.id, "modelo": v.modelo, "created": v.created} for v in veiculos])

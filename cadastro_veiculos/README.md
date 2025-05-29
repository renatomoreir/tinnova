# 1. Criar e ativar ambiente virtual
cd .\cadastro_veiculos\
python -m venv venv
venv\\Scripts\\activate

# 2. Instalar dependências
pip install -r requirements.txt
python.exe -m pip install --upgrade pip

# 3. Baixar o Docker Desktop
```Acesse o site oficial e baixe o instalador para Windows:

https://www.docker.com/get-started

Dê duplo-clique em Docker Desktop Installer.exe, Siga o assistente: Marque a opção Use WSL 2 instead of Hyper-V (recomendado), Aceite os termos e clique em Install, Aguarde baixar componentes e configurar tudo.

```

docker version
docker compose up -d
docker ps -a

# 4. Rodar o servidor
python .\run.py


# 5. Endpoints

localhost:5000/                         , ["GET"]
localhost:5000/                         , ["POST"], { "marca": "chevrolet", "modelo": "gol", "ano": "2000", "descricao": "1.0 Gasolina", "vendido": false}
localhost:5000/<int:id>                 , ["GET"]
localhost:5000/<int:id>                 , ["PUT"]
localhost:5000/<int:id>                 , ["PATCH"]
localhost:5000/<int:id>                 , ["DELETE"]
localhost:5000/nao-vendidos             , ["GET"]
localhost:5000/vendidos                 , ["GET"]
localhost:5000/distribuicao-decada      , ["GET"]
localhost:5000/distribuicao-fabricante  , ["GET"]
localhost:5000/ultimos                  , ["GET"]

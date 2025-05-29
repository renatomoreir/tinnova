# 1. Criar e ativar ambiente virtual
cd .\cadastro_veiculos\
python -m venv venv
## No Windows: 
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


# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
# Para criar o ambiente virtual python -m venv nome_do_ambiente_virtual
# Para ativar executar o . nome_do_ambiente_virtual/bin/activate (e desativar com deactivate)
# pip freeze para mostrar as bibliotecas instaladas
# pip install nome para instalar a biblioteca
# pip index version nome para verificar as versoes disponiveis da biblioteca nome
# pip install nome==versao para instalar uma versao especifica
# pip install nome --upgrade
# pip freeze > requirements.txt para gerar os requisitos de bibliotecas do projeto
# pip install -r requirements.txt para instalar o que está descrito no arquivo
## MAB - Mobilidade Acessível Brasileira

## Introdução

Bem-vindo ao <a href="https://drive.google.com/file/d/1fKrNdoC4BQECgJWsWTTeR-oTmSsxZqNo/view?usp=sharing">MAB - Mobilidade Acessível Brasileira</a>, um sistema em Flask projetado para facilitar a mobilidade de pessoas com deficiência visual de baixa visão durante a realização de viagens privadas.

## Instalação

Siga estas instruções para configurar e executar o MAB em seu ambiente local.

### Pré-requisitos

- Python 3.x instalado em seu sistema. Se necessário, faça o download em [python.org](https://www.python.org/downloads/).

### Passos de Instalação

1. Clone este repositório em seu sistema:

   ```bash
   git clone https://github.com/<seu-usuario>/MAB.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd MAB
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o banco de dados:

   ```bash
   flask db init
   ```
   ```bash
   flask db migrate
   ```
   ```bash
   flask db upgrade
   ```

5. Inicie o aplicativo:

   ```bash
   flask run --host=0.0.0.0
   ```

6. Acesse o MAB no seu navegador em `http://127.0.0.1:5000`.

## Utilização

O MAB oferece uma interface acessível e agradável para pessoas com deficiência visual de baixa visão, além de contar com um recurso de leitura sonora próprio, o que contribui ainda mais para a acessibilidade do sistema.

## Linguagens e Ferramentas

<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,flask,html,css,bootstrap,javascript,nodejs,sqlite" />
  </a>
</p>

---

Aproveite o uso do MAB e ajude a promover a acessibilidade no Brasil!

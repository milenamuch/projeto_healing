### Pre sets

- Criar o ambiente virtual: <br>
`python -m venv .venv`

- Ativar o ambiente virtual:  <br>
     - Windows: <br>
`./.venv/scripts/activade`

    -  Linux: <br>
`source venv/bin/activate`

- Após a ativação do ambiente virtual, instalar o requirements: <br>
`pip install -r requirements.txt`


### Códigos úteis para um projeto Django

- Criar um novo app: <br>
`python manage.py startapp nome_app`
    - Após a criação do app é necessário inseri-lo dentro de `setings.py`do projeto principal na lista `INSTALLED_APPS`.

- Criar um novo app: <br>
`python manage.py startapp nome_app`

- Executar alterações no banco de dados: <br>
`python manage.py makemigrations`

- Aplicar alterações no banco de dados: <br>
`python manage.py migrate`

- Criar um usuário administrador: <br>
`python manage.py createsuperuser`
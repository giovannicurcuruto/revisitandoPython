# CRUD básico, com exemplo de Flask em Python com banco de dados. 

Utilizado o Banco de Dados PostGreSQL

* **GET**
> /carros

* **GET by ID**
> /carros/ID

* **POST - Create**
> /carros/ID
> Deve ser adicionado informações no campo BODY

* **DELETE**
> /carros/ID

* **UPDATE**

> /carros/ID
> Deve ser adicionado informações no campo BODY

* **Exemplo de Body:**

>{
>    "ano": 2015,
>    "marca": "Nissan",
>    "modelo": "Versa"
>}

* **Banco de Dados**
> Deverá ser instanciado um BD dentro da ferramenta PgAdmin4


* **TODO**
> colocar os padrões REST (400,200,500, etc)
> criar uma classe de conexão com o banco
> Teste unitário
> Classe unitária para montar o JSONFY (?)
> Modelar usando Swagger ou OPEN_API

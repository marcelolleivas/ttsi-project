# language: pt
# encoding: utf-8

  Funcionalidade: Login

  Esquema do Cenário: : Login
    Dado que tente fazer login com usuário "<status do usuário>"
    Então status da requisição deve ser "<status da requisição>"
    E resposta deve ser de "<status da resposta>"

    Exemplos:
    | status do usuário | status da requisição | status da resposta |
    | valido            | 200                  | sucesso            |
    | invalido          | 401                  | erro               |

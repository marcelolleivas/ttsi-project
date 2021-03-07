# language: pt
# encoding: utf-8

  Funcionalidade: Produtos

  Esquema do Cenário: : Adicionar produto
    Dado que queira incluir um produto "<tipo de produto>"
    Então status de produto deve ser "<status da requisição>"
    E resposta de produto deve ser de "<status da resposta>"

    Exemplos:
    | tipo de produto         | status da requisição | status da resposta |
    | simples                 | 201                  | sucesso            |
    | mais de uma cor         | 201                  | sucesso            |
    | mais de um componente   | 201                  | sucesso            |
    | sem cor                 | 400                  | erro               |
    | sem componentes         | 400                  | erro               |
    | sem valor               | 400                  | erro               |


#  Esquema do Cenário: Editar produto
#    Dado que queira editar um produto para "<tipo de produto>"
#    Então status de produto deve ser "<status da requisição>"
#    E resposta deve ser de "<status da resposta>"
#
#
#    Exemplos:
#    | tipo de produto         | status da requisição | status da resposta |
#    | simples                 | 201                  | sucesso            |
#    | mais de uma cor         | 201                  | sucesso            |
#    | mais de um componente   | 201                  | sucesso            |
#    | sem cor                 | 400                  | erro               |
#    | sem componentes         | 400                  | erro               |
#    | sem valor               | 400                  | erro               |
#
#
#  Esquema do Cenário: Visualizar produto
#    Dado que queira visualizar um produto "<tipo de produto>"
#    Então status de produto deve ser "<status da requisição>"
#    E resposta deve ser "<status da resposta>"
#    E dados retornados devem estar de acordo com o objeto retornado
#
#    Exemplos:
#    | tipo de produto         | status da requisição | status da resposta |
#    | simples                 | 201                  | sucesso            |
#    | mais de uma cor         | 201                  | sucesso            |
#    | mais de um componente   | 201                  | sucesso            |
#    | sem cor                 | 400                  | erro               |
#    | sem componentes         | 400                  | erro               |
#    | sem valor               | 400                  | erro               |

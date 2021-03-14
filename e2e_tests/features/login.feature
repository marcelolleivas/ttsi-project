# language: pt
# encoding: utf-8


Funcionalidade: Login

  Esquema do Cenário: : Login
    Quando insiro usuário "<usuario login>"
    E insiro a senha "<usuario senha>"
    E clico em entrar
    Então devo estar na rota "<tipo de rota>"

    Exemplos:
    | usuario login   | usuario senha | tipo de rota |
    | marceloleivass  | marcelo123    | positiva     |
    | marceloleivass  | loremipsum    | negativa     |
    | loremipsum      | loremipsum    | negativa     |

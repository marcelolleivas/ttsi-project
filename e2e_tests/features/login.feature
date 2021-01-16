# language: pt
# encoding: utf-8


Funcionalidade: Login

Contexto: Tela de login
    Dado que esteja na página de login da lojinha

  Cenário: Fazer acesso com usuário válido
    Quando insiro usuário válido
    E insiro a senha
    E clico em entrar
    Então devo estar na página de lista de produtos
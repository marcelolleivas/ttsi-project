# language: pt
# encoding: utf-8

Funcionalidade: Criar produto


Contexto: Tela de Adicionar Produto
    Dado que esteja na página de "adicionar produto"

  Cenário: Imputar dados válidos e concluir inserção
    Quando insiro valor em "nome do produto"
    E insiro valor em "valor do produto"
    E insiro valor em "cores do produto
    E clico no botão "salvar"
    Então sistema deve retornar mensagem "Produto adicionado com sucesso"
    E lista de produtos deve constar novo produto

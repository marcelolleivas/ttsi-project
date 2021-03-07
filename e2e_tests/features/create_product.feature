# language: pt
# encoding: utf-8

Funcionalidade: Criar produto


Contexto: Tela de Adicionar Produto
    Dado que esteja na página de adicionar produto


    Esquema do Cenário: Adicionar produto

      Quando insere nome "<nome>"
      E insere valor "<valor>"
      E insere cor "<cor>"
      E clica em "<nome do botao>"
      Então deve haver mensagem "<corpo da mensagem>" na interface
      E lista de produtos "<tipo de validacao>" produto

      Exemplos:
      | nome           | valor    | cor          | nome do botao  | corpo da mensagem | tipo de validacao |
      | playstation 5  | 3.000,00 | preto        | salvar         | sucesso           | contem            |
      | playstation 5  | 3.000,00 | preto, cinza | salvar         | sucesso           | contem            |
#      | vazio          | 3.000,00 | preto        | salvar         | erro              | nao contem        |
#      | playstation 5  | vazio    | preto        | salvar         | erro              | nao contem        |
#      | playstation 5  | 3.000,00 | vazio        | salvar         | erro              | nao contem        |


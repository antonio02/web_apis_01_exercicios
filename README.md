# Web API's

## Lorem Picsum

Api para teste de Templates que utilizam imagens.

Exemplo de URL's

- https://picsum.photos/200 // Foto quadrada
- https://picsum.photos/200/300/?random // Foto aleatória
- https://picsum.photos/200/300/?blur // Imagem com efeito blur

## Exchange Rates Api

Api com taxas de cambio atuais e histórico de cambio para varias moedas.

Exemplo de URL's

- https://api.exchangeratesapi.io/lastest // Taxa de cambio para data atual (Default EUR)
- https://api.exchangeratesapi.io/2014-01-01 // Taxa de cambio de uma data especifica 
- https://api.exchangeratesapi.io//history?start_at=2018-12-01&end_at=2018-12-19&symbols=USD&base=BRL // Histórico de taxa de cambio usando como base o Real brasileiro
- 
## Stripe

Api para processamento de pagamentos, permitindo que pessoas e empresas recebam pagamentos pela internet.

Exemplo de URL's

- https://api.stripe.com/v1/customers // Cria um cliente em caso de POST e lista os clientes em caso de GET
- https://api.stripe.com/v1/customers/{id} // Ver e atualizar cliente 
-  https://api.stripe.com/v1/balance // Saldo atual da conta
- https://api.stripe.com/v1/products // Cria e lista produtos

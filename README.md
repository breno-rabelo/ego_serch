# Análise de Sentimentos no Twitter com Tweepy e Transformers

## Descrição
Este projeto permite buscar tweets recentes relacionados a um tema de interesse e analisar o sentimento desses tweets utilizando um modelo de machine learning baseado no BERT para a língua portuguesa.

## Tecnologias Utilizadas
- **Python 3**
- **Tweepy**: Para interação com a API do Twitter
- **Transformers**: Para análise de sentimentos utilizando o modelo `neuralmind/bert-base-portuguese-cased`

## Instalação
Antes de executar o projeto, instale as dependências necessárias:
```sh
pip install tweepy transformers
```

## Como Usar
1. **Configurar credenciais da API do Twitter**
   - Substitua as credenciais no código pelo seu `API_KEY`, `API_SECRET` e `BEARER_TOKEN`.

2. **Executar o Script**
   - Rode o script Python e insira um termo de busca quando solicitado.

3. **Visualizar os Resultados**
   - O script busca tweets recentes (excluindo retweets) e exibe a análise de sentimento para cada um deles.

## Exemplo de Uso
```sh
python script.py
Digite sua busca: Inteligência Artificial
[{'label': 'POSITIVE', 'score': 0.95}, {'label': 'NEGATIVE', 'score': 0.87}]
```

## Possíveis Erros e Soluções
- **Erro de autenticação**: Verifique se suas credenciais estão corretas.
- **Módulo não encontrado**: Instale os pacotes com `pip install tweepy transformers`.
- **Erro de taxa da API do Twitter**: Caso atinja o limite de requisições, aguarde e tente novamente.

## Licença
Este projeto é distribuído sob a licença MIT.


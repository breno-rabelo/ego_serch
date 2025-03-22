# X API KEY : HYNuKr21kbfk1fcbXc9YsBKun
# X APY KEY SEECRET: NXSrwiJetdCHbbL6XBsZLAHS227BuJz8f7PCx65LUe8rNyjbls
# A API e limitada a 20
import tweepy

API_KEY = 'API_KEY'
API_SECRET = 'API_SECRET'
BEARER_TOKEN = 'BEARER_TOKEN'

# Autenticando a chave API com Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# buscar tweets por um tema
search = input('Digite sua busca: ')
query = f'{search} -is:retweet lang:pt'
tweets = client.search_recent_tweets(query=query, max_results=10)

# usando modelo para sentimentos
from tranformers import pipeline

sentiment_pipeline = pipeline('sentiment-analysis', model='neuralmind/bert-base-portuguese-cased')
result = sentiment_pipeline(tweets)

print(result)

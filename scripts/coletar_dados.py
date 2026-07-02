import requests
import psycopg2
from datetime import datetime, UTC

# Configuração do banco (Render External URL)
DB_URL = "postgresql://analise_i_a_user:kaojQtQcUBCRr3HQJZwzLRbc6srJqWDt@dpg-d92qvujtqb8s73cm21qg-a.oregon-postgres.render.com/analise_i_a"

def salvar_crypto(symbol, name, price):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO cryptos (symbol, name, price_usd, updated_at)
        VALUES (%s, %s, %s, %s)
    """, (symbol, name, price, datetime.now(UTC)))
    conn.commit()
    cur.close()
    conn.close()

def salvar_news(title, source):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO history (query, result, created_at)
        VALUES (%s, %s, %s)
    """, ("crypto_news", title, datetime.now(UTC)))
    conn.commit()
    cur.close()
    conn.close()

# Exemplo: pegar preço do CoinGecko
def coletar_precos():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    data = requests.get(url).json()
    salvar_crypto("BTC", "Bitcoin", data["bitcoin"]["usd"])
    salvar_crypto("ETH", "Ethereum", data["ethereum"]["usd"])

# Exemplo: pegar notícia do NewsAPI
def coletar_noticias():
    url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey=c1db2aed1fd74d9dad7677e66db11474"
    data = requests.get(url).json()
    if "articles" in data and data["articles"]:
        artigo = data["articles"][0]
        salvar_news(artigo["title"], artigo["source"]["name"])
    else:
        print("Nenhuma notícia encontrada ou erro na API:", data)

if __name__ == "__main__":
    coletar_precos()
    coletar_noticias()

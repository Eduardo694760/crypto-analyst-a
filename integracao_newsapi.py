import requests
import psycopg2

# 1. Buscar notícias sobre criptomoedas
url = "https://newsapi.org/v2/everything"
params = {
    "q": "cryptocurrency OR bitcoin OR ethereum",
    "language": "pt",
    "sortBy": "publishedAt"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "X-Api-Key": "c1db2aed1fd74d9dad7677e66db11474"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code != 200:
    print(f"Erro do servidor (Código {response.status_code}):")
    print(response.text)
    exit()

data = response.json()

# 2. Conectar ao PostgreSQL
conn = psycopg2.connect(
    dbname="crypto_db",
    user="crypto_user",
    password="eduardo48",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 3. Inserir manchetes na tabela history
if "articles" in data:
    for article in data["articles"]:
        titulo_curto = article["title"][:100] if article["title"] else "Notícia sem título"
        
        cur.execute("""
            INSERT INTO history (user_id, query, result, created_at)
            VALUES (%s, %s, %s, NOW())
        """, (1, "crypto_news", titulo_curto))

    conn.commit()
    print("Notícias integradas e salvas com sucesso!")

cur.close()
conn.close()

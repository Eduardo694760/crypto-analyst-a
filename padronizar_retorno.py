import psycopg2
import json

# 1. Conectar ao banco
conn = psycopg2.connect(
    dbname="crypto_db",
    user="crypto_user",
    password="eduardo48",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 2. Buscar dados das criptos
cur.execute("SELECT symbol, name, price_usd, updated_at FROM cryptos;")
cryptos = [
    {"symbol": row[0], "name": row[1], "price_usd": float(row[2]), "updated_at": row[3].isoformat()}
    for row in cur.fetchall()
]

# 3. Buscar últimas notícias
cur.execute("SELECT result, created_at FROM history WHERE query = 'crypto_news' ORDER BY id DESC LIMIT 5;")
news = [
    {"title": row[0], "source": "NewsAPI", "created_at": row[1].isoformat()}
    for row in cur.fetchall()
]

# 4. Buscar última análise da IA
cur.execute("SELECT source, content, created_at FROM analysis ORDER BY id DESC LIMIT 1;")
row = cur.fetchone()
analysis = []
if row:
    analysis.append({"source": row[0], "content": row[1], "created_at": row[2].isoformat()})

cur.close()
conn.close()

# 5. Montar JSON padronizado
resultado = {
    "cryptos": cryptos,
    "news": news,
    "analysis": analysis
}

# 6. Exibir JSON formatado
print(json.dumps(resultado, indent=4, ensure_ascii=False))

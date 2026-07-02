import psycopg2

# Conectar ao banco
conn = psycopg2.connect(
    dbname="crypto_db",
    user="crypto_user",
    password="eduardo48",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1. Testar dados da CoinGecko
cur.execute("SELECT symbol, price_usd FROM cryptos;")
for symbol, price in cur.fetchall():
    if price is None or price <= 0:
        print(f"❌ Erro: preço inválido para {symbol}")
    else:
        print(f"✅ Preço válido para {symbol}: {price}")

# 2. Testar dados da NewsAPI
cur.execute("SELECT result FROM history WHERE query = 'crypto_news' LIMIT 5;")
for (titulo,) in cur.fetchall():
    if not titulo or titulo.strip() == "":
        print("❌ Erro: notícia sem título")
    else:
        print(f"✅ Notícia válida: {titulo[:60]}...")

# 3. Testar dados da IA
cur.execute("SELECT content FROM analysis ORDER BY id DESC LIMIT 1;")
(content,) = cur.fetchone()
if not content or content.strip() == "":
    print("❌ Erro: análise da IA vazia")
else:
    print("✅ Análise da IA válida")

cur.close()
conn.close()

import requests
import psycopg2

# 1. Buscar dados reais da CoinGecko
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "ids": "bitcoin,ethereum"}
response = requests.get(url, params=params)
data = response.json()

# 2. Conectar ao PostgreSQL com as credenciais certas
conn = psycopg2.connect(
    dbname="crypto_db",
    user="crypto_user",
    password="eduardo48",  # <-- AJUSTE AQUI SE A SENHA DO CRYPTO_USER FOR OUTRA
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 3. Inserir ou atualizar dados na tabela cryptos
for coin in data:
    # Transforma o símbolo em maiúsculo (ex: btc -> BTC)
    simbolo_maiusculo = coin["symbol"].upper()
    
    cur.execute("""
        INSERT INTO cryptos (symbol, name, market_cap, price_usd, updated_at)
        VALUES (%s, %s, %s, %s, NOW())
        ON CONFLICT (symbol) DO UPDATE
        SET market_cap = EXCLUDED.market_cap,
            price_usd = EXCLUDED.price_usd,
            updated_at = NOW();
    """, (simbolo_maiusculo, coin["name"], coin["market_cap"], coin["current_price"]))

# Salva as alterações de verdade no banco
conn.commit()

# Fecha os canais de comunicação
cur.close()
conn.close()

print("Dados da CoinGecko integrados e salvos com sucesso!")

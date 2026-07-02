import psycopg2
from google import genai  # <-- Nova biblioteca oficial do Google
import os

# 1. Configurar o cliente com a sua chave do Gemini (Google)
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# 2. Conectar ao PostgreSQL
conn = psycopg2.connect(
    dbname="crypto_db",
    user="crypto_user",
    password="eduardo48",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 3. Buscar últimas notícias do banco
cur.execute("SELECT result FROM history WHERE query = 'crypto_news' ORDER BY id DESC LIMIT 5;")
linhas = cur.fetchall()

# Formata as notícias extraindo o texto da tupla e limpando vazios
noticias = [row[0] for row in linhas if row[0] is not None]

if not noticias:
    print("Nenhuma notícia encontrada no banco para analisar.")
    cur.close()
    conn.close()
    exit()

# 4. Gerar o texto do prompt
noticias_formatadas = "\n".join(f"- {texto}" for texto in noticias)
prompt = f"Você é um analista especialista em mercado de criptomoedas. Resuma e analise estas últimas notícias de forma bem direta:\n\n{noticias_formatadas}"

# 5. Chamar o modelo gratuito do Gemini (modelo estável atual)
resposta = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

texto_analise = resposta.text.strip()

# 6. Salvar a análise gerada na tabela 'analysis'
cur.execute("""
    INSERT INTO analysis (source, content, created_at)
    VALUES (%s, %s, NOW())
""", ("Gemini", texto_analise))

conn.commit()

# 7. Fechar conexões
cur.close()
conn.close()

print("Análise da IA do Gemini salva com sucesso!")

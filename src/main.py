from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import psycopg2
from src.auth import create_access_token, verify_password, get_password_hash, decode_token, oauth2_scheme
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# ------------------- CONFIGURAÇÃO -------------------
app = FastAPI(title="Crypto Analyst API", version="1.0")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Servir frontend (index.html, style.css, script.js) na raiz
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Liberar CORS para permitir chamadas do navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode restringir para http://localhost:5500 se usar Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Usuário de teste (fixo)
fake_user = {
    "username": "eduardo",
    "hashed_password": get_password_hash("eduardo48")
}

def connect_db():
    return psycopg2.connect(
        "postgresql://analise_i_a_user:kaojQtQcUBCRr3HQJZwzLRbc6srJqWDt@dpg-d92qvujtqb8s73cm21qg-a/analise_i_a"
    )

# ------------------- AUTENTICAÇÃO -------------------
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != fake_user["username"] or not verify_password(form_data.password, fake_user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário ou senha inválidos")
    access_token = create_access_token(data={"sub": fake_user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    return payload["sub"]

# ------------------- ENDPOINTS -------------------
@app.get("/analysis")
def get_analysis(user: str = Depends(get_current_user)):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT source, content, created_at FROM analysis ORDER BY id DESC LIMIT 1;")
        row = cur.fetchone()
    if row:
        return {
            "source": row[0],
            "content": row[1],
            "created_at": row[2].isoformat() if row[2] else None
        }
    return {"message": "Nenhuma análise encontrada"}

@app.get("/news")
def get_news(limit: int = 5, user: str = Depends(get_current_user)):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT result, created_at FROM history WHERE query = 'crypto_news' ORDER BY id DESC LIMIT %s;", (limit,))
        rows = cur.fetchall()
    return [
        {"title": r[0], "source": "NewsAPI", "created_at": r[1].isoformat() if r[1] else None}
        for r in rows
    ]

@app.get("/compare")
def compare(symbol1: str, symbol2: str, user: str = Depends(get_current_user)):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT symbol, price_usd FROM cryptos WHERE symbol = %s OR symbol = %s;", (symbol1, symbol2))
        rows = cur.fetchall()
    return [
        {"symbol": r[0], "price_usd": float(r[1]) if r[1] else None}
        for r in rows
    ]

@app.get("/favorites")
def get_favorites(user: str = Depends(get_current_user)):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, content, created_at FROM memory WHERE type='favorito' ORDER BY id DESC;")
        rows = cur.fetchall()
    return [
        {"id": r[0], "content": r[1], "created_at": r[2].isoformat() if r[2] else None}
        for r in rows
    ]

@app.get("/history")
def get_history(limit: int = 10, user: str = Depends(get_current_user)):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, type, content, created_at FROM memory ORDER BY id DESC LIMIT %s;", (limit,))
        rows = cur.fetchall()
    return [
        {"id": r[0], "type": r[1], "content": r[2], "created_at": r[3].isoformat() if r[3] else None}
        for r in rows
    ]

@app.get("/")
def home():
    return {"status": "API online", "docs": "Acesse /docs para testar as rotas"}

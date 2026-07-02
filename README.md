# Crypto Analyst API

Uma aplicação completa para análise de criptomoedas, integrando **notícias**, **IA (Gemini)**, **banco de dados**, **autenticação JWT** e **frontend interativo**.

---

## 🚀 Funcionalidades
- [Autenticação JWT](ca://s?q=Autenticacao_JWT) segura com endpoint `/token`.
- [Integração com Gemini](ca://s?q=Integracao_com_Gemini) para análises inteligentes.
- [Integração com NewsAPI](ca://s?q=Integracao_com_NewsAPI) para puxar notícias atualizadas.
- [Banco de dados](ca://s?q=Banco_de_dados_SQLAlchemy) com histórico, favoritos e usuários.
- [Frontend](ca://s?q=Frontend_com_HTML_JS_CSS) em HTML/CSS/JS consumindo os endpoints.
- Deploy automático no [Render](ca://s?q=Deploy_no_Render).

---

## 📂 Estrutura do projeto
crypto-analyst-a/
├── src/
│   ├── api/          # Rotas da API
│   ├── models/       # Modelos do banco
│   ├── services/     # Serviços (IA, notícias, etc.)
│   └── main.py       # Inicialização FastAPI
├── integracao_ia.py  # Integração Gemini
├── integracao_newsapi.py # Integração NewsAPI
├── frontend/         # Interface web
├── requirements.txt  # Dependências
├── Procfile          # Configuração Render
└── README.md         # Documentação

Código

---

## ⚙️ Instalação local

1. Clone o repositório:
   ```bash
   git clone https://github.com/Eduardo694760/crypto-analyst-a.git
   cd crypto-analyst-a
Crie e ative o ambiente virtual:

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Crie o arquivo .env:

Código
NEWS_API_KEY=coloque_sua_chave_newsapi_aqui
GEMINI_API_KEY=coloque_sua_chave_gemini_aqui
Inicie o servidor local:

bash
uvicorn src.main:app --reload
🌐 Deploy no Render
Suba o código no GitHub (sem .env, venv/, __pycache__/).

Crie um novo serviço no Render conectado ao repositório.

Em Settings → Environment Variables, adicione:

NEWS_API_KEY

GEMINI_API_KEY

Deploy automático será feito a cada push no branch clean-main.

🔑 Autenticação
Gere um token em /token informando usuário e senha.

Use o JWT nas chamadas protegidas (Authorization: Bearer <token>).

🖥️ Frontend
O frontend está em frontend/ e consome os endpoints da API.

Basta abrir index.html no navegador ou configurar deploy estático.

As requisições usam fetch para chamar os endpoints hospedados no Render.

📖 Endpoints principais
POST /token → Gera JWT.

GET /analysis → Análise de criptomoedas via Gemini.

GET /news → Notícias atualizadas via NewsAPI.

GET /compare → Comparação de ativos.

GET /favorites → Lista de favoritos do usuário.

GET /history → Histórico de consultas.

✅ Status do projeto
Este projeto foi desenvolvido como portfólio para estágio.
Inclui backend, banco de dados, segurança e frontend funcional.
Melhorias futuras podem incluir testes mais robustos, CI/CD e dashboards avançados.
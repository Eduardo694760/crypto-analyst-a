from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_data():
    conn = psycopg2.connect(
        dbname="crypto_db",
        user="crypto_user",
        password="eduardo48",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Criptos
    cur.execute("SELECT symbol, name, price_usd, updated_at FROM cryptos;")
    cryptos = [
        {"symbol": row[0], "name": row[1], "price_usd": float(row[2]), "updated_at": row[3].isoformat()}
        for row in cur.fetchall()
    ]

    # Notícias
    cur.execute("SELECT result, created_at FROM history WHERE query = 'crypto_news' ORDER BY id DESC LIMIT 5;")
    news = [
        {"title": row[0], "source": "NewsAPI", "created_at": row[1].isoformat()}
        for row in cur.fetchall()
    ]

    # Última análise da IA
    cur.execute("SELECT source, content, created_at FROM analysis ORDER BY id DESC LIMIT 1;")
    row = cur.fetchone()
    analysis = []
    if row:
        analysis.append({"source": row[0], "content": row[1], "created_at": row[2].isoformat()})

    cur.close()
    conn.close()

    return {"cryptos": cryptos, "news": news, "analysis": analysis}

def get_context(limit=5):
    conn = psycopg2.connect(
        dbname="crypto_db",
        user="crypto_user",
        password="eduardo48",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT type, content FROM memory ORDER BY id DESC LIMIT %s;", (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"type": r[0], "content": r[1]} for r in rows]

@app.route("/api/data", methods=["GET"])
def api_data():
    return jsonify(get_data())

@app.route("/api/memory", methods=["GET", "POST", "DELETE"])
def api_memory():
    conn = psycopg2.connect(
        dbname="crypto_db",
        user="crypto_user",
        password="eduardo48",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    if request.method == "GET":
        cur.execute("SELECT id, type, content, created_at FROM memory ORDER BY id DESC LIMIT 20;")
        rows = cur.fetchall()
        mems = [
            {"id": r[0], "type": r[1], "content": r[2], "created_at": r[3].isoformat()}
            for r in rows
        ]
        cur.close()
        conn.close()
        return jsonify(mems)

    elif request.method == "POST":
        data = request.json
        cur.execute("INSERT INTO memory (type, content) VALUES (%s, %s)", (data["type"], data["content"]))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "saved"}), 201

    elif request.method == "DELETE":
        mem_id = request.args.get("id")
        cur.execute("DELETE FROM memory WHERE id = %s", (mem_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "deleted"})

@app.route("/api/context", methods=["GET"])
def api_context():
    return jsonify(get_context())

if __name__ == "__main__":
    app.run(debug=True)

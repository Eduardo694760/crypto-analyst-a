// ============================
// Configuração
// ============================
const API_BASE = "https://crypto-analyst-a.onrender.com/"; 
const TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZHVhcmRvIiwiZXhwIjoxNzgzMDA2ODg5fQ.ElR6nQfEY1PsKjx9zb1zJk-lpvQh-06w..."; // JWT gerado no /token

// ============================
// Elementos do DOM
// ============================
const btcPriceEl = document.getElementById("btc-price");
const ethPriceEl = document.getElementById("eth-price");
const newsListEl = document.getElementById("news-list");
const aiAnalysisEl = document.getElementById("ai-analysis");
const historyListEl = document.getElementById("history-list");
const errorMessageEl = document.getElementById("error-message");

// Canvas para gráfico
const compareChartCtx = document.getElementById("compareChart")?.getContext("2d");
let compareChart; // variável global para armazenar o gráfico

// ============================
// Função auxiliar para requisições
// ============================
async function fetchData(endpoint) {
    const res = await fetch(`${API_BASE}/${endpoint}`, {
        headers: { Authorization: `Bearer ${TOKEN}` }
    });

    if (!res.ok) {
        const errorText = await res.text();
        throw new Error(`Erro ${res.status}: ${errorText}`);
    }

    return res.json();
}

// ============================
// Formata número como preço em dólar
// ============================
function formatPrice(value) {
    const number = Number(value);
    if (isNaN(number)) return "N/A";
    return number.toLocaleString("en-US", {
        style: "currency",
        currency: "USD",
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

// ============================
// Exibe/oculta mensagem de erro
// ============================
function showError(show, msg = "") {
    errorMessageEl.style.display = show ? "block" : "none";
    if (show) errorMessageEl.textContent = msg;
}

// ============================
// Busca preços de BTC e ETH + gráfico
// ============================
async function loadCompare() {
    try {
        const data = await fetchData("compare?symbol1=BTC&symbol2=ETH");
        const btc = data.filter(c => c.symbol === "BTC").map(c => c.price_usd);
        const eth = data.filter(c => c.symbol === "ETH").map(c => c.price_usd);

        btcPriceEl.textContent = btc.length ? formatPrice(btc[btc.length - 1]) : "Indisponível";
        ethPriceEl.textContent = eth.length ? formatPrice(eth[eth.length - 1]) : "Indisponível";

        const labels = data.map((_, i) => `#${i+1}`);

        if (compareChart) {
            compareChart.data.labels = labels;
            compareChart.data.datasets[0].data = btc;
            compareChart.data.datasets[1].data = eth;
            compareChart.update();
        } else if (compareChartCtx) {
            compareChart = new Chart(compareChartCtx, {
                type: "line",
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: "BTC (USD)",
                            data: btc,
                            borderColor: "#f2a900",
                            backgroundColor: "rgba(242,169,0,0.2)",
                            fill: true,
                            tension: 0.3
                        },
                        {
                            label: "ETH (USD)",
                            data: eth,
                            borderColor: "#3c3c3d",
                            backgroundColor: "rgba(60,60,61,0.2)",
                            fill: true,
                            tension: 0.3
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: "top" },
                        title: { display: true, text: "Evolução dos preços BTC vs ETH" }
                    }
                }
            });
        }
    } catch (err) {
        btcPriceEl.textContent = "Erro";
        ethPriceEl.textContent = "Erro";
        showError(true, err.message);
    }
}

// ============================
// Busca notícias
// ============================
async function loadNews() {
    try {
        const data = await fetchData("news?limit=3");
        newsListEl.innerHTML = "";

        if (!Array.isArray(data) || data.length === 0) {
            newsListEl.innerHTML = "<li>Nenhuma notícia disponível no momento.</li>";
            return;
        }

        data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.title} (${item.source})`;
            newsListEl.appendChild(li);
        });
    } catch (err) {
        newsListEl.innerHTML = `<li>${err.message}</li>`;
        showError(true, err.message);
    }
}

// ============================
// Busca análise da IA
// ============================
async function loadAnalysis() {
    try {
        const data = await fetchData("analysis");
        aiAnalysisEl.textContent = data.content || "Nenhuma análise disponível no momento.";
    } catch (err) {
        aiAnalysisEl.textContent = err.message;
        showError(true, err.message);
    }
}

// ============================
// Busca histórico
// ============================
async function loadHistory() {
    try {
        const data = await fetchData("history?limit=10");
        historyListEl.innerHTML = "";

        if (!Array.isArray(data) || data.length === 0) {
            historyListEl.innerHTML = "<li>Nenhum histórico disponível.</li>";
            return;
        }

        data.forEach(item => {
            const li = document.createElement("li");
            const createdAt = item.created_at ? new Date(item.created_at).toLocaleString() : "Sem data";
            li.textContent = `${item.type}: ${item.content} (${createdAt})`;
            historyListEl.appendChild(li);
        });
    } catch (err) {
        historyListEl.innerHTML = `<li>${err.message}</li>`;
        showError(true, err.message);
    }
}

// ============================
// Inicialização
// ============================
document.addEventListener("DOMContentLoaded", () => {
    loadCompare();
    loadNews();
    loadAnalysis();
    loadHistory();
});

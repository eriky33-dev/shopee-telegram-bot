import requests
import random
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

POSTS = [
    """🔥 OFERTA IMPERDÍVEL 🔥

📦 {nome}
⭐ Avaliação: {nota}
🛒 +{vendas} vendidos

💰 Apenas R$ {preco}

👉 COMPRAR AGORA:
{link}
""",
    """✅ SUCESSO DE VENDAS NA SHOPEE

📦 {nome}
⭐ Nota: {nota}
🛒 Mais de {vendas} compradores

💸 Preço hoje: R$ {preco}

👉 Link:
{link}
""",
    """⏰ CORRE ANTES QUE ACABE!

🔥 {nome}
⭐ {nota} estrelas
🛒 {vendas}+ vendas

💰 R$ {preco}

👉 GARANTIR:
{link}
"""
]

def enviar_produto(produto):
    texto = random.choice(POSTS).format(**produto)

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "photo": produto["imagem"],
        "caption": texto
    }
    requests.post(url, data=payload)

def buscar_produtos():
    # ⚠️ SIMULAÇÃO — depois você conecta na Shopee API real
    return [{
        "nome": "Produto campeão de vendas",
        "nota": "4.9",
        "vendas": "2350",
        "preco": "79,90",
        "imagem": "https://via.placeholder.com/500",
        "link": "https://shopee.com.br"
    }]

if __name__ == "__main__":
    produtos = buscar_produtos()
    for produto in produtos:
        enviar_produto(produto)

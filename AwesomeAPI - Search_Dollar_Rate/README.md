# Conversor de Moedas com AwesomeAPI

Este repositório contém uma aplicação Python que utiliza a **[AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)** para obter 
a taxa de câmbio do dólar (Dollar_Rate) em relação a uma moeda especificada pelo usuário.

---

## 📋 Funcionalidades

- Consulta a taxa de câmbio do dólar (USD) para uma moeda específica.
- Exibe informações atualizadas em tempo real.
- Permite múltiplas consultas em uma única execução.

---

## 🛠️ Configuração do Ambiente

### **1. Requisitos**
- Python 3.8 ou superior.
- Gerenciador de pacotes `pip`.
- Conexão com a internet para acessar a API.

### **2. Instalação**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/conversor-moedas.git
   cd conversor-moedas

## 🔧 Configuração da API

- A aplicação utiliza a AwesomeAPI para realizar as consultas de taxa de câmbio. O endpoint principal utilizado é:
  https://economia.awesomeapi.com.br/json/last/USD-{MOEDA}
  Exemplo de Requisição

- Para consultar a taxa de câmbio do dólar para o real (BRL):

- GET https://economia.awesomeapi.com.br/json/last/USD-BRL

- Exemplo de Resposta

  {
    "USDBRL": {
      "code": "USD",
      "codein": "BRL",
      "name": "Dólar Americano/Real Brasileiro",
      "high": "5.25",
      "low": "5.20",
      "varBid": "0.01",
      "pctChange": "0.19",
      "bid": "5.22",
      "ask": "5.23",
      "timestamp": "1682000000",
      "create_date": "2023-04-20 10:00:00"
    }
  }

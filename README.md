Setup Steps: Instructions on installing dependencies using pip install -r requirements.txt and setting up the .env file.  
How to Run Examples
1. Placing a MARKET Order
* python cli.py --symbol ETHUSDT --side BUY --type MARKET --quantity 0.05
2. Placing a LIMIT Order
* python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 68500

# Simplified Binance Futures Trading Bot (USDT-M)

A lightweight, modular Python Command Line Interface (CLI) application built to interact with the Binance Futures Testnet. [cite_start]This bot allows users to seamlessly place **MARKET** and **LIMIT** orders for both **BUY** and **SELL** sides while maintaining a clean separation between the user-facing CLI layer and the network API client layer[cite: 6, 18, 19, 20, 31].

---

## 🏗️ Project Architecture

[cite_start]The repository adheres strictly to a clean, multi-layered Python package structure[cite: 31, 48]:

```text
trading_bot/
├── bot/
│   ├── __init__.py          # Marks the directory as a Python package
│   ├── client.py            # Low-level Binance API client & cryptographic signing layer
│   ├── logging_config.py    # Standardized logging setup (console + file outputs)
│   ├── orders.py            # High-level order orchestration logic
│   └── validators.py        # Strict user-input validation logic
├── cli.py                   # Main application entry point handling CLI arguments
├── requirements.txt         # Project external dependencies
└── README.md                # Project documentation

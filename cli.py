import os
import argparse
from dotenv import load_dotenv
from bot.logging_config import setup_logging
from bot.client import BinanceFuturesClient
from bot.orders import execute_order

# Load environment variables from a .env file
load_dotenv()

def main():
    # Initialize structured logging
    setup_logging()

    # Parse command line inputs
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Simplified Trading Bot CLI")
    
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="Order side (BUY or SELL)")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"], help="Order execution type (MARKET or LIMIT)")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity size")
    parser.add_argument("--price", type=float, default=None, help="Target entry price (Required only for LIMIT orders)")

    args = parser.parse_args()

    # Retrieve testnet credentials safely from environments
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("\n❌ Configuration Error: Please ensure BINANCE_API_KEY and BINANCE_API_SECRET are set in your .env file.\n")
        return

    # Initialize Client and Execute Order Chain
    client = BinanceFuturesClient(api_key=api_key, api_secret=api_secret)
    execute_order(
        client=client,
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

if __name__ == "__main__":
    main()

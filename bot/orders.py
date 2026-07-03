import logging
from bot.validators import validate_inputs
from bot.client import BinanceFuturesClient

logger = logging.getLogger("OrderManager")

def execute_order(client: BinanceFuturesClient, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    try:
        validate_inputs(symbol, side, order_type, quantity, price)
    except ValueError as val_err:
        logger.error(f"Validation Failure: {str(val_err)}")
        print(f"\n❌ Input Validation Error: {str(val_err)}")
        return

    print("\n========================================")
    print("        ORDER REQUEST SUMMARY           ")
    print("========================================")
    print(f"🔹 Symbol:    {symbol.upper()}")
    print(f"🔹 Side:      {side.upper()}")
    print(f"🔹 Type:      {order_type.upper()}")
    print(f"🔹 Quantity:  {quantity}")
    if order_type.upper() == "LIMIT":
        print(f"🔹 Price:     {price}")
    print("========================================\n")

    response = client.post_order(symbol, side, order_type, quantity, price)

    print("========================================")
    print("        ORDER RESPONSE DETAILS          ")
    print("========================================")
    if response.get("error"):
        print(f"❌ Order Placement Failed!")
        print(f"Error Message: {response.get('msg', 'Unknown Error')}")
    else:
        print(f"✅ Order Placed Successfully!")
        print(f"📝 Order ID:      {response.get('orderId')}")
        print(f"📊 Status:        {response.get('status')}")
        print(f"🔄 Executed Qty:  {response.get('executedQty')}")
        print(f"💵 Avg Price:     {response.get('avgPrice', 'N/A')}")
    print("========================================\n")

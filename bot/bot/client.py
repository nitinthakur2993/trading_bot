import time
import hmac
import hashlib
import requests
import logging
from urllib.parse import urlencode

logger = logging.getLogger("BinanceClient")

class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self, api_key: str, api_secret: str):
        if not api_key or not api_secret:
            raise ValueError("API Key and API Secret must be provided.")
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {
            "X-MBX-APIKEY": self.api_key
        }

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def post_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        endpoint = f"{self.BASE_URL}/fapi/v1/order"
        
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
            "timestamp": int(time.time() * 1000),
            "recvWindow": 5000
        }
        
        if order_type.upper() == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        payload = f"{query_string}&signature={signature}"

        logger.info(f"Sending API Order Request: URL={endpoint} | Payload={query_string}")

        try:
            response = requests.post(endpoint, data=payload, headers=self.headers, timeout=10)
            response_json = response.json()
            
            if response.status_code == 200:
                logger.info(f"API Order Success: {response_json}")
                return response_json
            else:
                logger.error(f"API Error Response [HTTP {response.status_code}]: {response_json}")
                return {"error": True, "code": response_json.get("code"), "msg": response_json.get("msg")}
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Network failure encountered: {str(e)}")
            return {"error": True, "msg": f"Network Error: {str(e)}"}

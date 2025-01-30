

# from typing import List, Optional, Type
# from pydantic import Field, BaseModel
# from langchain.tools import BaseTool

from helper import *
from pydantic import BaseModel, Field
from typing import Optional, Type
from langchain.tools import BaseTool
from functions import *
import json


class StockPriceCheckInput(BaseModel):
    """Input for Stock price check."""

    stockticker: str = Field(..., description="Ticker symbol for stock or index")


class StockPriceTool(BaseTool):
    name: str = "get_stock_ticker_price"
    description: str = "Useful for when you need to find out the price of stock. You should input the stockticker used on the yfinance API. No JSON format for this."

    def _run(self, stockticker: str):
        # print("i'm running")
        price_response = get_stock_price(stockticker)

        return price_response

    def _arun(self, stockticker: str):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = StockPriceCheckInput

# ------------------------------------------
# Stock Percentage Change Tool (Single JSON Input)
# ------------------------------------------
# class StockChangePercentageCheckInput(BaseModel):
#     """Input for Stock ticker percentage change check, wrapped in JSON."""

#     input_json: str = Field(..., description="A JSON containing stockticker and days_ago")

# class StockPercentageChangeTool(BaseTool):
#     name: str = "get_price_change_percent"
#     description: str = (
#         "Useful for when you need to find out the percentage change in a stock's value. "
#         "You should input a JSON string containing 'stockticker' and 'days_ago'."
#     )

#     def _run(self, input_json: str):
#         try:
#             # Parse JSON input
#             print(f"Recieved input: {input_json}")
#             data = json.loads(input_json)
#             required_keys = {"stockticker", "days_ago"}
#             missing_keys = required_keys - data.keys()

#             if missing_keys:
#                 raise ValueError(f"Missing keys in JSON input: {missing_keys}")
            
#             stockticker = data.get("stockticker")
#             days_ago = data.get("days_ago")

#             if not isinstance(stockticker, str):
#                 raise ValueError("Invalid 'stockticker': Expected a string.")
#             if not isinstance(days_ago, int):
#                 raise ValueError("Invalid 'days_ago': Expected an integer.")
            
#             # Call the actual function
#             price_change_response = get_price_change_percent(stockticker, days_ago)
#             return price_change_response
        
#         except json.JSONDecodeError:
#             return "Invalid JSON format. Please provide a valid JSON string."
#         except ValueError as e:
#             return f"Error: {str(e)}"

#     def _arun(self, input_json: str):
#         raise NotImplementedError("This tool does not support async")

#     args_schema: Optional[Type[BaseModel]] = StockChangePercentageCheckInput

# class StockBestPerformingInput(BaseModel):
#     """Input for getting best-performing stocks, wrapped in JSON."""

#     input_json: str = Field(..., description="A JSON string containing stocktickers (list) and days_ago")

# class StockGetBestPerformingTool(BaseTool):
#     name: str = "get_best_performing"
#     description: str = (
#         "Useful for checking the performance of multiple stocks over a period. "
#         "You should input a JSON string containing 'stocktickers' (a list of stock symbols) "
#         "and 'days_ago' (an integer representing the number of days ago to compare). "
#     )

#     def _run(self, input_json: str):
#         try:
#             print(f"Received Input: {input_json}")  # Debugging

#             # Parse JSON input safely
#             data = json.loads(input_json)

#             # Validate required keys
#             required_keys = {"stocktickers", "days_ago"}
#             missing_keys = required_keys - data.keys()
#             if missing_keys:
#                 raise ValueError(f"Missing input keys: {', '.join(missing_keys)}")

#             # Extract values
#             stocktickers = data.get("stocktickers")
#             days_ago = data.get("days_ago")

#             # Validate types
#             if not isinstance(stocktickers, list) or not all(isinstance(ticker, str) for ticker in stocktickers):
#                 raise ValueError("Invalid 'stocktickers': Expected a list of stock symbols as strings.")
#             if not isinstance(days_ago, int):
#                 raise ValueError("Invalid 'days_ago': Expected an integer.")

#             # Call the actual function
#             price_change_response = get_best_performing(stocktickers, days_ago)
#             return price_change_response

#         except json.JSONDecodeError:
#             return "Invalid JSON format. Please provide a valid JSON string."
#         except ValueError as e:
#             return f"Error: {str(e)}"

class StockChangePercentageCheckInput(BaseModel):
    """Input for Stock ticker check. for percentage check"""

    stockticker: str = Field(..., description="Ticker symbol for stock or index")
    days_ago: int = Field(..., description="Int number of days to look back")

class StockPercentageChangeTool(BaseTool):
    name: str = "get_price_change_percent"
    description: str = "Useful for when you need to find out the percentage change in a stock's value. You should input the stock ticker used on the yfinance API and also input the number of days to check the change over"

    def _run(self, stockticker: str, days_ago: int):
        price_change_response = get_price_change_percent(stockticker, days_ago)
        return price_change_response


    def _arun(self, stockticker: str, days_ago: int):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = StockChangePercentageCheckInput


# the best performing

class StockBestPerformingInput(BaseModel):
    """Input for Stock ticker check. for percentage check"""

    stocktickers: List[str] = Field(..., description="Ticker symbols for stocks or indices")
    days_ago: int = Field(..., description="Int number of days to look back")

class StockGetBestPerformingTool(BaseTool):
    name: str = "get_best_performing"
    description: str = "Useful for when you need to the performance of multiple stocks over a period. You should input a list of stock tickers used on the yfinance API and also input the number of days to check the change over"

    def _run(self, stocktickers: List[str], days_ago: int):
        price_change_response = get_best_performing(stocktickers, days_ago)

        return price_change_response

    def _arun(self, stockticker: List[str], days_ago: int):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = StockBestPerformingInput



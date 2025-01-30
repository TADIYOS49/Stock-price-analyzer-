import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import openai
from dotenv import load_dotenv

import yfinance as yf

from openai import OpenAI
from langchain.tools import BaseTool
from typing import Optional, Type, List
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage, FunctionMessage
from langchain.tools import MoveFileTool, format_tool_to_openai_function

from models import StockPriceTool, StockPercentageChangeTool, StockGetBestPerformingTool
from functions import get_best_performing,get_price_change_percent, get_stock_price
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
import json

from langchain.memory import ConversationBufferMemory
from langchain.agents import *
from langchain import LLMChain

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
GPT4 = os.getenv("MODEL")


from app.core.imports import *
from app.core.models import StockGetBestPerformingTool, StockPercentageChangeTool, StockPriceTool
from langchain.prompts.chat import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI


def create_agent(query):
    tools = [StockPriceTool(),StockGetBestPerformingTool(),StockPercentageChangeTool()]

    chat_history = MessagesPlaceholder(variable_name="chat_history")
    memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
    model = ChatOpenAI(model=GPT4, streaming = True, temperature=0) #to enable streaming of the output

#This one is for an agent that will not remember previous conversations
    open_ai_agent = initialize_agent (
        tools, model, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True, return_intermediate_steps = False,
        agent_kwargs= {
            "memory_prompts": [chat_history],
            "input_variables": ["input", "agent_scratchpad", "chat_history"]
        },
        memory = memory
    )
    response = open_ai_agent.run(query)
    return response
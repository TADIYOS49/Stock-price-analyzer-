
from helper import *


tools = [StockPriceTool(), StockPercentageChangeTool(), StockGetBestPerformingTool()]

model = ChatOpenAI(model=GPT4)

open_ai_agent = initialize_agent (
    tools, model, agent=AgentType.OPENAI_FUNCTIONS, verbose=True
)


while True:

    quesiton = input("Enter your question: ")
    print(open_ai_agent.run(quesiton))
    
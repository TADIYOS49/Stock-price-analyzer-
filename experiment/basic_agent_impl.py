
from helper import *


tools = [StockPriceTool(), StockPercentageChangeTool(), StockGetBestPerformingTool()]

model = ChatOpenAI(model=GPT4)

#This one is for an agent that will not remember previous conversations
# open_ai_agent = initialize_agent (
#     tools, model, agent=AgentType.OPENAI_FUNCTIONS, verbose=True
# )

#This one is for an agent that will be able to remember previous conversations
prefix = """Try to answer questions being asked by the user and make sure your answers are correct. You can access different tools to get the information you need."""
suffix = """Begin!

{chat_history}
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "chat_history", "agent_scratchpad"]
)

llm_chain = LLMChain(llm=model, prompt = prompt)

memory = ConversationBufferMemory(memory_key="chat_history")

agent = ZeroShotAgent(llm_chain=llm_chain, tools = tools, verbose = True)
agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)

while True:

    quesiton = input("Enter your question: ")
    if quesiton == "EXIT":
        break
    response = agent_chain.run(quesiton)
    #response = open_ai_agent.run(quesiton)
    print(response)
    
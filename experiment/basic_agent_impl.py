
from helper import *
from langchain.prompts.chat import MessagesPlaceholder


tools = [StockPriceTool(),StockGetBestPerformingTool(),StockPercentageChangeTool()]

chat_history = MessagesPlaceholder(variable_name="chat_history")
memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
model = ChatOpenAI(model=GPT4, streaming = True, temperature=0) #to enable streaming of the output

#This one is for an agent that will not remember previous conversations
open_ai_agent = initialize_agent (
    tools, model, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True,
    agent_kwargs= {
        "memory_prompts": [chat_history],
        "input_variables": ["input", "agent_scratchpad", "chat_history"]
    },
    memory = memory
)

#This one is for an agent that will be able to remember previous conversations
# prefix = """Try to answer questions being asked by the user and make sure your answers are correct. 
# If some information is missing, ask the user for clarification before executing a tool.
# You can access different tools to get the information you need."""
# suffix = """Begin!

# {chat_history}
# If the question lacks important details you need to run a tool, ask the user before procceeding.
# If you don't know the information about the tools and what they accept please ask.
# Question: {input}
# {agent_scratchpad}"""

# prompt = ZeroShotAgent.create_prompt(
#     tools,
#     prefix=prefix,
#     suffix=suffix,
#     input_variables=["input", "chat_history", "agent_scratchpad"]
# )

# llm_chain = LLMChain(llm=model, prompt = prompt)

# memory = ConversationBufferMemory(memory_key="chat_history")

# agent = ZeroShotAgent(llm_chain=llm_chain, tools = tools, verbose = True)
# agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory, handle_parsing_errors=True)

while True:

    quesiton = input("Enter your question: ")
    if quesiton == "EXIT":
        break
    #response = agent_chain.run(quesiton)
    print(open_ai_agent.run(quesiton))
    #print(response)

#Todo
# Modify the system onto API service
# Integrate Streamlit for interface
# Enable multiple users to communicate without the memory overlapping with eachother

#Note
# The agent still has some issues regarding implementing tasks. It might be due to the reason that I am using baked in agent type. 
# Next step is to improve on that
    
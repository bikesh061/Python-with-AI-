# pip install langgraph

from langgraph.graph import START,END,StateGraph
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os


load_dotenv()
#state
class My_State(TypedDict):
    country : str
    currency : str
    capital : str

groqAPI = os.getenv('GROQ_API_KEY')

# model
model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = groqAPI,
    temperature = 0.7,
    max_retries = 2,

)

# node functions
def capital_node_function(State : My_State)->My_State:
    country = State['country']
    prompt = f'''
    For this country : <country>{country}<country/>
    Give me the capital only no other texts
    '''
    capital = model.invoke(prompt).content
    State['capital'] = capital
    return State



def currency_node_function(State : My_State)->My_State:
    country = State['country']
    prompt = f'''
        For this country : <country>{country}<country/>
        Give me the currency only no other texts
        '''
    currency = model.invoke(prompt).content
    State['currency'] = currency
    return State

# building workflow
workflow = StateGraph(My_State)

# Making Nodes
workflow.add_node("capital_node", capital_node_function)
workflow.add_node("currency_node", currency_node_function)

# Adding nodes to graph
workflow.add_edge(START, "capital_node")
workflow.add_edge("capital_node","currency_node")
workflow.add_edge("currency_node", END)

#
chatbot = workflow.compile()

print(chatbot.invoke({'country': 'Nepal'}))

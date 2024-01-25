"""Module for retrieving context and generating responses for car diagnostics.

This module utilizes LangChain and OpenAI's GPT models to process and generate
diagnostic information for cars based on their make, model, year, and reported issues.
"""
import os
from flask import g
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.schema import SystemMessage
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import create_retriever_tool, create_conversational_retrieval_agent
from langchain_community.vectorstores import FAISS


def get_context(make, model, year, car_issue):
  """
  Generates a diagnostic context using LangChain and OpenAI GPT models.

  Utilizes LangChain to load a conversational retrieval agent with FAISS
  vectorstores and OpenAI embeddings. It creates a diagnostic context
  based on the provided car details (make, model, year, and issue) and
  prompts the agent to provide a diagnosis.

  Args:
    make (str): The make of the car.
    model (str): The model of the car.
    year (str): The year of the car.
    car_issue (str): The reported issue of the car.

  Returns:
    str: A string response from the conversational retrieval agent with
    diagnostic information.

  The function constructs a query combining the provided car details and
  uses the conversational agent to generate a response that includes a
  diagnosis and suggested fixes, adhering to the specified format.
  """
  llm = ChatOpenAI(temperature=0.1, openai_api_key=os.environ.get('OPENAI_API_KEY'))
  embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get('OPENAI_API_KEY'))
  car_diagnosis = FAISS.load_local("vector_files", embeddings)
  car_diagnosis = car_diagnosis.as_retriever()

  car_tool = create_retriever_tool(
  car_diagnosis,
  "search-for-car-diagnosis-context",
  "provides information about how to fix cars and what problems they have")

  tool1 = [car_tool]

  system_message = SystemMessage(
    content='''

    You are a Virtual Assistant to SUGGEST CAR DIAGNOSIS.
    BASED ON THE CAR MAKE, CAR MODEL, CAR YEAR and CAR ISSUE, PROVIDE A DESCRIPTION OF WHAT IS WRONG AND HOW TO FIX IT AND WHAT IS THE DIAGNOSIS? CAREFULLY ASSESS THE CONTEXT BEFORE ANSWERING.

    Format:

    WHAT IS THE DIAGNOSIS: ....
    add a new line here
    HOW TO FIX IT: ....

    STRICTLY USE THIS FORMAT TO ANSWER

    """
    '''
  )

  agent_executor = create_conversational_retrieval_agent(
    llm=llm,
    tools=tool1,
    system_message=system_message,
    remember_intermediate_steps=True,
    verbose=True,
    max_token_limit=4000
  )

  merged_text = 'CAR MAKE IS: ' + str(make) + '. CAR MODEL IS: ' + str(model) + '. CAR YEAR IS: ' + str(
    year) + '. CAR ISSUE IS: ' + str(car_issue)

  response = agent_executor(merged_text)
  response_text = response['output']

  response_text.replace("HOW TO FIX IT", "\n HOW TO FIX IT")

  return response_text

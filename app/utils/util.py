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


def retrieve_car_details():
  """Retrieves car details stored in Flask's global `g` object.

    Checks if the required car details (make, model, year, and issue) are present
    in the global context and returns them as a list. If any detail is missing,
    returns a list with None values.

    Returns:
      list: A list containing the car's make, model, year, and issue, or None
      values if any detail is missing.
    """
  if all(hasattr(g, attr) for attr in ['make', 'model', 'year', 'car_issue']):
    make = g.make
    model = g.model
    year = g.year
    car_issue = g.car_issue
    return [make, model, year, car_issue]
  else:
    return [None, None, None, None]


def get_context():
  """Generates a diagnostic context using LangChain and OpenAI GPT models.

    Utilizes LangChain to load a conversational retrieval agent with FAISS
    vectorstores and OpenAI embeddings. It then creates a diagnostic context
    by retrieving car details and prompts the agent to provide a diagnosis.

    Returns:
      str: A string response from the conversational retrieval agent with
      diagnostic information.
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

  details = retrieve_car_details()
  merged_text = 'CAR MAKE IS: ' + str(details[0]) + '. CAR MODEL IS: ' + str(details[1]) + '. CAR YEAR IS: ' + str(
    details[2]) + '. CAR ISSUE IS: ' + str(details[3])

  response = agent_executor(merged_text)
  response_text = response['output']

  response_text.replace("HOW TO FIX IT", "\n HOW TO FIX IT")

  return response_text

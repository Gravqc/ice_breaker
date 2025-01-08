import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


data = """
    Elon Musk
"""


if __name__ == "__main__":
    load_dotenv()
    print(os.environ['OPENAI_API_KEY'])

    template = """
        I am going to give you the name of a famous person, please give me 
        some fun facts about him. The person is {data}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["data"], template="template"
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"data": data})

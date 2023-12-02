from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

llm = OpenAI(temperature=0.5)

with open('docs/employee/job_description.md', 'r') as template_file:
    template = template_file.read()

prompt = PromptTemplate(
    input_variables=["userprompt"],
    template=template
)

parser = StrOutputParser()

chain = prompt | llm | parser

def get_response(userprompt):
    return chain.invoke({"userprompt":userprompt})


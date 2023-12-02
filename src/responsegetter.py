import logging
TAG = "#RESPONSEGETTER"

logging.basicConfig(level=logging.DEBUG) 

def log(msg, tag=TAG):
    logging.debug("%s: %s", tag, str(msg)) 

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

def get_preprompt():
    with open('docs/preprompt.md', 'r') as template_file:
        preprompt = template_file.read()
    return preprompt

def setup_prompt(preprompt):
    template = preprompt + "\nuser message: {userprompt}" 

    prompt = PromptTemplate(
        input_variables=["userprompt"],
        template=template
    )
    return prompt

def setup_llm():
    llm = OpenAI(temperature=0.5)
    return llm

def setup_chain(prompt, llm):
    chain = prompt | llm | StrOutputParser()
    return chain

def get_response(userprompt):
    log("userprompt: {}".format(userprompt)) 
    preprompt = get_preprompt()
    log("preprompt: {}".format(preprompt)) 
    prompt = setup_prompt(preprompt) 
    log("prompt: {}".format(prompt)) 
    llm = setup_llm()
    log("llm: {}".format(llm)) 
    chain = setup_chain(prompt, llm)
    log("chain: {}".format(chain)) 
    response = chain.invoke({"userprompt": userprompt})
    log("response: {}".format(response)) 
    return response


from crewai.flow.flow import Flow, start, listen
import time
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()
class Llm_Call_Flow(Flow):

    @start()
    def generatecity(self):
        msg = [{"role": "user", "content": "return any famaous sity of pakistan"}]
        responce = completion(
            model="gemini/gemini-1.5-flash", 
            messages=msg
        )
        city = responce['choices'][0]['message']['content']
        print(f"return city {city}") 
        return city

    @listen(generatecity)
    def createFact(self, city_Name):
        msg = [{"role": "user", "content": f"give me fact short about that city {city_Name}"}]
        responce = completion(
            model="gemini/gemini-2.0-flash-exp", 
            messages=msg
        )
        fact = responce['choices'][0]['message']['content']
        print(f"return fact {fact}")
        self.state["fact"] = fact

    @listen(createFact)
    def checkFact(self):
        fact = self.state["fact"]
        with open("fact.md", "w") as file:
            file.write(fact)

        msg = [{"role": "user", "content": f"is this fact ( {fact} ) is correct"}]
        responce = completion(
            model="gemini/gemini-2.0-flash-exp", 
            messages=msg
        )
        fact = responce['choices'][0]['message']['content']
        print(f"fact result {fact}")


def StartLlmFlow():
    simple = Llm_Call_Flow()
    simple.kickoff()
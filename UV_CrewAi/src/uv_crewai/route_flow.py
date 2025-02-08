from crewai.flow.flow import Flow, start, listen, router
from pydantic import BaseModel
import random 

class City(BaseModel):
    city: str = ""

class RouteFlow(Flow[City]):
    
    @start()
    def greeting(self):
        print("Step 1... \n Heelo!")
    
    @router(greeting)
    def SelectCity(self):
        print("Step 2 select city")
        city = ["Karachi", "Lahore", "Islamabad"]
        select_city = random.choice(city)
        self.state.city = select_city
        if select_city == "Karachi":
            return "Karachi"
        elif select_city == "Lahore":
            return "Lahore"
        elif select_city == "Islamabad":
            return "Islamabad"
        
    @listen("Karachi")
    def KarachiMsg(self):
        print("Step 3... \n Karachi is the largest city of Pakistan.")

    @listen("Lahore")
    def LahoreMsg(self):
        print("Step 3... \n Lahore is the largest city of Pakistan.")

    @listen("Islamabad")
    def IslamabadMsg(self):
        print("Step 3... \n Islamabad is the largest city of Pakistan.")
    
def StartRouteFlow():
    simple = RouteFlow()
    data = simple.kickoff()
    print(data)

def PlotRouteFlow():
    simple = RouteFlow()
    simple.plot()

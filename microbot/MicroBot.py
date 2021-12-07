# MicroBot v1.0.0
# Author: Juan Carlos Juárez García
# B.S. in Digital Systems and Robotics Engineer

from . import search
from . import words
from . import words
import sys
import animation
import string
import pyttsx3

# Voice Engine

engine = pyttsx3.init()
voice = False

# Response: The answer coming from the user
# Answer: The answer coming from MicroBot
# Query: The question or demand coming from the user
# Question: The question or demand coming from MicroBot

# ------- MicroBot Transaction Object (MTO) -------- #

class MTO:
  value = ""
  status = 0

  def __init__(self,currValue,currStatus):
    self.value = currValue
    self.status = currStatus

# ----------- MicroBot Main Class ------------------ #

class MicroBot:

  valid_attr = {"Name" : "", "Symbol" : "", "Voice" : "", "ID" : "", "Type" : ""}

  greetVal = ""
  lookingWeb = ""

  def __init__(self,attr):
    global voice
    if(len(attr) != len(self.valid_attr)):
      if(("Voice" in attr) or (len(attr) != len(self.valid_attr)-1)):
        print("<!> Missing Attributes on Microbot Declaration.\n")
        sys.exit()
    for key in attr:
      if(type(attr[key]) != str or type(key) != str): 
        print("<!> All Attribute Values must be Strings.\n")
        sys.exit()
      if(attr[key] == "" or key == ""): 
        print("<!> Attributes must not be Empty.\n")
        sys.exit()
      if(not key in self.valid_attr): 
        print("<!> Attribute not Identified.\n")
        sys.exit()
      if(key == "Voice"):
        if(attr[key] != "Male" and attr[key] != "Female"):
          print("<!> Invalid Voice Attributes.\n")
          sys.exit()
        voice = True
        voices = engine.getProperty('voices')
        if(attr[key] == "Male"):
          engine.setProperty('voice', voices[1].id)
        else:
          engine.setProperty('voice', voices[0].id)
      self.valid_attr[key] = attr[key]
    # Default Initialization
    self.greetVal = "Hi! My name is " + self.valid_attr["Name"] + "!"
  
  def say(self, data):
    print(self.valid_attr["Symbol"] + " " + data + "\n")
    if(voice): 
      engine.say(data)
      engine.runAndWait()
      
  def name(self) -> str:
    return self.valid_attr["Name"]

  def id(self) -> str:
    return self.valid_attr["ID"]

  def type(self) -> str:
    return self.valid_attr["Type"]

  def endWord(self) -> str:
    return self.valid_attr["EndWord"]

  def greet(self):
    self.say(self.greetVal)

  def customGreet(self,data):
    self.greetVal = data

  def ask(self,currQuestion):
    currQuestion = str(currQuestion)
    self.say(currQuestion)
    res = input("🔸 ")
    print("")
    return res

  def searchUrl(self,currQuery) -> str:
    print("💬 " + self.valid_attr["Name"] + " is looking up in the web.\n")
    clock = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    wait_animation = animation.Wait(clock, color="cyan", speed=1)
    wait_animation.start()
    res = ""
    res += self.valid_attr["Name"] + " found these results:\n\n"
    res += search.searchUrl(currQuery)
    wait_animation.stop()
    print(res+"\n")

  def searchWeb(self,currQuery) -> str:
    print("💬 " + self.valid_attr["Name"] + " is looking up in the web.\n")
    clock = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    wait_animation = animation.Wait(clock, color="cyan", speed=1)
    wait_animation.start()
    res = search.searchWeb(currQuery)
    wait_animation.stop()
    print(self.valid_attr["Name"] + " found this:\n")
    print("💡 " + res + "\n")
    if(voice):
      engine.say(res)
      engine.runAndWait()

    

  def askEnd(self, currAnswer):
    currAnswer = str(currAnswer)
    if(currAnswer == self.valid_attr["EndWord"]):
      print("MicroBot says Goodbye! 👋")
      sys.exit()

  def askBool(self, question) -> bool:
    while(True):
      ans = self.ask(question)
      if(not self.askBoolMTO(ans).status): 
        self.say("Sorry, could you be more specific?")
      elif(self.askBoolMTO(ans).value):
        return True
      else:
        return False

  def askQuit(self, question) -> bool:
    while(True):
      ans = self.ask(question)
      if(not self.askBoolMTO(ans).status): 
        self.say("Sorry, could you be more specific?")
      elif(self.askBoolMTO(ans).value):
        end()
      else:
        break

  def askBoolMTO(self, currResponse):
    if(len(currResponse) <= 0): return MTO(False,0)
    if(currResponse.lower() in  words.wordBank["no"]): return MTO(False,1)
    if(currResponse.lower() in words.wordBank["yes"]): return MTO(True,1)
    myCurr = currResponse.split()
    for i in myCurr:
      i = i.lower()
      i = i.translate(str.maketrans('', '', string.punctuation))
      if(i in words.wordBank["no"]): return MTO(False,1)
      if(i in words.wordBank["yes"]): return MTO(True,1)
    return MTO(False,0)

    
  

# -------- Opening Line ------------- #

print("\n© Juan Carlos Juárez 2021 - MicroBot v1.0.0\n")

# -------- Built-In MicroBot Functions --------- #

def end():
  print("MicroBot says Goodbye! 👋\n")
  sys.exit()
    
# ------ System Functions ------ #


# Microbot
An Intelligent Bot Framework to build simple yet powerful Assistance Bots.

To Run it simply run this command inside your terminal:

```python
pip install microbotpkg
```

And then import Microbot as follows:

```python
import microbot as mb
```

Here is a Bot Program Example:

```python
import microbot as mb

myBot = mb.MicroBot({
    "Name" : "Futura",
    "Symbol" : "🌬️",
    "ID" : "1",
    "Type" : "Assistance Bot"
})

myBot.greet()

while(True):
    if(myBot.askBool("Do you want to search someting?")):
        myBot.searchWeb(myBot.ask("What you wanna search?"))
    myBot.askQuit("Would you like to leave?")
```


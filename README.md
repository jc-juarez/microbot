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

Here is Code Example:

```python
import microbot as mb

myBot = mb.MicroBot({
    "Name" : "Futura",
    "Symbol" : ":o",
    "ID" : "1",
    "Type" : "Assistance Bot"
})

myBot.greet()

while(True):
    question = myBot.ask("What you wanna search?")
    myBot.searchWeb(question)
    myBot.askQuit("Would you like to leave?")
```


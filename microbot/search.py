# Needed Python Packages:
#google, beautifulsoup4, googlesearch

import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup

def searchUrl(query) -> str:
  res = ""
  for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    res += "🔗 " + j + "\n"
  res = res.rstrip("\n")
  return res

def searchWeb(query, index=0):
    fallback = 'Sorry, I cannot think of a reply for that.'
    result = ''

    try:
        search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

        page = ""

        newQ = query.lower()

        found = False

        if("who" in newQ or "what" in newQ):
            for i in search_result_list: 
              currI = i.lower()
              if("wikipedia" in currI):
                found = True
                page = requests.get(i)
                break
            if(found == False): page = requests.get(search_result_list[index])
        else:
          page = requests.get(search_result_list[index])
        tree = html.fromstring(page.content)

        soup = BeautifulSoup(page.content, features="lxml")

        article_text = ''
        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0] + "." + first_sentence[1] + "."

        chars_without_whitespace = first_sentence.translate(
            { ord(c): None for c in string.whitespace }
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback

        return result
    except:
        if len(result) == 0: result = fallback
        return result


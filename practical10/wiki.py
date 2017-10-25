
import wikipedia

user_input = input("Enter a page name:\n")


try:
    page = wikipedia.page(user_input)
except wikipedia.exceptions.DisambiguationError as e:
    page = wikipedia.page(e.options[0])
print(page.title, "\n", page.summary, "\n", page.url)
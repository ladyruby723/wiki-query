from flask import Flask, render_template, request
import wikipedia
import os
app = Flask(__name__)

@app.route('/')
def index():
    terms = request.values.get('terms')
    article = None
    if terms:
        article = wikipedia.summary(terms)
        return render_template('index.html', article=article)
    else:
        return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# request user input for a general search topic for Wikipedia
# search_terms = input("What general topic do you want to search for on Wikipedia? Enter any keyword(s). ")

# request user input for a subtopic or more specific category in Wikipedia
# wikipedia.search returns an array/list of categories and topics
# search_choice = input("""\n What subtopic related to {} would you like to read about? 
# Enter one of the following options: \n \n {} \n""".format(search_terms, wikipedia.search(search_terms)))

# create a function which takes an article argument (search keywords) and returns the article summary for those keywords
# def print_article(article):
#     print(wikipedia.summary(article))

# call the function above, using the search_choice value to return the article summary for the user's keyword input
# print_article(search_choice)
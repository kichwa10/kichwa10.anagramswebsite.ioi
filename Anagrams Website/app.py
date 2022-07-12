from flask import Flask, render_template

app = Flask(__name__)

@app.route("/words/<string:word>")
def words(word):

     f = open('words.txt')

     word_list = f.read().splitlines()

     upper_case_word = word.upper() in word_list

     anagrams = []

     for i in word_list:
        if sorted(word) == sorted(i):
            anagrams.append(i)

     return render_template('words.html', upper_case_word=upper_case_word, anagrams=anagrams)
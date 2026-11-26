from flask import Flask, render_template
import random

app = Flask(__name__)

MEMES = [
    ("https://imgflip.com", "One Does Not Simply"),
    ("https://imgflip.com", "Aliens")
    ("https://imgflip.com", "Sleeping Shaq"),
    ("https://imgflip.com", "Community Fire Pizza"),
    ("https://imgflip.com", "Math Lady")
    ]

@app.route("/")
def index():
    meme_pic,subreddit = random.choice(MEMES)
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
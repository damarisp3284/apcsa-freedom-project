from flask import Flask, render_template
import random

app = Flask(__name__)

MEMES = [
    ("/static/cat.jpg", "Sleeping Cat"),
    ("/static/hamster.jpg", "Scared Hamster"),
    ("/static/lady.jpg", "Math Lady")
    ]

@app.route("/")
def index():
    meme_pic, subreddit = random.choice(MEMES)
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
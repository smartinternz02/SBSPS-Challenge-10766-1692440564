from flask import Flask, render_template

app = Flask(__name__)

# Route for the embedded story
@app.route('/')
def story():
    story_url = "https://thecadenceuniverse.blogspot.com/"
    return render_template('story.html', story_url=story_url)

if __name__ == '__main__':
    app.run(debug=True)

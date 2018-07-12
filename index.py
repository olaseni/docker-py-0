from flask import Flask, render_template

app = Flask(__name__)

# uses lorem picsum to get a random image
image_url = 'https://picsum.photos/400/400/?random' 

@app.route('/')
def index():
    return render_template('index.html', url=image_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

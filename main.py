from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/bro')
def bro():

    return render_template("layout-static.html")



if __name__ == "__main__":
    app.run(debug=True, port=5001)

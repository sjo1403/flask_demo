from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	user = {'username' : 'Shantel'}
	posts = [
        {
            'author': {'username': 'Brandon'},
            'body': 'This Burger King deal is great!'
        },
        {
            'author': {'username': 'Baron'},
            'body': 'Get me some food, NOW!'
        }

    ]

	return render_template('index.html', user=user, posts=posts)

if __name__ == "__main__":
	app.run(debug=True)
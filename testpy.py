from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
@app.route('/testpy', methods=['GET', 'POST'])

def test_py():
	return render_template("index.html", title="Radiocast | Home")
	
if __name__ == '__main__':
	app.run(debug = True)

from flask import Flask, render_template, jsonify, redirect

import json, pprint, csv


def locate(name, dic):
	for each in dic:
		if each["name"] == name:
			return each

app = Flask(__name__)

with open('data.json') as ball:
    FIGLIST = json.load(ball)
	
PRINTER = pprint.PrettyPrinter(indent = 3)

@app.route('/')
def index():
	with open("intro_blurb.txt") as ball:
		result = ball.read().replace('\n', '<br/>')
	return render_template('landing_page.html', FIGLIST = FIGLIST, text = result)

@app.route("/data")
def show_data():
	with open("cities.csv") as ball:
		result = list(list(chain) for chain in csv.reader(ball, delimiter=','))
	return render_template('data.html', FIGLIST = FIGLIST, head = result[0], body = result[1:])

@app.route("/comparison")
def compare():
	result = [FIGLIST[:int(len(FIGLIST)/2)], FIGLIST[int(len(FIGLIST)/2):]]
	return render_template('compare.html', FIGLIST = FIGLIST, cols = result)
	
@app.route("/plot/<ball>")
def show_plot(ball):
	result = locate(ball, FIGLIST)
	return render_template('figure.html', FIGLIST = FIGLIST, figure = result)
	

if __name__ == "__main__":
    app.run(debug=True)
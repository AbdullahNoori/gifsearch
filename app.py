from flask import Flask, render_template, request
import requests
import json

key = "QDH2SCT995MD"

lmt = 10

app = Flask(__name__)
# TODO: Render the 'index.html' template, passing the list of gifs as a
# named parameter called 'gifs'
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/get_gifs')
def get_gifs(): 
    # make a request based on what you put in the text box
    text_input = request.args.get("search")
    query_string = "https://api.tenor.com/v1/search?q={}&key={}&limit={}".format(text_input, key, lmt)
    r = requests.get(query_string)

    gifs = []
    if r. status_code == 200:
        r_json = r.json()
        result_json = r_json["results"]
        for result in result_json:
            gif_path = result["media"][0]["mediumgif"]["url"]
            gifs.append(gif_path)
    else:
        r_json = None
    return render_template("gifs.html", gifs=gifs)
        
if __name__ == "__main__":
    app.run(debug=True)
        
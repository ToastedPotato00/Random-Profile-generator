import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

# with open('output.txt', 'w') as f:
#     f.write(f"{title} {name} is living according to {timezone} timezone\n")
#     f.write(f"{timezone} have a {offset} hour offsets from UTC")
  
@app.route('/run-script', methods=['POST','GET'])
def run_script():
    info = requests.get("https://randomuser.me/api")

    name = info.json()["results"][0]["name"]["first"]
    title = info.json()["results"][0]["name"]["title"]
    timezone = info.json()["results"][0]["location"]["timezone"]["description"]
    offset = info.json()["results"][0]["location"]["timezone"]["offset"]
    line1 = (f"{title} {name} is living according to {timezone} timezone")
    line2 = (f"{timezone} have a {offset} hour offsets from UTC")
    # line3 = '<a href="/run-script">refresh</a>'
    line3 = """<button onclick="window.location.href = '/run-script';">Generate New Profile</button>"""
    result = f"{line1}\n{line2}\n{line3}".replace("\n", "<br>")
    return result 

if __name__ == '__main__':
    app.run(debug=True)


# see = open("output.txt", "r")

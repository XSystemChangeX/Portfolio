from flask import Flask
import urllib.request
import json

app = Flask('app')

@app.route('/')
def hello_world():

  return render_template("index.html")

@app.route('/About')
def About():
  return render_template("About.html")

@app.route('/Contact')
def Contact():
  return render_template("Contact.html")

@app.route('/Gallery')
def Gallery():
  return render_template("Gallery.html")

@app.route('/Services')
def Services():
  return render_template("Services.html")

@app.route('/Weather')
def weather():
  city='sudbury'
  key='953156af1d8912580a0dc0e5c43c3fe3'
  url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  temp_c = result["main"]["temp"]-273.15
  return render_template("Weather.html",temp_c=temp_c)

app.run(host='0.0.0.0', port=8080)




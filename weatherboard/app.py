import requests
from flask import Flask, render_template, request

api="ba318a8494d512f033ce688d0c07d75b"

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
    city = request.form['city']
    countrycode = request.form['country_code']
    data = get_weather_results(city, countrycode, api)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    temp_min = "{0:.2f}".format(data["main"]["temp_min"])
    temp_max = "{0:.2f}".format(data["main"]["temp_max"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    return render_template('results.html', location=location, temp=temp, temp_max=temp_max, 
                            temp_min=temp_min, weather=weather, feels_like=feels_like)

def get_weather_results(city_name, country_code, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}".format(city_name, country_code, api_key)
    r = requests.get(api_url)
    return r.json()

if __name__== '__main__':
    app.run()


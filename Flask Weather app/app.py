from flask import Flask, render_template, request, redirect, url_for, flash
import requests


API_KEY =  # You
app = Flask(__name__)
app.secret_key = "fknjksfnklsfjlsflkgsjljdl;jv;lsjd"

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']
        if city_name != "":

            url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={API_KEY}'
            response = requests.get(url).json()
            print(response)

            temp = response['main']['temp']
            weather = response['weather'][0]['description']
            min_temp = response['main']['temp_min']
            max_temp = response['main']['temp_max']
            icon = response['weather'][0]['icon']
            humidity = response['main']['humidity']
     
            print(temp,weather,min_temp,max_temp, icon, humidity)
            return render_template('index.html',temp=temp, weather=weather, min_temp=min_temp, max_temp=max_temp,icon=icon,humidity=humidity, city_name=city_name)
        else:
            flash("Please Enter the City name")
            return redirect(url_for('index'))

    else:
        return render_template('index.html')
        


if __name__ == "__main__":
    app.run(debug=True)

import requests
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuration variables
app.config['BASE_API_URL'] = 'http://api.weatherstack.com'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/zipcode', methods=['POST'])
def process_zipcode():
    zipcode = request.form['zipcode']
    
    if not zipcode:
        note = "Please enter a zip code."
        return render_template('index.html', note=note)

    # Make API call with credentials and zipcode
    access_key = os.getenv('ACCESS_KEY')
    base_url = app.config['BASE_API_URL']
    params = {'access_key': access_key,
              'query': zipcode}
    response = requests.get(f'{base_url}/current', params=params)
    
    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        
        # Location data
        current_location = data['location']
        city = current_location['name']
        state = current_location['region']
        country = current_location['country']
        location = f'{city}, {state}, {country}'

        # Current weather data 
        current_weateher = data['current']

        condition = ', '.join(current_weateher['weather_descriptions'])
        temperature = current_weateher['temperature']

        precip = current_weateher['precip']
        uv_index = current_weateher['uv_index']
        wind_speed = current_weateher['wind_speed']


        # Questions
        questions = ['Should I go outside?', 
                     'Should I wear sunscreen?',
                     'Can I fly my kite?']

        answer1 = 'No, it\'s raining' if precip else 'Yes, there\'s no rain, you can go outside.'

        answer2 = f'Please use sunscreen before going out uv index is {uv_index}' \
            if uv_index > 3 else f'You can go outside w/o sunscreen uv index is safe'

        answer3 = f'Yes you can fly your kite, wind speed is {wind_speed} and no rain.' \
            if wind_speed > 15 and precip == 0 else 'No, the weather is not great to fly your kite.'

        answers = answer1, answer2, answer3
        qa_data = [{'question': q, 'answer': a} for q, a in zip(questions, answers)]

        return render_template('answers.html', 
                               qa_data=qa_data, 
                               location=location,
                               temperature=temperature, 
                               condition=condition)
    else:
        return 'Error fetching weather data from API'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Weather App</title></head>
<body style="font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px;">
    <h1>🌤️ Weather Forecast</h1>
    <form method="POST">
        <input type="text" name="city" placeholder="Enter city name" required 
               style="padding: 10px; width: 70%;">
        <button type="submit" style="padding: 10px 20px;">Get Weather</button>
    </form>
    {% if weather %}
    <div style="margin-top: 30px; padding: 20px; background: #f0f0f0; border-radius: 8px;">
        <h2>{{ weather.city }}, {{ weather.country }}</h2>
        <p style="font-size: 48px; margin: 10px 0;">{{ weather.temp }}°C</p>
        <p>{{ weather.desc }}</p>
        <p>Humidity: {{ weather.humidity }}% | Wind: {{ weather.wind }} m/s</p>
    </div>
    {% elif error %}
    <p style="color: red; margin-top: 20px;">{{ error }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = error = None
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = '8ca09708512cd9f5a47ad19a2cea8102'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            r = requests.get(url, timeout=10)
            data = r.json()
            
            print(f"Status Code: {r.status_code}")  # Debug print
            print(f"Response: {data}")  # Debug print
            
            if r.status_code == 200:
                weather = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temp': round(data['main']['temp']),
                    'desc': data['weather'][0]['description'].capitalize(),
                    'humidity': data['main']['humidity'],
                    'wind': data['wind']['speed']
                }
            elif r.status_code == 401:
                error = 'Invalid API key. Please check your key or wait for activation (can take up to 2 hours).'
            elif r.status_code == 404:
                error = f'City "{city}" not found. Try with country code (e.g., "London,UK")'
            else:
                error = f'Error: {data.get("message", "Unknown error")}'
        except requests.exceptions.Timeout:
            error = 'Request timed out. Please try again.'
        except Exception as e:
            error = f'Error: {str(e)}'
    
    return render_template_string(HTML, weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)
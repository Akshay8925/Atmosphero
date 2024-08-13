from  flask import Blueprint, render_template, request
from .weather import get_weather

bp = Blueprint('main',__name__)
@bp.route('/')
def index():
    city = request.args.get('City')
    country = request.args.get('Country')

    if city and country:
        weather_data = get_weather(city, country)
        if weather_data:

            return render_template('index.html', weather = weather_data)
        else:
            return render_template('index.html',error = "city not found")
    else:
        return render_template('index.html')
from flask import Blueprint, render_template
import sys, os

bp = Blueprint("weather", __name__, url_prefix="/weather")

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from Weather_project.main import GetWeather


@bp.route("/")
def index():
    info = GetWeather("서울특별시", "관악구", "대학동")
    return render_template("weather/weather.html", info=info)

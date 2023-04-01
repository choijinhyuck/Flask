from flask import Blueprint, render_template

bp = Blueprint("weather", __name__, url_prefix="/weather")


@bp.route("/")
def index():
    info = "신성동 날씨는"
    return render_template("weather/weather.html", info=info)

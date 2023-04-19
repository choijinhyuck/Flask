from flask import Blueprint, render_template, request
import sys, os

bp = Blueprint("weather", __name__, url_prefix="/weather")

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from Weather_project.main import GetWeather


@bp.route("")
def index():
    site = request.args.to_dict()
    if "si" in site:
        try:
            info = GetWeather(site["si"], site["gun"], site["dong"])
            return render_template(
                "weather/weather.html", info=info, site=[site["si"], site["gun"], site["dong"]]
            )
        except Exception as e:
            print(e)
            # return render_template(
            #     "weather/weather_index.html", msg="오류 발생. 현재 날씨 정보를 찾을 수가 없어요. 다시 선택해주세요."
        
    else:
        return render_template("weather/weather_index.html", msg="주소를 선택해주세요.")

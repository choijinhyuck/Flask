from flask import Blueprint, render_template, request, send_file, redirect, current_app, url_for
import os, sys, traceback

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from PDF_editor import PDF_rotation

bp = Blueprint("pdf", __name__, url_prefix="/pdf")


@bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        return render_template("pdf/pdf_index.html")

    try:
        angle = request.form.get("angle", type=int)
        file = request.files["pdf_file"]
        processed_name = file.filename
        processed_name = processed_name[:-4] + f"_rotated.pdf"
        filepath = os.path.join(os.getcwd(), "pdf_files", "temp.pdf")
        file.save(filepath)
        PDF_rotation.rotate(filepath, filepath, angle)
        print(processed_name)
        return send_file(filepath, download_name=processed_name, as_attachment=False)
        # return send_file(filepath, download_name=processed_name, as_attachment=True) # 바로 다운로드 화면
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + "\n" + str(trace_back)
        current_app.logger.error("ERROR \n %s", message)
        return render_template("pdf/pdf_index.html", msg="오류 발생! 올바른 파일 형식을 업로드해주세요.")

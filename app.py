from main import XssChecker
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": {"*"}}})


@app.route("/")
def home():
    return "Welcome to our XSS tool"


@app.route("/api/scan_website", methods=["POST", "GET"])
def xss_Scanner():
    if request.method == "POST":
        contents = request.get_json()
        webPageUrl = contents['url']
        webFrontedCode = XssChecker.get_html(webPageUrl)
        response = XssChecker.ScanningForxss(html=webFrontedCode)
        jsonify({"scan_result": response})

    # raid 0-increases the data for loss


if __name__ == "__main__":
    app.run(debug=True)

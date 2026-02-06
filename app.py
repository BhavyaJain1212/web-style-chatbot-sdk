from flask import Flask, render_template, request, jsonify
from web_scrape import save_file, extract_html_and_css


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/fetch-website-code", methods=["POST"])
def fetch_website_code():
    data = request.get_json()
    
    site_path = data.get("web_url")
    print(site_path)

    extract_html_and_css(site_path)

    return jsonify({
        "recieved": "yes"
    })

if __name__ == '__main__':
    app.run(debug=True)
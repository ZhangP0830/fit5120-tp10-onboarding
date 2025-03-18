from flask import Flask, request, jsonify
import requests
import pymysql
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'sunscreen'

pymysql.install_as_MySQLdb()


def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )


API_KEY = "44869d147a17986a38fcc08b77a43e1a"
OW_URL = "https://api.openweathermap.org/data/3.0/onecall?"


@app.route('/')
def home():
    return jsonify({"message": "欢迎使用 Flask API！"})


@app.route('/api/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM app_user")
        users = cursor.fetchall()
    connection.close()
    return jsonify(users)


@app.route('/api/clothing', methods=['GET'])
def get_clothing():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM clothing")
        clothing = cursor.fetchall()
    connection.close()
    return jsonify(clothing)


@app.route('/api/recommendation', methods=['GET'])
def clothing_recommendation():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM clothing_recommendation")
        recommended_clothing = cursor.fetchall()
    connection.close()
    return jsonify(recommended_clothing)


@app.route('/api/forecast', methods=['GET'])
def forecast_trend():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM forecast_trend")
        forecast = cursor.fetchall()
    connection.close()
    return jsonify(forecast)


@app.route('/api/incidence', methods=['GET'])
def incidence():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM incidence")
        incident = cursor.fetchall()
    connection.close()
    return jsonify(incident)


@app.route('/api/location', methods=['GET'])
def get_locations():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM location")
        location = cursor.fetchall()
    connection.close()
    return jsonify(location)


@app.route('/api/mortality', methods=['GET'])
def get_mortality():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM mortality")
        mortality = cursor.fetchall()
    connection.close()
    return jsonify(mortality)


@app.route('/api/remainder', methods=['GET'])
def get_remainders():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM reminder")
        remainders = cursor.fetchall()
    connection.close()
    return jsonify(remainders)


@app.route('/api/skintone', methods=['GET'])
def get_skintone():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM skintone")
        skintone = cursor.fetchall()
    connection.close()
    return jsonify(skintone)


@app.route('/api/sunscreenrec', methods=['GET'])
def get_sun_recommendation():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sunscreen_recommendation")
        sunscreen_recommendation = cursor.fetchall()
    connection.close()
    return jsonify(sunscreen_recommendation)


@app.route('/api/user/remainder', methods=['GET'])
def user_remainder():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user_reminder")
        remainder = cursor.fetchall()
    connection.close()
    return jsonify(remainder)


def get_uv_index(api_key, lat, lon):
    url = (
        "https://api.openweathermap.org/data/3.0/onecall"
        f"?lat={lat}&lon={lon}&appid={api_key}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return data.get("current", {}).get("uvi")


@app.route("/api/uv-index", methods=["GET"])
def get_uv_index():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({"error": "Missing latitude or longitude"}), 400
    try:
        response = requests.get("https://api.openweathermap.org/data/3.0/onecall"
                                f"?lat={lat}&lon={lon}&appid={API_KEY}")
        data = response.json().get("current", {}).get("uvi")
        return jsonify({"uv_index": (data)})
    except Exception as e:
        print(f"Error: {e}")


@app.route("/uv-index", methods=["GET"])
def uv_index():
    location = request.get_json()
    lat = location.get('lat')
    lon = location.get('lon')

    if lat is None or lon is None:
        return jsonify({"error": "Missing latitude or longitude parameters"}), 400

    uv_val = get_uv_index(API_KEY, lat, lon)
    if uv_val is not None:
        print({"UV Index": uv_val})
        return jsonify({"UV Index": uv_val})
    else:
        return jsonify({"error": "Failed to retrieve UV index"}), 500


@app.route("/api/select_location", methods=["GET"])
@cross_origin()
def get_location():
    try:
        suburb = request.args.get("suburb")

        if not suburb:
            return jsonify({"error": "Missing suburb parameter"}), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({"error": "Database connection failed"}), 500

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT location_long, location_lat FROM location WHERE location_suburb = %s",
                (suburb,)
            )
            result = cursor.fetchone()
            print(f"Database query result: {result}", flush=True)

        connection.close()

        if result:
            return jsonify({"lon": result["location_long"], "lat": result["location_lat"]})
        else:
            return jsonify({"error": "Location not found"}), 404

    except Exception as e:
        print(f"Unexpected error: {e}", flush=True)
        return jsonify({"error": "Internal Server Error"}), 500


# Api to get the skin cancer incidence data
# P
@app.route('/api/skin_cancer/incidence_rate', methods=['GET'])
@cross_origin()
def get_skin_cancer_incidence():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT year, sex, incidence_rate FROM skin_cancer_data ORDER BY year;")
        data = cursor.fetchall()
    connection.close()
    return jsonify(data)


# Api to get the skin cancer mortality data
# P
@app.route('/api/skin_cancer/mortality_rate', methods=['GET'])
@cross_origin()
def get_skin_cancer_mortality():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT year, sex, mortality_rate FROM skin_cancer_data ORDER BY year;")
        data = cursor.fetchall()
    connection.close()
    return jsonify(data)


@app.route('/api/heat_forecast', methods=['GET'])
@cross_origin()
def get_heat_forecast():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return jsonify({"error": "Missing latitude or longitude"}), 400

    try:
        response = requests.get("https://api.openweathermap.org/data/3.0/onecall"
                                f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric")
        data = response.json()
        print(data)
        forecast = [
            {
                "time": hour["dt"],
                "temperature": hour["temp"],
                "weather": hour["weather"][0]["main"] if "weather" in hour and hour["weather"] else "Unknown",
                "description": hour["weather"][0]["description"] if "weather" in hour and hour[
                    "weather"] else "No description"
            }
            for hour in data["hourly"][:6]
        ]
        print(forecast)
        return jsonify(forecast)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

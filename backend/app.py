from flask import Flask, request, jsonify
import requests
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'admin123'  # Your MySQL password
app.config['MYSQL_DB'] = 'sunscreen'
API_KEY = "44869d147a17986a38fcc08b77a43e1a"
mysql = MySQL(app)

# Example: Get users from the database
@app.route('/api/users', methods=['GET'])
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM app_user")
    users = cursor.fetchall()
    cursor.close()
    return jsonify(users)

@app.route('/api/clothing', methods=['GET'])
def get_clothing():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM clothing")
    clothing = cursor.fetchall()
    cursor.close()
    return jsonify(clothing)

@app.route('/api/recommendation', methods=['GET'])
def clothing_recommendation():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM clothing_recommendation")
    recommended_clothing = cursor.fetchall()
    cursor.close()
    return jsonify(recommended_clothing)

@app.route('/api/forcast', methods=['GET'])
def forcast_trend():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM forecast_trend")
    forcast = cursor.fetchall()
    cursor.close()
    return jsonify(forcast)

@app.route('/api/incidence', methods=['GET'])
def incidence():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM incidence")
    incident = cursor.fetchall()
    cursor.close()
    return jsonify(incident)

@app.route('/api/location', methods=['GET'])
def get_locations():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM location")
    location = cursor.fetchall()
    cursor.close()
    return jsonify(location)

@app.route('/api/mortality', methods=['GET'])
def get_mortality():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM mortality")
    mortality = cursor.fetchall()
    cursor.close()
    return jsonify(mortality)

@app.route('/api/remainder', methods=['GET'])
def get_remainders():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM reminder")
    mortality = cursor.fetchall()
    cursor.close()
    return jsonify(mortality)

@app.route('/api/skintone', methods=['GET'])
def get_skintone():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM skintone")
    skintone = cursor.fetchall()
    cursor.close()
    return jsonify(skintone)

@app.route('/api/sunscreenrec', methods=['GET'])
def get_sun_recommendation():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM sunscreen_recommendation")
    sunscreen_recommendation = cursor.fetchall()
    cursor.close()
    return jsonify(sunscreen_recommendation)

app.route('api/user/remainder', methods=['GET'])
def user_remainder():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user_reminder")
    remainder = cursor.fetchall()
    cursor.close()
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



@app.route("/uv-index", methods=["GET"])
def uv_index():
    location = request.get_json()
    lat = location['lat']
    lon = location['lon']


    if lat is None or lon is None:
        return jsonify({"error": "Missing latitude or longitude parameters"}), 400

    uv_val = get_uv_index(API_KEY, lat, lon)
    if uv_val is not None:
        return jsonify({"UV Index": uv_val})
    else:
        return jsonify({"error": "Failed to retrieve UV index"}), 500

@app.route("/select_location", methods=["GET"])
def get_location():
    cursor = mysql.connection.cursor()
    suburb = "Clayton South"
    cursor.execute("SELECT location_long,location_lat FROM location WHERE location_suburb = %s", (suburb,))
    cordinates = cursor.fetchall()
    print(cordinates[0])
    #print(cordinates[1])
    cursor.close()




if __name__ == '__main__':
    app.run(debug=True)
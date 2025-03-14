from flask import Flask, request, jsonify
import requests
import pymysql
from flask_cors import CORS

# 初始化 Flask 应用
app = Flask(__name__)
CORS(app)

# 数据库配置
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # 你的 MySQL 用户名
app.config['MYSQL_PASSWORD'] = 'admin123'  # 你的 MySQL 密码
app.config['MYSQL_DB'] = 'sunscreen'

# 让 pymysql 兼容 MySQLdb
pymysql.install_as_MySQLdb()

# 获取 MySQL 连接
def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor  # 让查询返回 JSON 友好的字典
    )


# OpenWeather API Key
API_KEY = "44869d147a17986a38fcc08b77a43e1a"

@app.route('/')
def home():
    return jsonify({"message": "欢迎使用 Flask API！"})

# 获取用户数据
@app.route('/api/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM app_user")
        users = cursor.fetchall()
    connection.close()
    return jsonify(users)


# 获取衣物数据
@app.route('/api/clothing', methods=['GET'])
def get_clothing():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM clothing")
        clothing = cursor.fetchall()
    connection.close()
    return jsonify(clothing)


# 获取服装推荐
@app.route('/api/recommendation', methods=['GET'])
def clothing_recommendation():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM clothing_recommendation")
        recommended_clothing = cursor.fetchall()
    connection.close()
    return jsonify(recommended_clothing)


# 获取天气预测数据
@app.route('/api/forecast', methods=['GET'])
def forecast_trend():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM forecast_trend")
        forecast = cursor.fetchall()
    connection.close()
    return jsonify(forecast)


# 获取疾病发病率数据
@app.route('/api/incidence', methods=['GET'])
def incidence():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM incidence")
        incident = cursor.fetchall()
    connection.close()
    return jsonify(incident)


# 获取位置数据
@app.route('/api/location', methods=['GET'])
def get_locations():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM location")
        location = cursor.fetchall()
    connection.close()
    return jsonify(location)


# 获取死亡率数据
@app.route('/api/mortality', methods=['GET'])
def get_mortality():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM mortality")
        mortality = cursor.fetchall()
    connection.close()
    return jsonify(mortality)


# 获取提醒数据
@app.route('/api/remainder', methods=['GET'])
def get_remainders():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM reminder")
        remainders = cursor.fetchall()
    connection.close()
    return jsonify(remainders)


# 获取肤色数据
@app.route('/api/skintone', methods=['GET'])
def get_skintone():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM skintone")
        skintone = cursor.fetchall()
    connection.close()
    return jsonify(skintone)


# 获取防晒推荐数据
@app.route('/api/sunscreenrec', methods=['GET'])
def get_sun_recommendation():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sunscreen_recommendation")
        sunscreen_recommendation = cursor.fetchall()
    connection.close()
    return jsonify(sunscreen_recommendation)


# 获取用户提醒数据
@app.route('/api/user/remainder', methods=['GET'])
def user_remainder():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user_reminder")
        remainder = cursor.fetchall()
    connection.close()
    return jsonify(remainder)


# 获取 UV 指数
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
    lat = location.get('lat')
    lon = location.get('lon')

    if lat is None or lon is None:
        return jsonify({"error": "Missing latitude or longitude parameters"}), 400

    uv_val = get_uv_index(API_KEY, lat, lon)
    if uv_val is not None:
        return jsonify({"UV Index": uv_val})
    else:
        return jsonify({"error": "Failed to retrieve UV index"}), 500


# 查询特定位置的坐标
@app.route("/select_location", methods=["GET"])
def get_location():
    connection = get_db_connection()
    suburb = "Clayton South"
    with connection.cursor() as cursor:
        cursor.execute("SELECT location_long, location_lat FROM location WHERE location_suburb = %s", (suburb,))
        coordinates = cursor.fetchone()
    connection.close()

    if coordinates:
        return jsonify({"longitude": coordinates['location_long'], "latitude": coordinates['location_lat']})
    else:
        return jsonify({"error": "Location not found"}), 404

# Api to get the skin cancer incidence data
# P
@app.route('/api/skin_cancer/incidence_rate', methods=['GET'])
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
def get_skin_cancer_():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT year, sex, mortality_rate FROM skin_cancer_data ORDER BY year;")
        data = cursor.fetchall()
    connection.close()
    return jsonify(data)

# 启动 Flask 服务器
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

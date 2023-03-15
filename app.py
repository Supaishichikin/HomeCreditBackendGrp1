from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DB')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
mysql = MySQL(app)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api')
def hello_world():  # put application's code here
    cur = mysql.connection.cursor()
    cur.execute('SELECT DISTINCT STATUS FROM `bureau_balance`')
    result = cur.fetchall()
    cur.close()
    return jsonify(result)


if __name__ == '__main__':
    app.run()

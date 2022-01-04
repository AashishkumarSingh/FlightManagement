from flask import Flask
from flask_mysqldb import MySQL
from flask import request
import MySQLdb.cursors

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flightdata'
mysql = MySQL(app)

@app.route('/flights', methods=['POST']) 
def getFlights():
    msg=''
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        flight = request.args['flightName']
        cursor.execute("insert into table flight values(flight,23)")
        mysql.connection.commit()
        msg = 'Success:'
    else:
        msg ='error:'

@app.route('/flight', methods=['GET', 'HEAD', 'PATCh', 'DELETE'])
def getFlight():
    msg =''
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'GET':
        flight = request.args['flightName']
        cursor.execute("select flightName  from flight WHERE flightName = flight")
        data=cursor.fetchall()
        return data
    elif request.method == 'HEAD':
        flight = request.args['flightName']
        cursor.execute("select flightName  from flight WHERE flightName = flight")
        data = cursor.fetchall()
        if data:
            msg = 'flight exist:'
        else:
            msg = 'flight not exist'
    elif request.method == 'PATCH':
        flightnew  = request.args['newFlight']
        flightold = request.args['oldFlight']
        flightno = request.args['flightNo']
        cursor.execute("update flight SET flightold = flightnew WHERE flightNo = flightno")
        mysql.connection.commit()
        msq= 'flight data updated'
    elif request.method == 'DELETE':
        flightno = request.args['flightNo']
        cursor.execute("Delete from flight WHERE flightNo = flightno")
        msg = 'flight data deleted:'
    else:
        msg = 'no data received:'




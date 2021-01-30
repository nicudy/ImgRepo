#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from mysql.connector import (connection)
from datetime import datetime
import config
import os

app = Flask(__name__)
CORS(app)

@app.route('/apiUpload/', methods=['POST'])
def api_upload():
	try:
		cnx = connection.MySQLConnection(user=config.username, password=config.password, host='127.0.0.1', database='imageRepository')
	except:
		print("Something is wrong with username or password")

	cursor = cnx.cursor(dictionary=True)
	try:
		cursor.execute("select count(*) from images;")
	except:
		print("Something is wrong with your query")

	numPics = str(cursor.fetchone().get('count(*)'))
	path = os.getcwd() + '/ImageRepo/' + numPics
	request.files['file'].save(path)
	try:
		cursor.execute(("INSERT INTO images" "(number, date)" "VALUES(%s,%s)"), (numPics, datetime.now()))
	except:
		print("Something is wrong with your query")
	cnx.commit()
	cnx.close()

	return "uploaded"
	

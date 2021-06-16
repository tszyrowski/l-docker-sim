from flask import Flask
import mysql.connector

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello world from dock compose"

if __name__ == "__main__":
    connection = mysql.connector.connect(
        user="user", password="pass", host="host", database="example"
    )
    cursor = connection.cursor()
    server.run()
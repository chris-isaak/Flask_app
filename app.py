from flask import Flask, json, request
import requests
import os.path
import logging



app = Flask(__name__)

# Logging calls to endpoint
logging.basicConfig(filename='flask_connection.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p %z')



@app.route('/manage_File', methods=['POST'])
def manage_file():
    # Pop out the JSON
    data = request.json
    # First check that the JSON is valid, return a helpful error
    if "action" not in data:
        return {'success':False,'message':'invalid json parameters'}

    # Check for proper actions and act
    if data["action"].lower() == "download":
        file = requests.get('https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt')
        with open("sample-txt-file.txt","w") as f:
            f.write(file.text)
        return {'success':True,'message':'File has been stored locally'}

    # Ensure that the global storage has content
    if os.path.exists("sample-txt-file.txt") == False:
       return {'success':False,'message':'please download the contents first to read them'}

    if data["action"].lower() == "read":
        with open("sample-txt-file.txt","r") as f:
            return f.read()

    return {'success':False,'message':'There are only 2 options and you have given neither! Why not try download or read'}

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 

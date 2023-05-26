from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask(__name__)

import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        # Save or process the uploaded file
        file.save('x.jpg')

        image_path="x.jpg"

        script_path = 'compress.py'
        output_path="compress.jpg"
        subprocess.run(['python', script_path, image_path, output_path])
        print( "Compression Successfull")

        quantum_path= 'qrng.py'
        pathToCompressedImage = "compress.jpg"
        pathToOutputFile = "file.txt"

        subprocess.run(['python3',quantum_path,pathToCompressedImage,pathToOutputFile])
        print("Key generation successfull")


        with open("file.txt", 'r') as file:
            key = file.read()

        print(key)
        response = {
            'status': 'success',
            'key': key
        }

        # print('ssssssssssss',response)
        return (response)
    # Check the subprocess result and handle accordingly
    else:
        return 'No file received'


# @app.route('/getKey')
# def getKey():
#     with open("file.txt", 'r') as file:
#         key = file.read()

#     print(key)
#     response = {
#         'status': 'success',
#         'key': key
#     }

#         # print('ssssssssssss',response)
#     return (response) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
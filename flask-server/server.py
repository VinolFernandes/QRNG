from flask import Flask, request
import subprocess

app = Flask(__name__)


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


        return "completed process"
    # Check the subprocess result and handle accordingly
    else:
        return 'No file received'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
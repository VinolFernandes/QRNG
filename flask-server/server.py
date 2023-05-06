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
        
        return "Compression Successfull"
    # Check the subprocess result and handle accordingly
    else:
        return 'No file received'



#API route
@app.route("/compress")
def compress(image_path,oytput_image):
    # Run the Python script as a subprocess
    script_path = 'compress.py'
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    
    # Check the subprocess result and handle accordingly
    if result.returncode == 0:
        output = result.stdout
        return f'Success: {output}'
    else:
        error = result.stderr
        return f'Error: {error}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
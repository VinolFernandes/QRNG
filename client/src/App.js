import React, { useState, useRef } from 'react';
import './index.css';
import Webcam from 'react-webcam';

const FileUploadForm = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (file) {
      const formData = new FormData();
      formData.append('file', file);
      
      try {
         await fetch('http://localhost:5000/upload', {
          method: 'POST',
          body: formData,
        })
        .then(response => response.json())
        .then(data => {
          if(data.status === 'success') {
            const key = data.key;

            console.log("Key", key)

            const keyElement = document.getElementById('keyValue') 
            keyElement.textContent = key

            const elementButton = document.getElementById('startProcess')
            elementButton.textContent = "Process Completed"
          }
          else {
            console.error("key generation failed");
          }
        })
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };



  const webcamRef = useRef(null);
  const [capturedImage, setCapturedImage] = useState(null);

  const captureImage = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    setCapturedImage(imageSrc);

    // Automatically select the captured image as the file input
    const fileInput = document.getElementById('imgFile');
    const capturedFile = dataURLtoFile(imageSrc, 'captured_image.jpg');
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(capturedFile);
    fileInput.files = dataTransfer.files;
    setFile(capturedFile);
  };

  const downloadImage = () => {
    const link = document.createElement('a');
    link.href = capturedImage;
    link.download = 'captured_image.jpg';
    link.click(); 
  };

  const startProcess = () => {
    const elementButton = document.getElementById('startProcess')
    elementButton.textContent = "Processing..."
  }

  // Helper function to convert data URL to File object(ie. Screenshot from webcam to file)
  const dataURLtoFile = (dataUrl, filename) => {
    if (!dataUrl) {
      return null;
    }
    const arr = dataUrl.split(',');
    const mime = arr[0].match(/:(.*?);/)[1];
    const bstr = atob(arr[1]);
    let n = bstr.length;
    const u8arr = new Uint8Array(n);
    while (n--) {
      u8arr[n] = bstr.charCodeAt(n);
    }
    return new File([u8arr], filename, { type: mime });
  };
  
  if(capturedImage || file){
    return (
      <div>
        <h1 className="Qrng">Quantum Random Key Stream Generator</h1>
        <div className="container contact-form">
          <div className="contact-image">
            <img src="quantum.png" alt="rocket_contact" />
          </div>
          <form onSubmit={handleSubmit} className="contact-form">
            <h3>Choose an image as a seed value</h3>
            <div className="row">
              <input type="file" id="imgFile" onChange={handleFileChange} className="form-control" />
              <div>
                {/* <div>
                  <button className="capture" onClick={captureImage}>Capture Image</button>
                </div> */}
                {capturedImage && (
                  <div>
                    <h2>Captured Image:</h2>
                    <img id='captredImage' src={capturedImage} alt="Captured" />
                  </div>
                )}
              </div>
              <button type="submit" className="btnContact" id="startProcess" onClick={startProcess}>Start Process</button>
            </div>
          </form>
          <div>
            <h2 className='enc'>The encryption key is:</h2>
            <div className='outputKey' id='keyValue'>
          </div>
          </div>
        </div>
      </div>  
    )
  }
  else {
    return (
      <div>
        <h1 className="Qrng">Quantum Random Key Stream Generator</h1>
        <div className="container contact-form">
          <div className="contact-image">
            <img src="quantum.png" alt="rocket_contact" />
          </div>
          <form onSubmit={handleSubmit} className="contact-form">
            <h3>Choose an image as a seed value</h3>
            <div className="row">
              <input type="file" id="imgFile" onChange={handleFileChange} className="form-control" />
              <div>
                <button className='btmCapture' onClick={captureImage}>Capture Image</button>
                {capturedImage && (
                  <button onClick={downloadImage}>Save Image</button>
                )}
              </div>
              <Webcam audio={false} ref={webcamRef} screenshotFormat="image/jpeg" />
            </div>
          </form>
          <div>
            <h2 className='enc'>The encryption key is:</h2>
            <div className='outputKey' id='keyValue'>
          </div>
          </div>
        </div>
      </div>  
    );
  }
};

export default FileUploadForm
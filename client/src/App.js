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
        const response = await fetch('http://localhost:5000/upload', {
          method: 'POST',
          body: formData,
        });

        console.log(response);

        // Handle the response from the backend
        if (response.ok) {
          console.log('File uploaded successfully');
        } else {
          console.error('Error uploading file');
        }
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

    // Automatically select the captured image in the file input
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

  // Helper function to convert data URL to File object
  const dataURLtoFile = (dataUrl, filename) => {
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
        <div className="container contact-form">
          <div className="contact-image">
            <img src="quantum.png" alt="rocket_contact" />
          </div>
          <form onSubmit={handleSubmit} className="contact-form">
            <h3>Choose an image as a seed value</h3>
            <div className="row">
              <input type="file" id="imgFile" onChange={handleFileChange} className="form-control" />
              <div>
                <div>
                  <button onClick={captureImage}>Capture Image</button>
                </div>
                {capturedImage && (
                  <div>
                    <h2>Captured Image:</h2>
                    <img src={capturedImage} alt="Captured" />
                  </div>
                )}
              </div>
              <button type="submit" className="btnContact">Start Process</button>
            </div>
          </form>
        </div>
      </div>  
    )
  }
  else {
    return (
      <div>
        <div className="container contact-form">
          <div className="contact-image">
            <img src="quantum.png" alt="rocket_contact" />
          </div>
          <form onSubmit={handleSubmit} className="contact-form">
            <h3>Choose an image as a seed value</h3>
            <div className="row">
              <input type="file" id="imgFile" onChange={handleFileChange} className="form-control" />
              <div>
                <Webcam audio={false} ref={webcamRef} screenshotFormat="image/jpeg" />
                <div>
                  <button onClick={captureImage}>Capture Image</button>
                  {capturedImage && (
                    <button onClick={downloadImage}>Save Image</button>
                  )}
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>  
    );
  }
  
};

export default FileUploadForm

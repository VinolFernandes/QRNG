import React, { useState } from 'react';
import './index.css'

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

        console.log(response)

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

  return (
//     <div class="container contact-form">
//         <div class="contact-image">
//             <img src="quantum.png" alt="rocket_contact"/>
//         </div>
//         <form method="post" id="imageForm">
//             <h3>Choose an image as a seed value</h3>
//            <div class="row">
//                 <div class="col-md-6" style="margin:auto">
//                     <div class="form-group">
//                         <input type="file" name="imgFile" id="imgFile" class="form-control" placeholder="" value="" />
//                     </div>
//                     <div class="form-group">
//                         <input type="submit" name="btnSubmit" class="btnContact" value="Start Process" />
//                     </div>
//                 </div>
//             </div>
//         </form>
// </div>
    <div >
      <div class="container contact-form">
        <div class="contact-image">
            <img src="quantum.png" alt="rocket_contact"/>
        </div>
        <form onSubmit={handleSubmit} class="contact-form">
        <h3>Choose an image as a seed value</h3>
        <div class="row">
        <input type="file" onChange={handleFileChange} class="form-control"/>
          <button type="submit" class="btnContact">Start Process</button>
        </div>
      </form>
      </div>
  </div>  
  );
};

export default FileUploadForm;

import React from "react";
import axios, { post } from 'axios';
class uploader extends React.Component {

  constructor(props) {
    super(props);
    this.state ={
     
    }
    this.fileUpload = this.fileUpload.bind(this);
  
  }
  
  fileUpload(){
    const url ='http://localhost:5000/uploader';
    const formData = new FormData(this.form);
    return  post(url, formData);
  }
  render() {
    return (
        <div>
        <h1>New File Upload</h1>
        <form  ref={el => (this.form = el)}>
        <input type="file" name="file"/>
        <input type="text" name="text"/>    
        </form>
        <button onClick={() => this.fileUpload()}>Upload</button>
        </div>
   );
  }
}

export default uploader;
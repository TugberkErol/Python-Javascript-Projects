import React from "react";
import axios, { post } from 'axios';
import ReactDOM from 'react-dom';
class download_File extends React.Component {

  constructor(props) {
    super(props);
    this.state ={
     
    }
    this.fileDownload = this.fileDownload.bind(this);
  
  }
  
  fileDownload(){
    const url ='http://localhost:5000/download_File';
    const formData = new FormData(this.form);
    return  post(url, formData);
  }
  render() {
    return (
        <div>
        <h1>New File Download</h1>
        <form  ref={el => (this.form = el)}>
        <input type="text" name="text2"/>
        <input type="text" name="text"/>    
        </form>
        <button onClick={() => this.fileDownload()}>Download</button>
         </div>
   );
  }
}
export default download_File;
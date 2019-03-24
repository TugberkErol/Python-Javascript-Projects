import React, { Component } from 'react';
import axios, { get,post } from 'axios';
 class list_files extends Component {
   constructor(props) {
    super(props);
    this.state ={
      files: []
    }
    this.onClick=this.onClick.bind(this)
}    
    onClick() {
     axios.post('http://localhost:5000/list_files')
      .then(res => {
        const files = res.data;
        this.setState({files});
      })
  }
   render() {
      return (
            <div className="list_files">
               <h1>List of Files</h1>
              <p>
               {this.state.files}
              </p>
        <button onClick={() => this.onClick()}>List All</button>
            </div>
      
      );
   }
}
export default list_files;
import React, { Component } from 'react';
import axios, { post } from 'axios';
 class deletee extends Component {
   constructor(props) {
    super(props);
    this.state ={
  
    }
    this.onClick=this.onClick.bind(this)
}    
    onClick(){
    const url ='http://localhost:5000/deletee';
    const formData = new FormData(this.form);
    return post(url, formData);
    }
   render() {
      return (
            <div>
            <h1>Delete Files</h1>
          <form ref={el => (this.form = el)}> 
          <input type="text" name="text"/>
           </form>
              <button onClick={() => this.onClick()}>Delete</button>
            </div>
      
      );
   }
}
export default deletee;
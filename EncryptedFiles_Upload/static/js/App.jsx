import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import uploader from './uploader';
import download_File from './download_File';
import list_files from "./list_files";
import deletee from "./deletee";

class App extends Component {
   render() {
      return (
         <Router>
            <div>
               <h2>File Storage Web Site</h2>                 
                <ul>
                  <li><Link to={'/uploader'}>Upload</Link></li>                                                                                    
                  <li><Link to={'/download_File'}>Download</Link></li>
                  <li><Link to={'/list_files'}>List Files</Link></li>
                  <li><Link to={'/deletee'}>Delete Files</Link></li>
               </ul>
               <hr />
               
               <Switch>
                  <Route exact path='/list_files' component={list_files}/>
                  <Route exact path='/uploader' component={uploader} />
                  <Route exact path='/download_File' component={download_File} />
                  <Route exact path='/deletee' component={deletee} />
               </Switch>
            </div>
         </Router>
      );
   }
}
export default App;
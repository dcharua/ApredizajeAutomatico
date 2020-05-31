import React from 'react';
import Predict from './components/predict'
import About from './components/about'
import MyNavbar from './components/MyNavbar';


import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import './App.css';


function App() {
  return (
    <Router>
      <div>

       <MyNavbar></MyNavbar>

        {/* A <Switch> looks through its children <Route>s and
          renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/predict">
            <Predict />
          </Route>
          {/* El path de / tiene que ir hasta abajo, hay un orden*/}
          <Route path="/">
            <h2 className="pageTitle">Home</h2>
            <p>Go to predict to test the model</p>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;

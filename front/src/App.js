import React from 'react';
import Predict from './components/predict'
import About from './components/about'
import Home from './components/home'
import MyNavbar from './components/MyNavbar';
import Cluster from './components/cluster';


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
          <Route path="/cluster">
            <Cluster />
          </Route>
          {/* El path de / tiene que ir hasta abajo, hay un orden*/}
          <Route path="/">

            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;

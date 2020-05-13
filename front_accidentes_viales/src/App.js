import React from 'react';
import Predict from './components/predict'
import About from './components/about'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/predict">Predict</Link>
            </li>
          </ul>
        </nav>

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
            <h3>HOME</h3>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;

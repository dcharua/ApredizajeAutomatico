import React from 'react';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import {Link} from "react-router-dom";

function MyNavbar() {
    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Navbar.Brand> <Link to="/">Home</Link> </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="mr-auto">
            <Link class="mar-r-1" to="/about"> About</Link>
            <Link to="/predict">Predict</Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
}
export default MyNavbar;



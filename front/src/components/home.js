import React from "react";

// reactstrap components
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import {Link} from "react-router-dom";
import About from "./about";

// core components

function Home() {

    let pageHeader = React.createRef();
    
    React.useEffect(() => {
        if (window.innerWidth < 991) {
        const updateScroll = () => {
            let windowScrollTop = window.pageYOffset / 3;
            pageHeader.current.style.transform =
            "translate3d(0," + windowScrollTop + "px,0)";
        };
        window.addEventListener("scroll", updateScroll);
        return function cleanup() {
            window.removeEventListener("scroll", updateScroll);
        };
        }
    });

  return (
    <>
          <div
        style={{
          backgroundImage: "url(" + require("../assets/img/home.jpg") + ")"
        }}
        className="page-header"
        data-parallax={true}
        ref={pageHeader}
      >
        <div className="filter" />
        <Container>
          <div className="motto text-center">
            <h1>Making safer cities</h1>
            <h3>We predict car accidents, saving lives and building the cities of the future</h3>
            <br />
            <Button className="btn-round" color="neutral" type="button" outline>
            <Link to="/predict">Predict</Link>
            </Button>
          </div>
        </Container>
      </div>
      <About></About>

      
    </>
  );
}

export default Home;
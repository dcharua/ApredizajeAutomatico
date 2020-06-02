import React, { useState , useEffect} from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import {
  BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';


function About() {

  const [data, setData] = useState([]); 


  useEffect(() => {
    let url = new URL('http://localhost:5000/predict?column=mes&model=polynomial_LSR&value=5&complete=True');
    fetch(url, {method: "GET",}).then(response => response.json())
      .then(res => {
        console.log(res)
          let newData = []
          res.prediction.y.forEach((accidents, i) => {
            newData.push({name: i +1, accidents: accidents})
          });
          setData(newData); 
      })
      .catch(error => {
      });
  }, [])
  

    
  return (
      <div className="main">
      <div className="section text-center">
        <Container>
          <Row>
            <Col className="ml-auto mr-auto" md="8">
              <h2 className="title">The problem</h2>
              <h5 className="description">
              It is a reality that Mexico City depends on automobile transport on a daily basis. There are more than 4.7 million registered motor vehicles in the city, either for private or public use. Due to the high vehicle capacity, a daily average of 1,095 road accidents of different character are recorded in the country's capital, positioning the city in third place within Mexico. At the national level, 2.2% of deaths are due to traffic accidents. Fortunately, data on these accidents have been recompiled and using statistical techniques, machine learning techniques and the use of datasets of automobile accidents in Mexico City, we will obtain predictions, patterns and trends to be able to predict future accidents and their peculiarities. By finding specific patterns we will be able to identify in which areas, dates, times or other variables influence the occurrence of car accidents, and suggestions and precautions can be elaborated to curve these figures.
              </h5>
              <br />
            </Col>
          </Row>
          <br />
          <br />
          <Row>
            <Col md="6">
              <div className="info">
                <div className="icon icon-info">
                  <i className="nc-icon nc-album-2" />
                </div>
                <div className="description">
                  <h4 className="info-title">Solution</h4>
                  <p className="description">
                  Fortunately, data on these accidents have been recompiled and using statistical techniques, machine learning techniques and the use of datasets of automobile accidents in Mexico City, we will obtain predictions, patterns and trends to be able to predict future accidents and their peculiarities. By finding specific patterns we will be able to identify in which areas, dates, times or other variables influence the occurrence of car accidents, and suggestions and precautions can be elaborated to curve these figures.
                  </p>
                </div>
              </div>
            </Col>
            <Col md="6">
              <div className="info">
                <div className="icon icon-info">
                  <i className="nc-icon nc-bulb-63" />
                </div>
                <div className="description">
                  <h4 className="info-title">Project</h4>
                  <p>
                  The project is designed as a tool so that users can inform themselves about the history of car accidents in CDMX by taking off relevant data such as the schedule with the most accidents, the day of the week with the most accidents, the influence of public holidays, etc. The user can also take the predictions as starting points for making decisions regarding transport in the city.
                  </p>                    
                </div>
              </div>
            </Col>
          </Row>
          {data.length > 0 ?
              <div>
                  <h3>Predicted car accidents per month in CDMX</h3>
              
                <BarChart width={1000} height={350} data={data} margin={{
                  top: 5, right: 30, left: 20, bottom: 5,
                }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="accidents" fill="#8884d8" />
                </BarChart>
              </div>
              : <div></div>
          }
        
        </Container>
      </div>
    </div>

  );
}
export default About;

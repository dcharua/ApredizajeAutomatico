import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form'
import Container from 'react-bootstrap/Container'
import Jumbotron from 'react-bootstrap/Jumbotron'



function Predict() {
    const [model, setModel] = useState('sklearn_polynomial_LSR');
    const [column, setColumn] = useState('mes');
    const [value, setValue] = useState('3');
    const [prediction_y, setPredictionY] = useState('0');
    const [prediction_r_sq, setPredictionRSQ] = useState('0');
    const [plot, setPlot] = useState('');


    const handleModelChange = (e) => setModel(e.target.value);
    const handleColumnChange = (e) => setColumn(e.target.value);
    const handleValueChange = (e) => setValue(e.target.value);


    const onPredict = (e) => {
        let url = new URL('http://127.0.0.1:5000/predict');
        url.search = new URLSearchParams({
            model: model,
            column: column,
            value: value
        })
        fetch(url, { method: "GET", mode: 'cors' }).then(response => { console.log(response); return response.json() })
            .then(data => {
                //console.log(data);
                setPredictionY(data.prediction.y);
                setPredictionRSQ(data.prediction.r_sq);
                setPlot(" data:image/jpeg;charset=utf-8;base64, " + data.plot);

            })
            .catch(error => {
                setPredictionY("error ocurred");
                setPredictionRSQ("error ocurred");
                console.log("error, failed to  communicate with the API");
                //console.log(error);
            });
    }
    return (
        <div>
            <Container>
                <h1>Predict</h1>
                <h3>Select Parameters:</h3>

                <Form>
                    <Form.Group controlId="exampleForm.ControlSelect1">
                        <Form.Label>Model</Form.Label>
                        <Form.Control as="select" onChange={e => handleModelChange(e)}>

                            <option value='sklearn_polynomial_LSR'>
                                sklearn_polynomial_LSR
                            </option>
                            <option value='polynomial_LSR'>
                                polynomial_LSR
                            </option>
                            <option value="linear_LSR">
                                linear_LSR
                            </option>
                            <option value='sklearn_linear_LSR'>
                                sklearn_linear_LSR
                            </option >
                        </Form.Control>
                    </Form.Group>
                    <Form.Group controlId="exampleForm.ControlInput2">
                        <Form.Label>Columna</Form.Label>
                        <Form.Control type="text" placeholder="mes" onChange={e => handleColumnChange(e)} />
                    </Form.Group>
                    <Form.Group controlId="exampleForm.ControlInput3">
                        <Form.Label>Value</Form.Label>
                        <Form.Control type="text" placeholder="3" onChange={e => handleValueChange(e)} />
                    </Form.Group>
                    <Button
                        onClick={e => onPredict(e)}>
                        Predict
                    </Button>

                </Form>

                <Jumbotron>
                    <h2>Prediction Y : {prediction_y}</h2>
                    <h2>Prediction R_SQ : {prediction_r_sq}</h2>
                    <img src={plot} alt="Plot"></img>
                </Jumbotron>
            </Container>

        </div >
    );
}
export default Predict;



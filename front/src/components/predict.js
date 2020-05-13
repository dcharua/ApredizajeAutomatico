import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';




function Predict() {
    const [model, setModel] = useState('sklearn_linear_LSR');
    const [column, setColumn] = useState('');
    const [value, setValue] = useState('');
    const [prediction, setPrediction] = useState('0');

    const handleModelChange = (e) => { setModel(e.target.value); console.log(e.target.value); }
    const handleColumnChange = (e) => { setColumn(e.target.value); console.log(e.target.value); }
    const handleValueChange = (e) => { setValue(e.target.value); console.log(e.target.value); }


    const onPredict = (e) => {
        let url = new URL('http://127.0.0.1:5000/predict');
        url.search = new URLSearchParams({
            model: model,
            column: column,
            value: value
        })
        fetch(url, {
            // mode: 'no-cors',
            method: "GET",
            //body: JSON.stringify({ "model": model, "column": "mes", "value": 3 }),
        })
            .then(response => response.json())
            .then(data => {
                console.info(data)
                //setPrediction("58654");
                setPrediction(response.prediction.y);

            })
            .catch(error => {
                setPrediction("error ocurred");
                console.log("error, failed to  communicate with the API");
                console.log(error);
            });
    }
    return (
        <div>
            <h3>PREDICT</h3>

            <h2>Select Parameters:</h2>
            <div className="predictForm">
                <label>Model</label>
                <select onChange={e => handleModelChange(e)}>
                    <option value='sklearn_linear_LSR'>
                        sklearn_linear_LSR
                </option >
                    <option value='polynomial_LSR'>
                        polynomial_LSR
                </option>
                    <option value='linear_LSR'>
                        linear_LSR
                </option>
                </select>
                <label> Columna</label>
                <input onChange={e => handleColumnChange(e)}>
                </input>
                <label> Value</label>
                <input onChange={e => handleValueChange(e)}>
                </input>
            </div>
            <div className="predictForm">
                <Button
                    onClick={e => onPredict(e)}>
                    Predict
            </Button>
            </div>

            <div>
                <h2>Prediction: {prediction}</h2>
            </div>
        </div >
    );
}
export default Predict;



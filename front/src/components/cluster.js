import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form'
import Container from 'react-bootstrap/Container'
import Jumbotron from 'react-bootstrap/Jumbotron'



function Cluster() {
    const [model, setModel] = useState('agglo_cluster');
    const [month, setMonth] = useState(2);
    const [year, setYear] = useState(2016);
    const [clusters, setClusters] = useState(5);
    const [plot, setPlot] = useState('');
    const handleModelChange = (e) => setModel(e.target.value);
    const handleMonthChange = (e) => setMonth(e.target.value);
    const handleYearChange = (e) => setYear(e.target.value);
    const handleClustersChange = (e) => setClusters(e.target.value);



    const onPredict = (e) => {
        let url = new URL('http://127.0.0.1:5000/cluster');
        url.search = new URLSearchParams({
            model: model,
            month: month,
            year: year,
            clusters: clusters
        })
        fetch(url, { method: "GET", mode: 'cors' }).then(response => { console.log(response); return response.json() })
            .then(data => {
                setPlot("data:image/jpeg;charset=utf-8;base64, " + data.plot);

            })
            .catch(error => {
                setPlot("error ocurred");
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
                            <option value='agglo_cluster'>
                                agglo_cluster
                            </option>
                            <option value='modelo2'>
                                modelo2
                            </option>

                        </Form.Control>
                    </Form.Group>
                    <Form.Group controlId="exampleForm.ControlInput2">
                        <Form.Label>Mes</Form.Label>
                        <Form.Control type="text" placeholder="mes" onChange={e => handleMonthChange(e)} />
                    </Form.Group>
                    <Form.Group controlId="exampleForm.ControlInput3">
                        <Form.Label>Año</Form.Label>
                        <Form.Control type="text" placeholder="año" onChange={e => handleYearChange(e)} />
                    </Form.Group>
                    <Form.Group controlId="exampleForm.ControlInput3">
                        <Form.Label>Clusters</Form.Label>
                        <Form.Control type="text" placeholder="clusters" onChange={e => handleClustersChange(e)} />
                    </Form.Group>
                    <Button
                        onClick={e => onPredict(e)}>
                        Predict
                    </Button>

                </Form>

                <Jumbotron>

                    <img src={plot} alt="Plot"></img>
                </Jumbotron>
            </Container>

        </div >
    );
}
export default Cluster;



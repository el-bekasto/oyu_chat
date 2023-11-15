import React, {useState} from 'react';
import {login} from '../actions/auth';
import {connect} from 'react-redux';
import {Navigate} from "react-router-dom";
import Container from "react-bootstrap/Container";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import CSRFToken from "./CSRFToken";
import {Link} from "react-router-dom";

function Login({ isAuthenticated, login }) {
    const [formData, setFormData] = useState({
        username: '',
        password: ''
    });
    const [loggedIn, setLoggedIn] = useState(false);

    function onChange(event) {
        setFormData({ ...formData, [event.target.name]: event.target.value })
    }
    function onSubmit(event) {
        event.preventDefault();

        login(formData.username, formData.password);
        setLoggedIn(true);
    }

    if (loggedIn || isAuthenticated) {
        return (<Navigate to={'/'}/>);
    }

    return (
        <Container>
            <h1>Sign in</h1>
            <p>Log into your account and start chatting right now!</p>
            <Form onSubmit={e => onSubmit(e)}>
                <CSRFToken/>
                <Row>
                    <Col>
                        <Form.Group className={'mt-3'} controlId={'formUsername'}>
                            <Form.Label>Username</Form.Label>
                            <Form.Control
                                type={'text'}
                                placeholder={'Enter username'}
                                name={'username'}
                                value={formData.username}
                                onChange={e => onChange(e)}
                                required
                            />
                        </Form.Group>
                    </Col>
                    <Col>
                        <Form.Group className={'mt-3'} controlId={'formPassword'}>
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                type={'password'}
                                placeholder={'Enter password'}
                                name={'password'}
                                value={formData.password}
                                onChange={e => onChange(e)}
                                required
                            />
                        </Form.Group>
                    </Col>
                </Row>
                <Button className={'mt-3'} type={'submit'}>Log in</Button>
            </Form>
            <p className={'mt-3'}>
                Don't have an account? <Link to={'/register'}>Create one!</Link>
            </p>
        </Container>
    )
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { login })(Login);
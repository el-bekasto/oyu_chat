import React, {useState} from 'react';
import {register} from '../actions/auth';
import {connect} from 'react-redux';
import {redirect} from 'react-router-dom';
import Container from "react-bootstrap/Container";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function Register({ register }) {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        re_password: ''
    });
    const [accountCreated, setAccountCreated] = useState(false);

    function onChange(event) {
        setFormData({ ...formData, [event.target.name]: event.target.value })
    }
    function onSubmit(event) {
        event.preventDefault();

        if (formData.password === formData.re_password) {
            register(formData.username, formData.password, formData.re_password);
            setAccountCreated(true);
        }
    }

    if (accountCreated) {
        // return redirect('/');
    }

    return (
        <Container>
            <h1>Register</h1>
            <p>Create an account and join our wonderful chat app!</p>
            <Form onSubmit={e => onSubmit(e)}>
                <Form.Group controlId={'formUsername'}>
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
                <Form.Group className={'mt-3'} controlId={'formPassword'}>
                    <Form.Label>Password</Form.Label>
                    <Row>
                        <Col>
                            <Form.Control
                                type={'password'}
                                placeholder={'Enter password'}
                                name={'password'}
                                value={formData.password}
                                onChange={e => onChange(e)}
                                minLength={8}
                                required
                            />
                        </Col>
                        <Col>
                            <Form.Control
                                type={'password'}
                                placeholder={'Confirm password'}
                                name={'re_password'}
                                onChange={e => onChange(e)}
                                value={formData.re_password}
                                minLength={8}
                                required
                            />
                        </Col>
                    </Row>
                </Form.Group>
                <Button className={'mt-3'} type={'submit'}>Register</Button>
            </Form>
            <p className={'mt-3'}>
                Already have an account? <a href={'/login'}>Sign in</a>
            </p>
        </Container>
    )
}

export default connect(null, { register })(Register);
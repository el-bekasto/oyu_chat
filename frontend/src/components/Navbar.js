import Nav from 'react-bootstrap/Nav';
import Navbar from "react-bootstrap/Navbar";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Offcanvas from "react-bootstrap/Offcanvas";
import '../styles/Navbar.css';

export default function NavbarComponent () {
    return (
        <Row>
            <Col lg={2}>
                <Navbar key={false} expand={false} collapseOnSelect>
                    <Container fluid>
                        <Navbar.Toggle aria-controls={`offcanvasNavbar-expand-${false}`}/>
                        <Navbar.Offcanvas
                            id={`offcanvasNavbar-expand-${false}`}
                            aria-labelledby={`offcanvasNavbarLabel-expand-${false}`}
                            placement="start"
                        >
                            <Offcanvas.Header closeButton>
                                <Container fluid>
                                    <Row>
                                        <Col lg={2}>
                                          <img src={'https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg?20200418092106'}/>
                                        </Col>
                                        <Col>
                                            <span>Beknur Seydazim Torebekuly</span>
                                            <br></br>
                                            <span style={{fontSize: '10px'}}>+7 706 428 24 15</span>
                                        </Col>
                                    </Row>
                                </Container>
                            </Offcanvas.Header>
                            <Offcanvas.Body>
                                <Nav className={'flex-column'}>
                                    <Nav.Link>1</Nav.Link>
                                    <Nav.Link>2</Nav.Link>
                                    <Nav.Link>3</Nav.Link>
                                    <Nav.Link>4</Nav.Link>
                                </Nav>
                            </Offcanvas.Body>
                        </Navbar.Offcanvas>
                        <Navbar.Brand href={"/"}>Chats</Navbar.Brand>
                    </Container>
                </Navbar>
            </Col>
        </Row>
    )
}
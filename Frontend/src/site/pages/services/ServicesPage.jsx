import React from 'react'
import { Container, Col, Row, Card} from 'react-bootstrap';
import { Link } from 'react-router-dom'
import ServiceCard from './components/ServiceCard';
import './style/css/service.css'

export const ServicesPage = () => {
  return (
    <>

    <Container>
    <Row className = "srv_row">
      <text>OUR SERVICES</text>
    </Row>
    <Row>
      
      <Col>
          <ServiceCard/>
      </Col>
      <Col>
          <ServiceCard/>
      </Col>
      <Col>
          <ServiceCard/>
      </Col>
      <Col>
          <ServiceCard/>
      </Col>
    </Row>
  </Container>
</>
  )
}

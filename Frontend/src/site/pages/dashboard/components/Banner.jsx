import React from 'react'
import { Container, Col, Row, Image, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom'
import '../styles/banner.css'
export const Banner = () => {
  return (
    <>


      <Container className='bn_con'>
        <Row className='bn_row'>
          <Col className='bn_col'>
            <text className="bn_title">
              Amet minim
              mollit non si
            </text>
            <p className='bn_paragraph'>
              Amet minim mollit non deserunt ullamco est <br />
              sit aliqua dolor do amet sint velit
            </p>
            <Link to="/">
              <Button className='bn_button' title='Call to action'>

                Call to action

              </Button>
            </Link>
          </Col>
          <Col>
            <Image className='bn_img'
              src='https://github.com/Dargeo/images/blob/master/handyman.png?raw=true'

            />
          </Col>
        </Row>
      </Container>
    </>
  )
}

import { Navbar, NavDropdown, Nav, Offcanvas } from 'react-bootstrap';
import { HashLink as Link } from 'react-router-hash-link';

export const NavBar = () => {

  return (
    <Navbar fixed='top'expand="lg" className="">

      <Navbar.Brand href="/" className='row align-items-center'>
        <img
          alt='Cameinhandyman Logo'
          src='https://static.wixstatic.com/media/e1b08d_62533ab5c805474db01c37ffdcb1b4be~mv2.png/v1/fill/w_78,h_78,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Copy%20of%20OnHandy.png'
          className='col-6'
        />
        <span className='col-2'>Came in <br /> Handyman</span>
      </Navbar.Brand>

      <Navbar.Toggle aria-controls='offcanvasNavbar-expand-lg' className='mx-3' />

      <Navbar.Offcanvas
        id='offcanvasNavbar-expand-lg'
        aria-labelledby='offcanvasNavbar-expand-lg'
        placement="end"
        className="text-bg-dark"
      >
        <Offcanvas.Header closeButton closeVariant='white'>
          <Offcanvas.Title className='row align-items-center'>
            <img
              alt='Came in Handyman'
              src='https://static.wixstatic.com/media/e1b08d_62533ab5c805474db01c37ffdcb1b4be~mv2.png/v1/fill/w_78,h_78,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Copy%20of%20OnHandy.png'
              className='col-5'
            />
            <span className='col-4'>
              Came in Handyman
            </span>
          </Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
          <Nav className="justify-content-evenly flex-grow-1 pe-3">
            <Nav.Link className='fw-bolder' href="#about">About</Nav.Link>
            <Nav.Link className='fw-bolder' href="#services">Services</Nav.Link>
            <Nav.Link className='fw-bolder' href="#calendar">Calendar</Nav.Link>
            <Nav.Link className='fw-bolder' href="#contact">Contact</Nav.Link>
          </Nav>
        </Offcanvas.Body>
      </Navbar.Offcanvas>
    </Navbar>
  )
}

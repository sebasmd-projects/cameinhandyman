import { Navbar, NavDropdown,Container, Nav, Offcanvas } from 'react-bootstrap';
import { HashLink as Link } from 'react-router-hash-link';
import React,{useState, useEffect} from 'react';
import './css/navBar.css'
export const NavBar = () => {

  const [navbarsito,setNavbar] = useState(false);
  const specs = document.querySelector('#services')
  const changeBackground = ()=> {
    console.log(specs.getBoundingClientRect().top)
    if(specs.getBoundingClientRect().top <=0){
      setNavbar(true);
    }else{
      setNavbar(false)
    }
  }

  window.addEventListener('scroll',changeBackground);
  return (
    <Navbar class="navbar fixed-top navbar-expand-lg navbar-dark p-md-3">
      <Container>
        <a class="navbar-brand" href="#">Web Zone</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <div class="mx-auto"></div>
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link text-white" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="#">Blog</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </Container>
    </Navbar>
  )
}

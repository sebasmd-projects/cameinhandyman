import React from 'react'
import { NavBar } from '../../helpers/generalComponents/NavBar';
import  AboutPage  from '../about/AboutPage';
import { ServicesPage } from '../services/ServicesPage';

import './dashboard.css'


export const DashboardPage = ({ title }) => {
  document.title = title;
  return (

    <>
      <NavBar />
      <section id='about' className='section_about'>

        <AboutPage />

      </section>
      <section id='services' className='section_services'>

        <ServicesPage />

      </section>

    </>
  )
}

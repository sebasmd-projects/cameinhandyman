import React from 'react'
import { NavBar } from '../../helpers/generalComponents/NavBar';
import { Banner } from './components/Banner';
import { Service } from './components/Service';
import './dashboard.css'

export const DashboardPage = ({ title }) => {
  document.title = title;
  return (

    <>
      <NavBar />
      <section id='about' className='section_about'>

        <Banner />

      </section>
      <section id='services' className='section_services'>

        <Service />

      </section>

    </>
  )
}

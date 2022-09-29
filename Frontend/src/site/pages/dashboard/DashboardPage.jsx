import React from 'react'
import { Container } from 'react-bootstrap';
import { NavBar } from '../../helpers/generalComponents/NavBar';
import { BannerSection } from './components/BannerSection';
import { HomeContent } from './components/HomeContent';
import './styles/DashboardPage.css'

export const DashboardPage = ({ title }) => {
  document.title = title;

  return (
    <>
      <NavBar />

      <div className='row d-flex align-items-center justify-content-between browser_background_img cel_vh'>
        <BannerSection />
      </div>

      <Container className='mt-4'>
        <HomeContent />
      </Container>
    </>
  )
}

import React from 'react'
import { Link } from 'react-router-dom';
import { NavBar } from '../../helpers/generalComponents/NavBar';

export const DashboardPage = ({ title }) => {
  document.title = title;

  return (
    <>
      <NavBar />
      <div className='row align-items-center'>
        <div className="col-6 ms-2">
          <h2 style={{ fontSize: "calc(2rem + 0.4vw)" }} className="ms-md-5">Amet minim</h2>
          <h2 style={{ fontSize: "calc(2rem + 0.1vw)" }} className="ms-md-5">mollit non si</h2>

          <p style={{ fontSize: "calc(1rem + 0.2vw)" }} className='mt-3 ms-md-5 mt-sm-5'>
            Amet minim mollit non deserunt ullamco est <br />
            sit aliqua dolor do amet sint velit
          </p>

          <Link to="/" className="btn btn-warning ms-sm-5">
            Call to action
          </Link>

        </div>
        <div className="col-5 ">
          <img className="img-fluid"
            alt='Home Handyman'
            src="data:image/jpeg;base64,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"
          />
        </div>
      </div>
    </>
  )
}

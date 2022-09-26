import React from 'react'
import { Link } from 'react-router-dom';


export const BannerSection = () => {
  return (
    <>
      <div className="col-6 offset-1">
        <h2 style={{ fontSize: "calc(2rem + 0.4vw)" }} className="ms-md-5 text-white">Amet minim</h2>
        <h2 style={{ fontSize: "calc(2rem + 0.1vw)" }} className="ms-md-5 text-white">mollit non si</h2>

        <p style={{ fontSize: "calc(1rem + 0.2vw)" }} className='mt-3 ms-md-5 mt-sm-5 text-white'>
          Amet minim mollit non deserunt ullamco est <br />
          sit aliqua dolor do amet sint velit
        </p>
        
        <Link to="/" className="btn btn-primary ms-sm-5">
          Call to action
        </Link>

      </div>
      <div className="col-5 ">
        <img className="mt-5"
          alt='Home Handyman'
          src="https://raw.githubusercontent.com/Dargeo/images/master/handyman.png"
          style={{ width: "80%" }}
        />
      </div>
    </>
  )
}

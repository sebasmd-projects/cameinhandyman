import React from 'react'
import { Link } from 'react-router-dom';


export const BannerSection = () => {
  return (
    <>
      <div className="col-6 offset-1">
        <h2 className="ms-md-5 text-white">Amet minim <br/>mollit non si</h2>

        <p className='mt-3 ms-md-5 mt-sm-5 text-white'>
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
          style={{ width: "90%" }}
        />
      </div>
    </>
  )
}

import React, { useState } from 'react'

const SideBar = () => {
  const [showSideBar,setShowSideBar]=useState(false)
    return (
        <>

        <button className='sidebar-button'onClick={()=>{setShowSideBar(true)}}><i className="fas fa-align-justify"></i></button>
    <div className={`${showSideBar ? 'sidebar-show':'sidebar-notshow'} `}>
        <button onClick={()=>{setShowSideBar(false)}} className='cancel-button'><i className="fas fa-x"></i></button>
    <ul className={`${showSideBar ? 'show':'notshow'} side-list `}>
        <li><a className="navbar-brand" href="#"><span className='first-letter'>K</span>asem</a></li>
        <li>Overview</li>
        <li>Dashboard</li>
        <li>Categories</li>
        <li>Contact us</li>
    </ul>
    </div>
        </>
  )
}

export default SideBar
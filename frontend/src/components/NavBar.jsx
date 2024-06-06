import React from "react";
import SideBar from "./SideBar.jsx";

const NavBar = () => {
  return (
    <nav className="">
      <div className="side-brand">
        <SideBar />
        <a className="navbar-brand" href="#">
          <span className="first-letter">K</span>asem
        </a>
      </div>

      <div className="navbar-list" id="navbarSupportedContent">
        <ul className="nav-list ml-auto">
          <li className=" ">
            <a className="nav-link" href="#">
              Sign in
            </a>
          </li>
          <li className=" ">
            <a className="nav-link" href="#">
              About us
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default NavBar;

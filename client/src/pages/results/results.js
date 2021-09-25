import React from "react";
import { Link } from "react-router-dom";
import Card from "../../components/card/card";
import "../home/home.css";

export default function Results() {
  return (
    <React.Fragment>
      <Link to="/Main" style={{ textDecoration: "none", margin: "5px" }}>
        {" "}
        &#10094;{" "}
      </Link>
      <div className="font" style={{textAlign:"center", fontWeight: "600", padding:"40px"}}>Detect number of people around me </div>
      <div className="font" style={{ fontSize: "20px", fontWeight: "600" }}>
        <div style={{marginLeft:"16px", marginBottom:"11px"}}>There are: </div>
        <Card text="4" />
        <div style={{marginLeft:"16px", marginTop:"11px"}}>people around you</div>
      </div>
    </React.Fragment>
  );
}

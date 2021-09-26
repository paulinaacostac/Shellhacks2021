import React from "react";
import { Link } from "react-router-dom";
import Card from "../../components/card/card";
import "../home/home.css";


export default function Results3(){

    return (
      <React.Fragment>
        
        <Link to="/Main" style={{ textDecoration: "none", margin: "5px" }}>
          {" "}
          &#10094;{" "}
        </Link>
        <div className="font" style={{textAlign:"center", fontWeight: "600", padding:"20px"}}>Detect objects around me</div>
        <div className="font" style={{ fontSize: "20px", fontWeight: "600" }}>
          <div style={{marginLeft:"16px", marginBottom:"11px"}}>There are: </div>
          <Card text="4" />
          <div style={{marginLeft:"16px", marginTop:"11px"}}>objects around you.</div>
          <div style={{marginLeft:"16px", marginTop:"11px", marginBottom:"20px"}}>The list of objects is:</div>
          <Card text="Phone Laptop Bag Toothbrush Spoon" font={20}/>
        </div>
      </React.Fragment>
  
    )
  }
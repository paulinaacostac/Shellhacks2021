import React from "react";
import { Link } from "react-router-dom";
import Card from "../../components/card/card";
import "../home/home.css";


export default function Results4(){

    return (
      <React.Fragment>
        
        <Link to="/Main" style={{ textDecoration: "none", margin: "5px" }}>
          {" "}
          &#10094;{" "}
        </Link>
        <div className="font" style={{textAlign:"center", fontWeight: "600", padding:"40px"}}>Find an object</div>
        <div className="font" style={{ fontSize: "20px", fontWeight: "600" }}>
          <div style={{marginLeft:"16px", marginBottom:"11px"}}>The object requested is: </div>
          <Card text="Phone" />
          <div style={{marginLeft:"16px", marginTop:"11px", marginBottom:"10px"}}>Distance to this object:</div>
          <Card text="70 inches away to the left" font={20}/>
        </div>
      </React.Fragment>
  
    )
  }
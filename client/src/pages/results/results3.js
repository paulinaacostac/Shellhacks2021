import React from "react";
import { Link } from "react-router-dom";
import Card from "../../components/card/card";
import "../home/home.css";

export default function Results3() {
  return (
    <React.Fragment>
      <Link to="/Main" style={{ textDecoration: "none", margin: "5px" }}>
        {" "}
        &#10094;{" "}
      </Link>
      <div
        className="font"
        style={{ textAlign: "center", fontWeight: "600", padding: "20px" }}
      >
        Detect objects around me
      </div>
      <div className="font" style={{ fontSize: "20px", fontWeight: "600" }}>
        <div style={{ marginLeft: "16px", marginBottom: "11px" }}>
          There are:{" "}
        </div>
        <Card text="4" />
        <div style={{ marginLeft: "16px", marginTop: "11px" }}>
          objects around you.
        </div>
        <div
          style={{
            marginLeft: "16px",
            marginTop: "11px",
            marginBottom: "20px",
          }}
        >
          The list of objects is:
        </div>
        <div
          to="/Results"
          className="font detect poster"
          style={{
            textDecoration: "none",
            maxWidth: "200px",
            border: "none",
            
            justifyContent: "center",
            margin: "auto",
            padding: "35px 25px",
            backgroundColor: "green",
            borderRadius: "15px",
            color: "black",
            fontSize: "22px",
            fontWeight: "600",
            letterSpacing: "1px",
            textAlign: "center",
          }}
        >
          {" "}
          <div> Phone </div>
          <div> Laptop </div>
          <div> Bag </div>
          <div> Toothbrush </div>
          <div> Spoon </div>
        </div>
      </div>
    </React.Fragment>
  );
}

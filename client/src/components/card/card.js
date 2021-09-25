import React from "react";
import "../../pages/home/home.css";

export default function Card(props) {
  return (
    <React.Fragment>
      <div
        to="/Results"
        className="font detect poster"
        style={{
          textDecoration: "none",
          maxWidth: "200px",
          border: "none",
          maxHeight:"50px",
          justifyContent:"center",
          margin:"auto",
          padding: "35px 25px",
          backgroundColor: "green",
          borderRadius: "15px",
          color: "black",
          fontSize: "40px",
          fontWeight: "600",
          letterSpacing: "1px",
          textAlign: "center",
        }}
      >
        {" "}
        <div style={{ height: "90px" }}>{props.text} </div>
      </div>
    </React.Fragment>
  );
}

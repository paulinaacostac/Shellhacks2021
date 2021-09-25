import React from "react";
import { Link } from "react-router-dom";
import "../home/home.css";

export default function Profile() {
  return (
    <React.Fragment>
      <Link to="/Main" style={{ textDecoration: "none", margin: "5px" }}>
        {" "}
        &#10094;{" "}
      </Link>
      <div
        className="font"
        style={{ fontSize: "20px", fontWeight: "600", padding: "20px" }}
      >
        Profile
      </div>
      <div
        className="font"
        style={{ justifyContent: "center", margin: "auto", maxWidth: "180px" }}
      >
        <div style={{ borderBottom: "1px solid gray", paddingBottom: "5px" }}>
          Name
          <input type="text" placeholder="Fran M" style={{ border: "none" }} />
        </div>
        <div
          style={{
            borderBottom: "1px solid gray",
            marginTop: "20px",
            paddingBottom: "5px",
          }}
        >
          Email
          <input
            type="text"
            placeholder="franmazzei00@gmail.com"
            style={{ border: "none" }}
          />{" "}
        </div>
      </div>
      <Link
        to=""
        style={{
          margin: "auto",
          justifyContent: "center",
          display: "flex",
          textDecoration: "none",
          marginTop: "40px",
        }}
      >
        <button
          className="font"
          style={{
            textDecoration: "none",
            border: "none",
            borderRadius: "15px",
            padding: "10px 15px",
          }}
        >
          Log out
        </button>
      </Link>
    </React.Fragment>
  );
}

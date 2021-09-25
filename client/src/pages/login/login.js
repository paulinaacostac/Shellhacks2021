import React from "react";
import { Link } from "react-router-dom";
import "../home/home.css";

export default function Login() {
  return (
    <React.Fragment>
      <Link to="" style={{ textDecoration: "none", margin: "5px" }}>
        {" "}
        &#10094;{" "}
      </Link>
      <div style={{ margin: "auto", textAlign: "center" }}>
        <div
          className="font"
          style={{ margin: "20px", fontSize: "20px", fontWeight: "600" }}
        >
          Login
        </div>

        <input
          type="text"
          style={{
            margin: "20px",
            borderRadius: "10px",
            border: "1px solid gray",
            padding: "8px 9px",
          }}
          placeholder="Email adress"
        />
        <input
          type="text"
          style={{
            margin: "10px",
            borderRadius: "10px",
            border: "1px solid gray",
            padding: "8px 9px",
          }}
          placeholder="Password"
        />
        <Link to="/Main">
          <button style={{ margin: "20px 20px" }} className="button">
            Login
          </button>
        </Link>
        <Link to="/Create">
        <button className="button2" style={{ textDecoration: "underline" }}>
          {" "}
          Create an account
        </button>
        </Link>
      </div>
    </React.Fragment>
  );
}

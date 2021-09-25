import React from "react";
import { Link } from "react-router-dom";

export default function Create() {
  function handleCreate() {}

  return (
    <React.Fragment>
      <Link to="" style={{ textDecoration: "none", margin:"5px" }}>
        {" "}
        &#10094;{" "}
      </Link>
      <div style={{ textAlign: "center" }} className="font">
        <div style={{ fontSize: "20px", margin: "40px", fontWeight: "600" }}>
          Create an account
        </div>
        <input
          type="text"
          style={{
            borderRadius: "10px",
            border: "1px solid gray",
            padding: "8px 9px",
          }}
          placeholder="Full name"
        />
        <input
          style={{
            margin: "20px",
            borderRadius: "10px",
            border: "1px solid gray",
            padding: "8px 9px",
          }}
          type="text"
          placeholder="Email adress"
        />
        <input
          style={{
            marginBottom: "30px",
            borderRadius: "10px",
            border: "1px solid gray",
            padding: "8px 9px",
          }}
          type="text"
          placeholder="Password"
        />

        <button className="button" onClick={() => handleCreate()}>
          Create account
        </button>

        <Link to="/Login">
          <button
            className="button2"
            style={{ margin: "20px", textDecoration: "underline" }}
          >
            Already have an account?
          </button>
        </Link>
      </div>
    </React.Fragment>
  );
}

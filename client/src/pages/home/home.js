import React from "react";
import { Link } from "react-router-dom";
import "./home.css";

export default function Home() {
  return (
    <React.Fragment>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          minHeight: "100vh",
        }}
      >
        <div
          style={{
            justifyContent: "center",
            margin: "auto",
            textAlign: "center",
            alignItems: "center",
          }}
          className="font"
        >
          <img src={require("../..//img/logo.png").default} height={200} />
          <div style={{ fontSize: "20px", margin: "20px", fontWeight: "600" }}>
            Help maintain social distancing
          </div>
          <div style={{ margin: "20px" }}>Please select an option:</div>
          <Link to='/Create'>
            <button className="button" style={{ margin: "20px" }}>
              {" "}
              Create account
            </button>
          </Link>
          <Link to='/Login'>
            <button className="button2"> Login</button>
          </Link>
        </div>
      </div>
    </React.Fragment>
  );
}

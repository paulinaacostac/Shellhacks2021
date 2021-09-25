import React from "react";
import "../home/home.css";
import "./main.css";

export default function Main() {
  return (
    <React.Fragment>
      <div style={{ maxWidth: "270px", textAlign: "left" }}>
        <div
          className="font"
          style={{ margin: "20px", fontWeight: "600", fontSize: "25px" }}
        >
          Welcome
        </div>
        <button
          className="font video"
          style={{
            textDecoration: "none",
            minWidth: "270px",
            border: "none",
            padding: "35px 25px",
            backgroundColor: "green",
            borderRadius: "15px",
            color: "white",
            fontSize: "20px",
            fontWeight: "600",
            letterSpacing: "1px",
          }}
        >
          Livestream Video &#9887;
        </button>
        <div className="font" style={{ fontWeight: "600", margin: "20px" }}>
          Activities
        </div>

        <div className="row">
          <div
            className="font detect poster"
            style={{
              textDecoration: "none",
              maxWidth: "270px",
              border: "none",
              width: "100%",
              minWidth: "160px",
              padding: "35px 25px",
              backgroundColor: "green",
              borderRadius: "15px",
              color: "white",
              fontSize: "20px",
              fontWeight: "600",
              letterSpacing: "1px",
              textAlign: "center",
            }}
          >
            {" "}
            <div style={{ height: "90px" }}>
              Detect number of people around me{" "}
            </div>
            <div>&#10043; </div>
          </div>

          <div
            className="font detect2 poster"
            style={{
              textDecoration: "none",
              maxWidth: "270px",
              width: "100%",
              minWidth: "160px",
              border: "none",
              padding: "35px 25px",
              backgroundColor: "green",
              borderRadius: "15px",
              color: "white",
              fontSize: "20px",
              fontWeight: "600",
              letterSpacing: "1px",
              textAlign: "center",
            }}
          >
            {" "}
            <div style={{ height: "90px" }}>
              Detect number of people less than 6 feet{" "}
            </div>
            <div>&#10043; </div>
          </div>
          <div
            className="font detect3 poster"
            style={{
              textDecoration: "none",
              maxWidth: "270px",
              border: "none",
              width: "100%",
              minWidth: "160px",
              padding: "35px 25px",
              backgroundColor: "green",
              borderRadius: "15px",
              color: "white",
              fontSize: "20px",
              fontWeight: "600",
              letterSpacing: "1px",
              textAlign: "center",
            }}
          >
            {" "}
            <div style={{ height: "90px" }}>Detect objects around me </div>
            <div>&#10043; </div>
          </div>
          <div
            className="font detect4 poster"
            style={{
              textDecoration: "none",
              maxWidth: "270px",
              border: "none",
              width: "100%",
              minWidth: "160px",
              padding: "35px 25px",
              backgroundColor: "green",
              borderRadius: "15px",
              color: "white",
              fontSize: "20px",
              fontWeight: "600",
              letterSpacing: "1px",
              textAlign: "center",
            }}
          >
            {" "}
            <div style={{ height: "60px" }}>Find an object </div>
            <div>&#10043; </div>
          </div>
          <div
            className="font detect5 poster"
            style={{
              textDecoration: "none",
              maxWidth: "270px",
              border: "none",
              width: "100%",
              minWidth: "160px",
              padding: "35px 25px",
              backgroundColor: "green",
              borderRadius: "15px",
              color: "white",
              fontSize: "20px",
              fontWeight: "600",
              letterSpacing: "1px",
              textAlign: "center",
            }}
          >
            {" "}
            <div
              style={{
                height: "60px",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              {" "}
              Read text around me{" "}
            </div>{" "}
            <div>&#10043; </div>
          </div>
          <div
            className="font detect6 poster"
            style={{
              textDecoration: "none",
              maxWidth: "270px",
              border: "none",
              width: "100%",
              minWidth: "160px",
              padding: "35px 25px",
              backgroundColor: "green",
              borderRadius: "15px",
              color: "white",
              fontSize: "20px",
              fontWeight: "600",
              letterSpacing: "1px",
              textAlign: "center",
            }}
          >
            {" "}
            <div style={{ height: "90px", justifyContent: "center" }}>
              Road recognition for navigation
            </div>
            <div>&#10043; </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

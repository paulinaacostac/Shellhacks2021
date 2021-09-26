import React from "react";
import { AiFillHome } from "react-icons/ai";
import { FiUser } from "react-icons/fi";
import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <React.Fragment>
      <div>
        <div
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            bottom: 0,
            background: "#F3F3F3",
            width: "100%",
            height: "40px",
            textAlign: "center",
          }}
        >
          <div
            style={{
              justifyContent: "space-between",
              maxWidth: "90px",
              display: "flex",
              margin: "auto",
              alignItems: "center",
            }}
          >
            <Link
              style={{
                textDecoration: "none",
                color: "black",
                fontSize: "25px",
                paddingTop: "5px",
              }} to="/Main"
            >
              <AiFillHome />{" "}
            </Link>
            <Link
              to="/Profile"
              style={{ color: "black", fontSize: "25px", paddingTop: "5px" }}
            >
              <FiUser />{" "}
            </Link>{" "}
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

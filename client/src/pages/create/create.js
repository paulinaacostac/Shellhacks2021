import React from "react";
import { Link } from "react-router-dom";

export default function Create() {
  function handleCreate() {}

  return (
    <React.Fragment>
      <div>Create an account</div>
      <input type="text" placeholder="Full name"/>
      <input type="text" placeholder="Email adress"/>
      <input type="text" placeholder="Password"/>

      <button onClick={() => handleCreate()}>Create account</button>

      <Link to="/Login">
        <button>Already have an account</button>
      </Link>
    </React.Fragment>
  );
}

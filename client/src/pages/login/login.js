import React from "react";

export default function Login() {
  return (
    <React.Fragment>
      <div>login</div>

      <input type="text" placeholder="Email adress"/>
      <input type="text" placeholder="Password"/>

      <button>Login</button>
      <button> Create an account</button>
    </React.Fragment>
  );
}
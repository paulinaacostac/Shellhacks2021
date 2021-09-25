import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Create from "./pages/create/create";
import F4f from "./pages/f4f/f4f";
import Home from "./pages/home/home";
import Login from "./pages/login/login";
import Main from "./pages/main/main";
import "./App.css";
import Profile from "./pages/profile/profile";
import Results from "./pages/results/results";

function App() {
  return (
    <React.Fragment>
      <Router>
        <Switch>
          <Route exact strict path="/" component={Home} />
          <Route exact strict path="/Create" component={Create} />
          <Route exact strict path="/Login" component={Login} />
          <Route exact strict path="/Main" component={Main} />
          <Route exact strict path="/Profile" component={Profile}/>
          <Route exact strict path="/Results" component={Results}/>
          <Route component={F4f} />
        </Switch>
      </Router>
    </React.Fragment>
  );
}

export default App;

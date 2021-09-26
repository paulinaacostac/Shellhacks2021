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
import Video from "./pages/video/video";
import Results2 from "./pages/results/results2";
import Results3 from "./pages/results/results3";
import Results4 from "./pages/results/results4";
import Results5 from "./pages/results/results5";

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
          <Route exact strict path='/Video' component={Video}/>
          <Route exact strict path='/Results2' component={Results2}/>
          <Route exact strict path='/Results3' component={Results3}/>
          <Route exact strict path='/Results4' component={Results4}/>
          <Route exact strict path='/Results5' component={Results5}/>
          <Route component={F4f} />
        </Switch>
      </Router>
    </React.Fragment>
  );
}

export default App;

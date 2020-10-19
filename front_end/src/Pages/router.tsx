import React, { Component, Fragment } from "react";
import { Route, Switch } from "react-router";
import axios from "axios";

import Header from "../Components/Header";
import Home from "./Home";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;

class Router extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Switch>
          <Route
            exact
            path="/"
            render={(routeProps: any) => <Home {...routeProps} />}
          />
          {/* <Route
            exact
            path="/login"
            render={(routeProps: any) => <Login {...routeProps} />} />
          <Route
            exact
            path="/register"
            render={(routeProps: any) => <Register {...routeProps} />} /> */}
        </Switch>
      </Fragment>
    );
  }
}

export default Router;

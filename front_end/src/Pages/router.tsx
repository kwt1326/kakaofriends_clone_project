import React, { Component, Fragment } from "react";
import { Route, Switch } from "react-router";
import axios from "axios";

import Header from "../Components/Header/header";
import Home from "./Home";
import Category from "../Components/Category/category";
import Info from "../Components/Info/info";
import Help from "../Components/Help/help";
import Mypage from "../Components/Mypage/mypage";
import Basket from "../Components/Basket/basket";

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
            path="/products/category"
            render={(routeProps: any) => <Category {...routeProps} />}
          />
          <Route
            exact
            path="/info/storeInfo"
            render={(routeProps: any) => <Info {...routeProps} />}
          />
          <Route
            exact
            path="/info/storeInfo"
            render={(routeProps: any) => <Info {...routeProps} />}
          />
          <Route
            exact
            path="/help"
            render={(routeProps: any) => <Help {...routeProps} />}
          />
          <Route
            exact
            path="/signin"
            render={(routeProps: any) => <Mypage {...routeProps} />}
          />
          <Route
            exact
            path="/basket/products"
            render={(routeProps: any) => <Basket {...routeProps} />}
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

import React, { Component, Fragment } from "react";
import { Route, Switch } from "react-router";
import axios from "axios";

import Header from "../Components/Header/header";
import Home from "./Home";
import Category from "./Category/category";
import Info from "./Info/info";
import Help from "./Help/help";
import Mypage from "./Mypage/mypage";
import Basket from "./Basket/basket";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;

class Router extends Component {
  render() {
    return (
      <Fragment>
        <Header />
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

        {/*
        <Route
          exact
          path="/"
          render={(routeProps: any) => <Home {...routeProps} />}
        />
        <Route
            exact
            path="/login"
            render={(routeProps: any) => <Login {...routeProps} />} />
          <Route
            exact
            path="/register"
            render={(routeProps: any) => <Register {...routeProps} />} /> */}
      </Fragment>
    );
  }
}

export default Router;

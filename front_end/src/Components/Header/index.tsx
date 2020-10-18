import React, { Component } from "react";
//import * as Router from "react-router";
import HeaderList from "./headerList";
/** @jsx jsx */
import { jsx, css } from "@emotion/core";
class Header extends Component {
  constructor(props: any) {
    super(props);
    //this.state = {};
  }

  render() {
    return (
      <div>
        <header
          css={css`
            display: flex;
            justify-content: space-around;
            align-items: center;
            background-color: yellow;
          `}
        >
          <div className="menu">
            <span>카테고리</span>
            <span>매장안내</span>
            <span>고객센터</span>
          </div>
          <h3>KAKAO FRIENDS</h3>
          <div
            css={css`
              display: flex;
            `}
          >
            <input type="search" placeholder="무엇을 찾으세요?" />
            <div>icon1</div>
            <div>icon2</div>
          </div>
        </header>
        <HeaderList />
      </div>
    );
  }
}

export default Header;

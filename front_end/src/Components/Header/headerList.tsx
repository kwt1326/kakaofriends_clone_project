import React from "react";
import Characters from "./characters";
/** @jsx jsx */
import { jsx, css } from "@emotion/core";
const HeaderList = () => {
  return (
    <section
      css={css`
        display: flex;
        background-color: brown;
        width: 500px;
        margin: 0.5em 5%;
      `}
    >
      <ul
        css={css`
          background-color: pink;
          flex: 1 1 55%;
          list-style: none;
          padding: 0;
        `}
      >
        <li>전체</li>
        <li>테마기획전</li>
        <li>토이</li>
      </ul>
      <div>
        <Characters />
      </div>
    </section>
  );
};

export default HeaderList;

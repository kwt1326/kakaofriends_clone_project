import React from "react";
/** @jsx jsx */
import { jsx, css } from "@emotion/core";
const Characters = () => {
  return (
    <section
      css={css`
        background-color: purple;
        flex: 1 1 45%;
        display: flex;
        flex-wrap: wrap;
        height: 100%;
        margin: 10px;
      `}
    >
      <div
        css={css`
          width: 50px;
          height: 50px;
          background-color: white;
          border-radius: 50%;
        `}
      ></div>
      <div
        css={css`
          width: 50px;
          height: 50px;
          background-color: white;
          border-radius: 50%;
        `}
      ></div>
      <div
        css={css`
          width: 50px;
          height: 50px;
          background-color: white;
          border-radius: 50%;
        `}
      ></div>
      <div
        css={css`
          width: 50px;
          height: 50px;
          background-color: white;
          border-radius: 50%;
        `}
      ></div>
      <div
        css={css`
          width: 50px;
          height: 50px;
          background-color: white;
          border-radius: 50%;
        `}
      ></div>
    </section>
  );
};

export default Characters;

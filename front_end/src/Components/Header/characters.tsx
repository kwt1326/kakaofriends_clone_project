import React from "react";
/** @jsx jsx */
import { jsx, css } from "@emotion/core";
import * as S from "./styles";
const Characters = () => {
  return (
    <S.CharSection>
      <S.CharDiv>1</S.CharDiv>
      <S.CharDiv>2</S.CharDiv>
      <S.CharDiv className="special">3</S.CharDiv>
    </S.CharSection>
  );
};

export default Characters;

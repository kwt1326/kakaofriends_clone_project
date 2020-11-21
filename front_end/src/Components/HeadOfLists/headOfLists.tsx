import React from "react";
import * as S from "./headOfLists_styles";

const HeadOfLists = ({ title }: any) => (
  <S.HeadDiv>
    <S.HeadTitle>{title}</S.HeadTitle>
  </S.HeadDiv>
);

export default HeadOfLists;

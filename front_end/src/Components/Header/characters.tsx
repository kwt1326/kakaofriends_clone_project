import React from "react";
import * as S from "./characters_styles";
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

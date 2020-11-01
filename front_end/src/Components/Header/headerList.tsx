import React from "react";
import Characters from "./characters";
import * as S from "./headerList_styles";

const HeaderList = () => {
  return (
    <S.Section>
      <S.CateUl>
        <S.CateList>전체</S.CateList>
        <S.CateList>테마기획전</S.CateList>
        <S.CateList>토이</S.CateList>
      </S.CateUl>
      <div>
        <Characters />
      </div>
    </S.Section>
  );
};

export default HeaderList;

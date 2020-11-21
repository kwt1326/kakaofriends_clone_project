import React, { useEffect } from "react";

import * as S from "./basket_styles";

const Basket = () => {
  return (
    <S.MainBody>
      <h1>장바구니</h1>
      <S.MainSection>
        <p>아직 관심 상품이 없네요!</p>
        <p> 귀여운 프렌즈 상품을 추천드릴게요</p>
        <S.Buttton>인기 상품 보기</S.Buttton>
      </S.MainSection>
    </S.MainBody>
  );
};

export default Basket;

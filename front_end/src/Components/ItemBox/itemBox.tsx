import React from "react";

import * as S from "./itemBox_styles";
const ItemBox = ({ item }: any) => (
  <S.itemBoxLi>
    <S.itemBoxImg
      src={`https://t1.daumcdn.net/friends/prod/product/${item.img_path}`}
      alt="products"
    />
    <S.itemBoxText>
      <span>{item.product_name}</span>
      <span>{item.price}</span>
    </S.itemBoxText>
  </S.itemBoxLi>
);

export default ItemBox;

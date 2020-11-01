import React, { useState } from "react";
//import * as Router from "react-router";
import HeaderList from "./headerList";
import * as S from "./header_styles";
import { Link } from "react-router-dom";
const imageMypage = require("../../assets/images/icon_header_mypage.png");
const imageBusket = require("../../assets/images/icon_header_basket.png");

const Header = () => {
  const [isHovered, SetIsHovered] = useState(false);
  const handleHover = () => {
    SetIsHovered(!isHovered);
  };
  return (
    <div>
      <S.MainHeader>
        <S.MainUl>
          <S.MainLi onMouseOver={handleHover}>
            <Link to="/products/category">카테고리 </Link>
          </S.MainLi>
          <S.MainLi>
            <Link to="/info/storeInfo">매장안내</Link>
          </S.MainLi>
          <S.MainLi>
            <Link to="/help">고객센터 </Link>
          </S.MainLi>
        </S.MainUl>
        <S.MainHome>KAKAO FRIENDS</S.MainHome>
        <S.MainInfo>
          <S.MainInput type="search" placeholder="무엇을 찾으세요?" />
          <S.MainIcon>
            <Link to="/signin">
              <S.MainIconImage src={imageMypage} />
            </Link>
          </S.MainIcon>
          <S.MainIcon>
            <Link to="/basket/products">
              <S.MainIconImage src={imageBusket} />
            </Link>
          </S.MainIcon>
        </S.MainInfo>
      </S.MainHeader>
      {isHovered && (
        <S.MainMenuDiv onMouseLeave={handleHover}>
          <HeaderList />
        </S.MainMenuDiv>
      )}
    </div>
  );
};

export default Header;

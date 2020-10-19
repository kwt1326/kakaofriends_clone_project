import React, { useState } from "react";
//import * as Router from "react-router";
import HeaderList from "./headerList";
/** @jsx jsx */
import { jsx, css } from "@emotion/core";
import * as S from "./styles";
//import LocalMallOutlinedIcon from "@material-ui/icons/LocalMallOutlined";
//import PermIdentityIcon from "@material-ui/icons/PermIdentity";

const Header = () => {
  const [isHovered, SetIsHovered] = useState(false);
  const handleHover = () => {
    SetIsHovered(!isHovered);
  };
  return (
    <div>
      <S.MainHeader>
        <S.MainUl>
          <S.MainLi onMouseOver={handleHover}>카테고리</S.MainLi>
          <S.MainLi>매장안내</S.MainLi>
          <S.MainLi>고객센터</S.MainLi>
        </S.MainUl>
        <S.MainHome>KAKAO FRIENDS</S.MainHome>
        <S.MainInfo>
          <S.MainInput type="search" placeholder="무엇을 찾으세요?" />
          <S.MainIcon>icon1</S.MainIcon>
          <S.MainIcon>icon2</S.MainIcon>
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

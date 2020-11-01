import React from "react";

import * as S from "./mypage_styles";
const Mypage = () => {
  return (
    <S.MainBody>
      <S.Head>
        <h2>오늘도 힘차게!!</h2>
        <h2>로그인을 해주세요</h2>
      </S.Head>
      <S.Section>
        <S.Button>카카오계정 로그인</S.Button>
        <ul>
          <h4>고객님께 안내 드립니다.</h4>
          <li>
            카카오프렌즈 고객님께 다양한 혜택을 드리고자 카카오프렌즈 회원가입
            서비스를 도입하게 되었습니다. 카카오프렌즈는 회원가입시 최소한의
            정보만 수집합니다.
          </li>
          <li>
            기존 구매 고객님께서는 카카오 계정 로그인 후 추가정보를 입력
            해주시면 구매이력과 주문 정보 등의 서비스를 동일하게 이용할 수
            있습니다.
          </li>
        </ul>
      </S.Section>
    </S.MainBody>
  );
};

export default Mypage;

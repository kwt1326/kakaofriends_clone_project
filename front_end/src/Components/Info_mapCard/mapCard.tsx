import React from "react";

import * as S from "./mapCard_styles";

const MapCard = () => {
  return (
    <S.Li>
      <S.Image
        alt="map"
        src="https://t1.kakaocdn.net/friends/prod/info/bg_storeInfo_gangnam_W.jpg"
      />
      <S.InfoSection>
        <section>글</section>
        <section>지도</section>
      </S.InfoSection>
    </S.Li>
  );
};

export default MapCard;

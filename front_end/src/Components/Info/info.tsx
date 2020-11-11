import React, { useEffect, useState } from "react";
import MapCard from "./mapCard";
import * as S from "./info_styles";
const Info = () => {
  let [index, setIndex] = useState(0);
  // useEffect(() => {
  //   const sliding = () =>
  //     setInterval(
  //       () => setIndex(index === 4 ? (index = 0) : (index += 1)),
  //       5000
  //     );
  //   sliding();
  //   return clearInterval(sliding());
  // }, []);

  const slideData: { id: string; src: string }[] = [
    {
      id: "1",
      src:
        "https://t1.kakaocdn.net/friends/prod/info/bg_storeInfo_01_W_180219.jpg",
    },
    {
      id: "2",
      src: "https://t1.kakaocdn.net/friends/prod/info/bg_storeInfo_02_W.jpg",
    },
    {
      id: "3",
      src: "https://t1.kakaocdn.net/friends/prod/info/bg_storeInfo_03_W.jpg",
    },
    {
      id: "4",
      src: "https://t1.kakaocdn.net/friends/prod/info/bg_storeInfo_04_W.jpg",
    },
    {
      id: "5",
      src: "https://t1.kakaocdn.net/friends/prod/info/bg_storeInfo_05_W.jpg",
    },
  ];

  return (
    <S.MainBody>
      <img alt="slide" src={slideData[0].src} width="100%" />
      <S.MainSection>
        <S.Ul>
          <MapCard key="1" />
        </S.Ul>
      </S.MainSection>
    </S.MainBody>
  );
};

export default Info;

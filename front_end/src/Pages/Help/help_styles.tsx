import styled from "@emotion/styled";

//이거 공통되는 section
export const MainSection = styled.section`
  width: 80%;
  margin: auto;
  background-color: coral;
`;

// 공통되는 Head
export const HeadDiv = styled.div`
  display: flex;
  align-items: center;
  height: 220px;
  background-image: url("https://t1.kakaocdn.net/friends/new_store/2.0/pc/banner_faq.png");
  background-position-x: center;
  background-position-y: center;
  background-size: contain;
  background-repeat: no-repeat;
`;
export const HeadTitle = styled.span`
  font-weight: bold;
  font-size: 36px;
  letter-spacing: -0.2px;
  margin-left: 30px;
  color: rgb(255, 255, 255);
`;

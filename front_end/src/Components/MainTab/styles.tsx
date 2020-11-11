import styled from "@emotion/styled";

export const Main = styled.div`
  width: 100%;
`;

export const Tab = styled.ul`
  display: flex;
  border-top: 1px solid rgb(227, 229, 232);
  border-bottom: 1px solid rgb(227, 229, 232);
  list-style: none;
  padding: 0 20px;
  margin: 0px auto;
  align-items: center;
  top: 60px;
  left: 0;
  width: 100%;
  background: rgb(255, 255, 255);
  text-align: center;
  justify-content: center;

  & > li {
    position: relative;
    width: 106px;
    height: 54px;
    font-size: 15px;
    line-height: 54px;
    position: relative;
    display: inline-block;
    text-align: center;
    list-style: none;
  }
`;

export const TabButton = styled.button`
  display: block;
  width: 100%;
  height: 100%;
  color: rgb(0, 0, 0);
  font-size: 16px;
  outline: none;
  border: 0 none;
  background-color: transparent;
  cursor: pointer;
`;

export const Hr = styled.hr`
  height: 3px;
  width: 18vw;
  max-width: 60px;
  margin-top: -2px;
  text-align: center;
  border-width: 3px 0px 0px;
  border-right-style: initial;
  border-bottom-style: initial;
  border-left-style: initial;
  border-right-color: initial;
  border-bottom-color: initial;
  border-left-color: initial;
  border-image: initial;
  border-top-style: solid;
  border-top-color: rgb(48, 48, 48);
  display: block;
  color: red;
`;

export const itemWrap = styled.div`
  width: 80%;
  margin: auto;
  margin-top: 50px;
`;

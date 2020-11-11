import styled from "@emotion/styled";

//index.jsx - Header Components
export const MainHeader = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 3em;
`;
export const MainUl = styled.ul`
  list-style: none;
  display: flex;
  padding: 0;
  margin: 0;
`;
export const MainLi = styled.li`
  padding: 1em;
  align-items: center;

  & > a {
    text-decoration: none;
    color: black;
  }
`;

export const MainInfo = styled.div`
  display: flex;
`;
export const MainIcon = styled.div`
  padding: 0.5em;
`;
export const MainIconImage = styled.img`
  width: 18px;
  height: 19px;
`;
export const MainHome = styled.h3`
  background-color: black;
  color: white;
  padding: 0.3em 0.5em;
  border-radius: 1.2em;
  margin: 0.5em;
`;
export const MainInput = styled.input`
  padding: 0.5em;
  border-radius: 0.5em;
  margin-right: 0.5em;
  outline: 0;
  border: 0.5px solid lightgray;
`;
export const MainMenuDiv = styled.div`
  position: absolute;
  top: 50px;
`;

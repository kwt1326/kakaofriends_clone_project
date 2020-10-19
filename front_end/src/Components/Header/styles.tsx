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

//HeaderList Components
export const Section = styled.section`
  display: flex;
  width: 500px;
  top: 40px;
  margin: 0 1.5rem;
  background-color: white;
  border-radius: 5px;
  box-shadow: 4px 7px 24px -12px rgba(122, 122, 122, 1);
`;
export const CateUl = styled.ul`
  border-right: 0.5px solid lightgrey;
  flex: 1 1 55%;
  list-style: none;
  padding: 0 1em;
`;
export const CateList = styled.li`
  padding: 0.5em;
`;

//Character Components
export const CharSection = styled.section`
  background-color: purple;
  flex: 1 1 45%;
  display: flex;
  flex-wrap: wrap;
  margin: 10px;
`;

export const CharDiv = styled.div`
  width: 50px;
  height: 50px;
  background-color: white;
  border-radius: 50%;
  margin: 0.2em;
  &.special {
    background-color: orange;
  }
`;

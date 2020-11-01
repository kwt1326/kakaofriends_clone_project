import styled from "@emotion/styled";
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

import styled from "@emotion/styled";

export const MainBody = styled.section`
  display: flex;
  flex-direction: column;
  margin: auto;
  width: 80%;
`;

export const MainSection = styled.section`
  border-top: 1px solid lightgray;
  border-bottom: 1px solid lightgray;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-top: 3em;
  padding-bottom: 2em;

  color: rgb(154, 154, 158);
`;

export const Buttton = styled.button`
  border-radius: 4px;
  background-color: rgb(60, 64, 75);
  cursor: pointer;
  outline: 0;
  color: white;
`;

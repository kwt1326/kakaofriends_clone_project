import React from "react";
import Characters from "./characters";
import * as S from "./headerList_styles";

const HeaderList = (props: any) => {
  const queryParse = () => {
    const base = props.props.location.search;
    const params = base.split("?")[1]?.split("&");
    params.map((param: string) => {
      const parsedArr = param.split("=");
      console.log({ [parsedArr[0]]: parsedArr[1] });
    });
  };

  return (
    <S.Section>
      <S.CateUl>
        <S.CateList
          onClick={() => {
            queryParse();
            props.props.history.push();
          }}
        >
          전체
        </S.CateList>
        <S.CateList>테마기획전</S.CateList>
        <S.CateList>토이</S.CateList>
      </S.CateUl>
      <div>
        <Characters />
      </div>
    </S.Section>
  );
};

export default HeaderList;

import { css } from "@emotion/core";
import React, { FC, useState } from "react";

import * as S from "./styles";
import All from "./tabs/All";
import Home from "./tabs/Home";
import Hot from "./tabs/Hot";
import New from "./tabs/New";
import Sale from "./tabs/Sale";

const MainTab: FC = () => {
  const [active, setActive] = useState(0);
  const tabActiveChange = (idx: number) => {
    setActive(idx);
  };

  return (
    <>
      <S.Main>
        <S.Tab>
          {tabName.map((name, idx) => (
            <li key={idx} onClick={() => tabActiveChange(idx)}>
              <S.TabButton>{name}</S.TabButton>
              {active === idx && <S.Hr />}
            </li>
          ))}
        </S.Tab>
      </S.Main>
      <S.itemWrap>{tabArr[active]}</S.itemWrap>
    </>
  );
};

export default MainTab;

const tabName = ["홈", "세일", "신상", "인기", "전체"];
const tabArr: any = {
  0: <Home />,
  1: <Sale />,
  2: <New />,
  3: <Hot />,
  4: <All />,
};

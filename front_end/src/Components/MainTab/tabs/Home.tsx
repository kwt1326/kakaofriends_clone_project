import React from "react";
import * as S from "./styles";
import Dummy from "dummyjs";

import Masonry from "react-masonry-css";

const Home = () => {
  const items = new Array(40).fill([]).map((item, i) => {
    return (
      <S.ItemWrap key={i}>
        <div>
          <a>
            <div>
              <img src={Dummy.src(500, 400)} style={{ width: "100%" }} />
            </div>
          </a>
          <a>
            <div>{Dummy.text("20,60")}</div>
          </a>
        </div>
      </S.ItemWrap>
    );
  });

  return (
    <S.HomeWarp>
      <Masonry
        breakpointCols={3}
        className="my-masonry-grid"
        columnClassName="my-masonry-grid_column"
      >
        {items}
      </Masonry>
    </S.HomeWarp>
  );
};

export default Home;

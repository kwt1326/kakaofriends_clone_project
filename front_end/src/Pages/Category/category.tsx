import React, { useEffect, useState } from "react";
import HeadOfLists from "../../Components/HeadOfLists/headOfLists";
import ItemBox from "../../Components/ItemBox/itemBox";
import { axiosApiCall, callApiProps } from "../../utils/callApi";
import * as S from "./category_styles";

const Category = () => {
  const [list, setList] = useState<Array<any>>([]);
  const applyProduct = async () => {
    const page = 1;
    const perPage = 20;
    const data: callApiProps = {
      method: "GET",
      url: `api/product?page=${page}&per_page=${perPage}`,
    };
    const response = await axiosApiCall(data);
    console.log(response);
    setList(response.data);
    console.log(response.data);
  };

  useEffect(() => {
    applyProduct();
  }, []);
  return (
    <S.itemSection>
      <HeadOfLists title={"전체"} />
      <S.itemUl>
        {list.map((item) => (
          <ItemBox key={item.id} item={item} />
        ))}
      </S.itemUl>
    </S.itemSection>
  );
};
export default Category;

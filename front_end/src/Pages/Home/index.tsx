import React, { useEffect } from "react";
import { axiosApiCall, callApiProps } from "../../utils/callApi";
import MainTab from "../../Components/MainTab";

const Home = (props: any) => {
  // @callapi 예시
  // const applyProduct = async () => {
  //   const data: callApiProps = {
  //     method: 'POST',
  //     url: 'api/product',
  //     body: {
  //       product_name: 'test_from_front',
  //       category: 'others',
  //       price: '20000',
  //     }
  //   }
  //   const response = await axiosApiCall(data);
  //   console.log(response);
  // }

  // useEffect(() => {
  //   applyProduct()
  // })

  return <MainTab />;
};

export default Home;

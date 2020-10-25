import React, { useEffect } from 'react';
import { axiosApiCall, callApiProps } from '../../utils/callApi'

const Home = (props: any) => {
  const applyProduct = async () => {
    const data: callApiProps = {
      method: 'POST',
      url: 'api/product',
      body: {
        product_name: 'test_from_front',
        category: 'others',
        price: '20000',
      }
    }
    const response = await axiosApiCall(data);
    console.log(response);
  }

  useEffect(() => {
    applyProduct()
  })

  return (
    <h1>hello world!</h1>
  )
}

export default Home;
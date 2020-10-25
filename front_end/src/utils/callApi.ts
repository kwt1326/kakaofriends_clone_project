import axios, { AxiosRequestConfig } from 'axios'
import { serverUrl } from '../constant/config';
// import getCookie from './getCookie'

export interface callApiProps {
  method: AxiosRequestConfig["method"],
  url: string,
  body?: Object,
  headers?: Object,
}

export const axiosApiCall = (data: callApiProps) => {
  try {
    const requestConfig: AxiosRequestConfig = {
      method: data.method,
      url: `${serverUrl()}${data.url}`,
      data: data.body || {},
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',  
        // 'X-CSRFToken': csrfToken, // 필요할 경우 해제
        ...data.headers,
      }
    }

    return axios(requestConfig
    ).then(response => {
      return response;
    }).catch(err => {
      return err;
    })
  } catch (err) {
    console.log(`failed request: ${serverUrl()}${data.url}`)
    return err;
  }
}
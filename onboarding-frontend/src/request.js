import axios from "axios";

const myAxios = axios.create({
  baseURL: "http://34.134.231.140:5000",
  timeout: 10000,
});

myAxios.interceptors.request.use(
  function (config) {
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  function (response) {
    console.log(response);
  },
  function (error) {
    return Promise.reject(error);
  }
);

export default myAxios;

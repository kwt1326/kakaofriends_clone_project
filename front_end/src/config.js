/* eslint-disable import/prefer-default-export */
export function serverUrl() {
  switch (process.env.NODE_ENV) {
    case "production":
      return "";
    case "development":
    default:
      return "http://193.122.107.208/";
  }
}

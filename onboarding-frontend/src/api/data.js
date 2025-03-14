import myAxios from "@/request";

/**
 * Collect states uv index
 */
export const getStatesUvIndex = async () => {
  try {
    const res = await myAxios.request({
      url: "/table/data",
      method: "GET",
    });
    return res.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

/**
 *
 * @param states
 * @param city
 * @param suburb
 * @returns {Promise<*|null>}
 */
export const getUvIndexByLocation = async ({ suburb }) => {
  try {
    const res = await myAxios.request({
      url: "/uv-index",
      method: "GET",
      params: { suburb }, // 直接传递对象，Axios 会自动转换为查询参数
    });

    return res?.data || null;
  } catch (error) {
    console.error("Error fetching UV index data:", error);
    return null;
  }
};

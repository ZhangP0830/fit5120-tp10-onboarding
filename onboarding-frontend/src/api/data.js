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

export const getSkinCancerIncidenceData = async () => {
  try {
    const response = await myAxios.get("/api/skin_cancer/incidence_rate");
    console.log("API 响应数据:", response); // ✅ 确保 Axios 收到正确的 JSON
    return response.data; // ✅ 只返回 data 部分，避免 Vue 解析失败
  } catch (error) {
    console.error("获取皮肤癌数据失败:", error);
    return [];
  }
};

export const getSkinCancerMortalityData = async () => {
  try {
    const response = await myAxios.get("/api/skin_cancer/mortality_rate");
    return response.data;
  } catch (error) {
    return [];
  }
};

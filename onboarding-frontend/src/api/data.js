import myAxios from "@/request";

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

export const getUvIndexByLocation = async ({ suburb }) => {
  try {
    const res = await myAxios.request({
      url: "/uv-index",
      method: "GET",
      params: { suburb },
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
    return response.data;
  } catch (error) {
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

export const fetchLocationData = async (suburb) => {
  try {
    const response = await myAxios.get(`/api/select_location?suburb=${suburb}`);
    console.log("API response:", response.data);

    if (
      response.data &&
      response.data.lon !== undefined &&
      response.data.lat !== undefined
    ) {
      return {
        suburb,
        lat: response.data.lat,
        lon: response.data.lon,
      };
    } else {
      console.warn("Location data not found:", response.data.error);
      return null;
    }
  } catch (error) {
    console.error(
      "Error fetching location data:",
      error.response ? error.response.data : error.message
    );
    return null;
  }
};

export const getWeatherForecast = async (lat, lon) => {
  try {
    const response = await myAxios.get(
      `/api/heat_forecast?lat=${lat}&lon=${lon}`
    );

    return response.data.map((d) => ({
      time: new Date(d.time * 1000).toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
      temperature: d.temperature,
    }));
  } catch (error) {
    console.error("Failed to fetch weather data:", error);
    return [];
  }
};

export const getUvIndex = async (lat, lon) => {
  try {
    const response = await myAxios.get(`/api/uv-index?lat=${lat}&lon=${lon}`);

    if (response.data["uv_index"] !== undefined) {
      return response.data["uv_index"];
    } else {
      console.warn("No UV Index data found.");
      return null;
    }
  } catch (error) {
    console.error("Failed to fetch weather data:", error);
    return [];
  }
};

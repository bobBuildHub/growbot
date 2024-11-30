import axios from "axios";

// Mock axios for test
jest.mock("axios");
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe("API Integration Tests", () => {
  it("fetches data successfully", async () => {
    const mockResponse = { data: { message: "success" } };
    mockedAxios.get.mockResolvedValueOnce(mockResponse);

    const response = await axios.get("/api/test");
    expect(response.data.message).toBe("success");
  });

  it("handles API errors", async () => {
    mockedAxios.get.mockRejectedValueOnce(new Error("Network Error"));

    try {
      await axios.get("/api/test");
    } catch (error) {
      expect(error).toEqual(new Error("Network Error"));
    }
  });
});

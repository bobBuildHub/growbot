module.exports = {
  testEnvironment: "jsdom",
  transform: {
    "^.+\\.(ts|tsx|js|jsx)$": "babel-jest",
  },
  moduleNameMapper: {
    "^axios$": "axios",
  },
  moduleDirectories: ["node_modules", "src"],
};

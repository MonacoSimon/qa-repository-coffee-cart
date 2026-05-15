const { defineConfig } = require("cypress");

module.exports = defineConfig({
  allowCypressEnv: false,

  // Deshabilitar capturas y videos
  screenshotOnRunFailure: false,
  video: false,
  videoUploadOnPasses: false,

  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
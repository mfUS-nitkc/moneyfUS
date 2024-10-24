// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },

  alias: {
    "~": "./src",
    "public": "./public"
  },

  srcDir: "src/",
  modules: ["@nuxtjs/storybook"]
})

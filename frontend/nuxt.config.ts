// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, {transformAssetUrls} from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },

  alias: {
    "~": "./src",
    "public": "./public"
  },

  srcDir: "src/",
  modules: [(_options, nuxt) => {
    nuxt.hooks.hook('vite:extendConfig', (config) => {
      config.plugins.push(vuetify({autoImport: true}))
    })
  },"@nuxtjs/storybook"],
  build: {
    transpile: ['vuetify'],
  },
  vite: {
    vue: {
      template: {
        transformAssetUrls
      }
    }
  }
})

// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, {transformAssetUrls} from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.API_BASE_URL || 'http://localhost:8000/api/v1',
    }
  },
  alias: {
    "~": "./src",
    "public": "./public"
  },

  srcDir: "src/",
  modules: [(_options, nuxt) => {
    nuxt.hooks.hook('vite:extendConfig', (config) => {
      config.plugins.push(vuetify({autoImport: true}))
    })
  },
  '@pinia/nuxt',
  () => { process.env.NODE_ENV === 'DEVELOP' ? "@nuxtjs/storybook" : ''},
],
  build: {
    transpile: ['vuetify'],
  },
  vite: {
    vue: {
      template: {
        transformAssetUrls
      }
    },
    server: {
      watch: {
        usePolling: true
      }
    }
  }
})

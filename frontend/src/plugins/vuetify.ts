// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css'

import 'vuetify/styles'
import colors from 'vuetify/util/colors'
import { createVuetify } from 'vuetify'

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    theme: {
      themes: {
        light: {
          dark: false,
          colors: {
            primary: colors.blue.lighten4,
            secondary: colors.teal.lighten1,
          }
        },
      },
    },
  })
  app.vueApp.use(vuetify)
})


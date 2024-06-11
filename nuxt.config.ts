// https://nuxt.com/docs/api/configuration/nuxt-config
import { resolve } from "path";
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ["~/assets/main.scss"],
  alias: {
    "@": resolve(__dirname, "/"),
  },
  modules: ["@nuxt/ui", "@nuxtjs/tailwindcss", "@nuxt/test-utils/module"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
});

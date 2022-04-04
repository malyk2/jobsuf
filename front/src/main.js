import { createApp } from "vue";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/tailwind.css";
import { can } from "@/directives/can";

// mouting point for the whole app

import App from "@/App.vue";
import store from './store'
// routes
import router from './router'

const app = createApp(App)
app.directive('can', can)
app.use(router).use(store).mount("#app");
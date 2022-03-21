import { createApp } from "vue";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/tailwind.css";


// mouting point for the whole app

import App from "@/App.vue";
import store from './store'
// routes
import router from './router'

createApp(App).use(router).use(store).mount("#app");

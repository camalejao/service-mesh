import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import Products from './components/Products'
import Customers from './components/Customers'
import Orders from './components/Orders'
import HelloWorld from './components/HelloWorld'
import 'bootstrap/dist/css/bootstrap.min.css'

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/', component: HelloWorld },
        { path: '/products', component: Products },
        { path: '/customers', component: Customers },
        { path: '/orders', component: Orders },
    ]
})

const app = createApp(App)

app.use(router)
app.mount('#app')

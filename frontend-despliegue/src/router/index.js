
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/hello',
            name: 'hello',
            // Carga diferida: solo descarga esta vista cuando se visita
            component: () => import('@/views/HelloView.vue'),
        },
    ],
})

export default router

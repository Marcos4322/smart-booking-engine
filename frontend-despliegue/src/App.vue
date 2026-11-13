
<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <header class="app-header">
        <nav>
            <RouterLink to="/">Inicio</RouterLink>
            <RouterLink to="/hello">Hello</RouterLink>
        </nav>
    </header>

    <main class="app-main">
        <RouterView />
    </main>
</template>


<style scoped>
.app-header {
    padding: var(--space-m) var(--space-l);
    background: var(--color-primary);
}

nav {
    display: flex;
    align-items: center;
    gap: var(--space-l);
}

nav a {
    padding: var(--space-s) var(--space-m);
    border-radius: var(--radius-md);
    color: var(--color-on-primary);
    font-family: var(--font-family);
    font-size: var(--font-size-body);
    font-weight: 500;
    text-decoration: none;
    transition: background-color 0.2s ease;
}

nav a:hover {
    background: var(--color-primary-dark);
}

nav a.router-link-exact-active {
    background: var(--color-primary-dark);
    text-decoration: underline;
    text-underline-offset: 4px;
}

.app-main {
    padding: var(--space-l);
}
</style>


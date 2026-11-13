
<script setup>
import { ref } from 'vue'
import { getHello } from '@/services/helloService'
import HelloResult from '@/components/HelloResult.vue'

// Estado de la vista
const name = ref('')
const message = ref('')
const error = ref('')
const loading = ref(false)

// Acción: se ejecuta al enviar el formulario
async function saludar() {
    loading.value = true
    error.value = ''
    message.value = ''

    try {
        message.value = await getHello(name.value)
    } catch (e) {
        error.value = 'No se ha podido contactar con el backend. ¿Está arrancado?'
        console.error(e)
    } finally {
        loading.value = false
    }
}
</script>

<template>
    <section class="hello">
        <h1>Hello World</h1>

        <form class="hello__form" @submit.prevent="saludar">
            <label for="name">Tu nombre (opcional)</label>
            <input id="name" v-model="name" type="text" placeholder="Ana" />
            <button type="submit" :disabled="loading">
                {{ loading ? 'Cargando…' : 'Saludar' }}
            </button>
        </form>

        <HelloResult :message="message" :error="error" />
    </section>
</template>


<style scoped>
.hello h1 {
    font-family: var(--font-family-heading);
    font-size: var(--font-size-title);
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.03em;
    color: var(--color-text-main);
}

.hello__form {
    display: flex;
    flex-direction: column;
    gap: var(--space-s);
    max-width: 320px;
}

label {
    color: var(--color-text-main);
    font-size: var(--font-size-body);
    font-weight: 500;
}

input {
    height: 42px;
    padding: var(--space-s) var(--space-m);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    background: var(--color-surface);
    color: var(--color-text-main);
    font: inherit;
}

input:focus-visible {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(36, 92, 79, 0.12);
}

button {
    padding: var(--space-s) var(--space-l);
    border: none;
    border-radius: var(--radius-md);
    background: var(--color-primary);
    color: var(--color-on-primary);
    font: inherit;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

button:hover:not(:disabled) {
    background: var(--color-primary-dark);
}

button:disabled {
    opacity: 0.6;
    cursor: wait;
}
</style>


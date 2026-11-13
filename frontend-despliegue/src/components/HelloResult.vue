
<script setup>
defineProps({
    message: { type: String, default: '' },
    error: { type: String, default: '' },
})
</script>

<template>
    <p v-if="error" class="result result--error" role="alert">{{ error }}</p>
    <p v-else-if="message" class="result" aria-live="polite">{{ message }}</p>
</template>

<style scoped>
.result {
    margin-top: var(--space-l);
    padding: var(--space-m);
    border-radius: var(--radius-m);
    font-size: var(--font-size-title);
}

.result--error {
    color: var(--color-error);
    font-size: var(--font-size-body);
}
</style>

<script setup>
import { ref, onMounted } from 'vue'

const estadoBackend = ref('Conectando con el backend...')
const errorConexion = ref(false)

onMounted(async () => {
  try {
    const respuesta = await fetch('http://localhost:3000/api/health')
    const datos = await respuesta.json()
    // Acepta 'mensaje', 'message' o pinta el JSON completo para que nunca quede vacío
    estadoBackend.value = datos.mensaje || datos.message || `Conectado: ${JSON.stringify(datos)}`
    errorConexion.value = false
  } catch (error) {
    estadoBackend.value = 'Error al conectar con el Backend en http://localhost:3000'
    errorConexion.value = true
  }
})
</script>

<template>
  <main style="min-height: 100vh; background-color: #0f172a; color: white; display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: sans-serif; padding: 1.5rem;">
    <div style="max-width: 450px; width: 100%; background-color: #1e293b; padding: 2rem; border-radius: 1rem; border: 1px solid #334155; text-align: center; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);">
      <h1 style="font-size: 2rem; font-weight: bold; color: #818cf8; margin-bottom: 0.5rem;">BookFlow</h1>
      <p style="color: #94a3b8; font-size: 0.875rem; margin-bottom: 1.5rem;">Boilerplate Hito 1 - Prueba de Comunicación Front/Back</p>
      
      <!-- Tarjeta con estilos en línea asegurados -->
      <div 
        :style="{
          backgroundColor: errorConexion ? '#450a0a' : '#064e3b',
          borderColor: errorConexion ? '#ef4444' : '#10b981',
          color: errorConexion ? '#fecaca' : '#a7f3d0'
        }"
        style="padding: 1rem; border-radius: 0.5rem; border-width: 1px; border-style: solid; font-size: 0.95rem; font-weight: 500;"
      >
        {{ estadoBackend }}
      </div>
    </div>
  </main>
</template>
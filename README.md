# Motor de Citas Inteligente (BookFlow)

## Descripción
BookFlow es mi propuesta para una plataforma web de reservas diseñada para gestionar la disponibilidad de servicios de forma dinámica. El problema principal que quiero resolver es evitar los huecos fijos y los solapamientos; mi sistema calculará matemáticamente los espacios libres cruzando la duración del servicio con el calendario y descansos del profesional. Está dirigido a clínicas o negocios basados en citas, ofreciendo un panel de administración para los trabajadores y una interfaz intuitiva para que los clientes reserven en tiempo real.

## Tecnologías

### Guía de estilo / diseño
Voy a utilizar **Tailwind CSS**. 
*Justificación:* Lo he elegido porque es el framework de utilidades CSS más demandado en la actualidad. Me permite un desarrollo de interfaces rápido y moderno sin tener que abandonar mis archivos de componentes, asegurando un diseño responsive con una curva de aprendizaje muy ágil.

### Backend
Emplearé **Node.js con el framework Express**.
*Justificación:* Express es un estándar en la industria por su ligereza y flexibilidad para construir APIs RESTful. Además, al usar JavaScript en el backend, unifico el lenguaje de programación con el frontend, lo que me reduce la curva de aprendizaje y optimiza el manejo de la asincronía necesaria para programar mi algoritmo de disponibilidad.

### Frontend
Desarrollaré una SPA (Single Page Application) usando **Vue 3** junto con el empaquetador **Vite**.
*Justificación:* Me decanto por Vue porque destaca por su excelente curva de aprendizaje, código limpio y su reactividad intuitiva, lo que me permitirá desarrollar el panel interactivo del calendario de forma rápida. Utilizaré la Composition API por ser el estándar moderno del framework. Vite lo he elegido por su extrema velocidad de compilación en el entorno de desarrollo.

### Base de datos
Voy a usar **MySQL** (Base de datos relacional) desplegada mediante **Docker**.
*Justificación:* Al ser un sistema de reservas, mis datos van a estar fuertemente estructurados y relacionados (Usuarios -> Citas -> Servicios). Una base de datos relacional me garantiza la integridad referencial y me permite realizar consultas complejas para calcular los huecos disponibles (previniendo concurrencia). Además, he decidido usar Docker para levantar la base de datos porque me asegura un entorno de desarrollo aislado, reproducible y muy fácil de configurar para el profesor o para mí en otra máquina, sin necesidad de instalar el motor de MySQL directamente en el sistema operativo.

### Documentación
*   **Markdown:** Para la documentación interna del repositorio (este mismo archivo y la memoria técnica en `docs/instalacion.md`).
*   **Swagger / OpenAPI:** Para documentar los endpoints de mi API REST. 
*Justificación:* Swagger me va a generar una interfaz interactiva donde el profesor podrá probar visualmente las peticiones a mi backend (rutas GET/POST) comprobando el correcto funcionamiento de la API.

### Librerías y dependencias
*   **Autenticación:** JWT (JSON Web Tokens) para mantener sesiones seguras.
*   **Calendario UI:** Librerías como V-Calendar o FullCalendar-Vue para la visualización del panel.
*   **Asistente de Desarrollo:** Uso de agentes de IA de código abierto (como OpenCode) como apoyo para la asistencia en refactorización y agilización de scripts de configuración.

### Control de versiones
Voy a utilizar **Git** y **GitHub**.
*   **Flujo de trabajo:** Al tratarse de un proyecto desarrollado de forma individual, sigo un flujo directo sobre la rama principal `main`, realizando commits frecuentes, atómicos y bien delimitados para cada avance o funcionalidad implementada.
*   **Convención de commits:** Adoptaré *Conventional Commits* (ej. `feat: añade lógica de fechas`, `fix: corrige solapamiento`, `chore: actualiza dependencias`) para mantener un historial limpio, claro y profesional.

---

## 🚀 Instrucciones para Levantar el Proyecto en Local

Sigue estos 7 pasos en orden para arrancar el entorno completo en local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Marcos4322/smart-booking-engine.git](https://github.com/Marcos4322/smart-booking-engine.git)
cd smart-booking-engine
```

### 2. Configurar las variables de entorno
Copia la plantilla de ejemplo para crear tu archivo `.env` local:
```bash
cp .env.example .env
```
*Variables a configurar:*
* `PORT`: Puerto en el que correrá el backend de Express (por defecto: `3000`).
* `VITE_API_URL`: URL base de la API consumida por el cliente (`http://localhost:3000/api`).

### 3. Instalar dependencias
Instala los paquetes en ambas partes del proyecto:
```bash
# Dependencias del backend
cd backend
npm install
cd ..

# Dependencias del frontend
cd frontend
npm install
cd ..
```

### 4. Preparar la base de datos
*En este Hito 1 inicial no se requiere persistencia de datos activa ni migraciones.* La base de datos MySQL se desplegará mediante Docker en los siguientes hitos de lógica de negocio.

### 5. Arrancar el Backend
En una terminal situada en la raíz del proyecto:
```bash
cd backend
node index.js
```
El servidor quedará disponible en: `http://localhost:3000`.

### 6. Arrancar el Frontend
En una segunda terminal situada en la raíz del proyecto:
```bash
cd frontend
npm run dev
```
La interfaz quedará disponible en: `http://localhost:5173`.

### 7. Comprobar funcionamiento
1. Abre en tu navegador `http://localhost:3000/api/health` para ver la respuesta JSON directa del servidor (`status: OK`).
2. Abre `http://localhost:5173` en el navegador: la aplicación de Vue cargará y mostrará una tarjeta verde con el mensaje recibido desde el backend en tiempo real, demostrando la comunicación bidireccional.
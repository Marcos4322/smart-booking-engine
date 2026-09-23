# Motor de Citas Inteligente (BookFlow)

## Descripción
BookFlow es una plataforma web de reservas diseñada para gestionar la disponibilidad de servicios de forma dinámica. El problema principal que resuelve es evitar los huecos fijos y los solapamientos; el sistema calcula matemáticamente los espacios libres cruzando la duración del servicio con el calendario y descansos del profesional. Está dirigido a clínicas o negocios basados en citas, ofreciendo un panel de administración y una interfaz intuitiva para clientes.

## Tecnologías

### Guía de estilo / diseño
Se utilizará **Tailwind CSS**. 
*Justificación:* Es el framework de utilidades CSS más demandado en la actualidad. Permite un desarrollo de interfaces rápido y moderno sin tener que abandonar el archivo de componentes, asegurando un diseño responsive con una curva de aprendizaje ágil.

### Backend
Se empleará **Node.js con el framework Express**.
*Justificación:* Express es un estándar en la industria por su ligereza y flexibilidad para construir APIs RESTful. Al usar JavaScript en el backend, se unifica el lenguaje de programación con el frontend, reduciendo la curva de aprendizaje y optimizando el manejo de la asincronía necesaria para los cálculos de disponibilidad.

### Frontend
Se desarrollará como una SPA (Single Page Application) usando **Vue 3** junto con el empaquetador **Vite**.
*Justificación:* Vue destaca por su excelente curva de aprendizaje, código limpio y su reactividad intuitiva, lo que permitirá desarrollar el panel interactivo del calendario de forma rápida. Se utilizará la Composition API por ser el estándar moderno del framework. Vite se elige por su extrema velocidad de compilación en el entorno de desarrollo.

### Base de datos
Se utilizará **MySQL** (Base de datos relacional).
*Justificación:* Al tratarse de un sistema de reservas, los datos están fuertemente estructurados y relacionados (Usuarios -> Citas -> Servicios). Una base de datos relacional garantiza la integridad referencial y permite realizar consultas complejas para calcular los huecos disponibles (previniendo concurrencia).

### Documentación
*   **Markdown:** Para la documentación interna del repositorio.
*   **Swagger / OpenAPI:** Para documentar los endpoints de la API REST. 
*Justificación:* Swagger genera una interfaz interactiva donde el equipo y los evaluadores pueden probar visualmente las peticiones al backend (rutas GET/POST) asegurando el correcto funcionamiento de la API.

### Librerías y dependencias
*   **Autenticación:** JWT (JSON Web Tokens) para mantener sesiones seguras.
*   **Calendario UI:** Librerías como V-Calendar o FullCalendar-Vue para la visualización del panel.
*   **Asistente de Desarrollo:** Uso de agentes de IA de código abierto (como OpenCode) para la asistencia en refactorización y agilización de scripts de configuración.

### Control de versiones
Se utilizará **Git** y **GitHub**.
*   **Flujo de trabajo:** Modelo basado en *Feature Branches* (rama `main` y ramas `feature/nombre-funcionalidad` para cada avance).
*   **Convención de commits:** Se adoptará *Conventional Commits* (ej. `feat: añade lógica de fechas`, `fix: corrige solapamiento`) para mantener un historial limpio y profesional.

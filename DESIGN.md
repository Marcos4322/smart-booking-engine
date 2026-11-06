# DESIGN.MD — BOOKFLOW DESIGN SYSTEM SPECIFICATION

> **Versión:** 1.0.0  
> **Producto:** BookFlow (SaaS de Gestión de Citas, Agendas y Servicios)  
> **Stack frontend de referencia:** React 18+, CSS Modules / Tailwind CSS, Lucide Icons  
> **Estado:** Documentación oficial lista para producción  

---

## 1. DESCRIPCIÓN DEL PRODUCTO

**BookFlow** es una plataforma SaaS de gestión integral de reservas, citas y agendas diseñada para profesionales independientes, especialistas (salud, bienestar, consultoría, estética, servicios legales) y negocios de servicios.

### Propuesta de Valor y Principios de Diseño
1. **Calma & Organización:** La gestión de agenda suele generar estrés tanto al profesional como al cliente. La interfaz reduce la carga cognitiva mediante espacios generosos, tipografía editorial y colores orgánicos.
2. **Cero Azul Genérico ("Anti-Generic SaaS"):** BookFlow rompe con los paneles SaaS estándar de tonos azules fríos. Adopta una paleta inspirada en papelería premium, botánica y cuero artesanal (*Verde Bosque, Marfil y Cobre*).
3. **Claridad Operativa de Tres Vistas:**
   - **Administrador:** Control total de negocio, métricas clave, servicios, equipo y facturación.
   - **Profesional:** Foco diario en agenda, detalle de citas y validación ágil mediante código QR.
   - **Cliente:** Experiencia de autoservicio fluida, optimizada para móviles, sin fricciones.

---

## 2. IDENTIDAD VISUAL Y LOGOTIPO

### Isotipo & Logomarca
- **Concepto:** Fusión de un folio/calendario con una curva fluida continua que representa el "Flow" (flujo de tiempo armónico).
- **Construcción:**
  - Letra `B` estilizada con dos bucles suaves que evocan ranuras de calendario continuo o dos tarjetas de citas superpuestas.
  - Símbolo secundario: Indicador de punto de confirmación en color cobre (#B7794B).
- **Tipografía de marca:** `Manrope` / `Inter` Bold con interletrado `-0.02em` y `Flow` en peso Medium.
- **Zona de exclusión:** Mínimo `1x` del ancho del isotipo alrededor de la marca.
- **Uso en fondos:**
  - Fondo Marfil (`#F7F5F0`): Isotipo Verde Bosque con detalle Cobre, texto Carbón Verdoso.
  - Fondo Verde Bosque (`#245C4F`): Isotipo Blanco con acento Cobre, texto Blanco.

---

## 3. PALETA DE COLORES Y DESIGN TOKENS

### Paleta Primaria
| Nombre Token | HEX | Aplicación |
|---|---|---|
| `color-primary` (Verde Bosque) | `#245C4F` | Acciones principales, botones primarios, marca activa, bordes focales |
| `color-primary-dark` (Verde Oscuro) | `#19483E` | Hover de botones primarios, encabezados oscuros, sidebar activo |
| `color-primary-soft` (Verde Suave) | `#EAF2ED` | Fondos de badges de estado, filas seleccionadas, contenedores secundarios |
| `color-background` (Marfil) | `#F7F5F0` | Fondo general de la aplicación, canvas de dashboard |
| `color-surface` (Blanco Puro) | `#FFFFFF` | Tarjetas, modales, formularios, dropdowns, tablas |
| `color-accent` (Cobre) | `#B7794B` | Detalles de atención, botones secundarios destacados, badges VIP, acentos de calendario |
| `color-accent-hover` (Cobre Oscuro) | `#9E643B` | Hover de elementos en cobre |
| `color-text-main` (Carbón Verdoso) | `#26352F` | Títulos principales (h1, h2, h3), texto de lectura de alto contraste |
| `color-text-secondary` (Gris Verdoso) | `#66736B` | Descripciones, placeholders, metadata, subtítulos |
| `color-border` (Borde Neutro) | `#DDDCD2` | Líneas divisorias, bordes de inputs, cuadrículas de calendario |

### Tokens Semánticos
| Estado | Color Fondo | Color Texto / Icono | Aplicación |
|---|---|---|---|
| **Confirmada / Éxito** | `#EAF5EE` | `#24704B` | Reserva confirmada, pago completado, validación QR exitosa |
| **Pendiente / Advertencia** | `#FDF6EB` | `#A66518` | Cita pendiente de aprobación, aviso de conflicto horario |
| **Cancelada / Error** | `#FCEEEF` | `#B83236` | Cita rechazada/cancelada, error de formulario, bloqueo total |
| **Informativo / Neutro** | `#EAF2ED` | `#245C4F` | Indicadores de horario, notas informativas del profesional |

---

## 4. TIPOGRAFÍA Y ESCALA

### Fuentes del Sistema
- **Principal (UI & Datos):** `Inter`, `-apple-system`, `BlinkMacSystemFont`, `sans-serif`
- **Alternativa Titulares (Editorial/Premium):** `Manrope`, `sans-serif`

### Jerarquía Tipográfica
| Nivel | Tamaño | Peso | Interlineado | Tracking | Aplicación |
|---|---|---|---|---|---|
| **Display / H1** | `32px (2rem)` | 700 (Bold) | `1.2` | `-0.03em` | Títulos principales de dashboard |
| **H2 / Sección** | `24px (1.5rem)` | 600 (SemiBold) | `1.25` | `-0.02em` | Títulos de vistas, modales |
| **H3 / Tarjeta** | `18px (1.125rem)` | 600 (SemiBold) | `1.3` | `-0.01em` | Encabezados de tarjetas y servicios |
| **Body Regular** | `14px (0.875rem)` | 400 (Regular) | `1.5` | `0` | Párrafos, tablas, valores de campo |
| **Body Medium** | `14px (0.875rem)` | 500 (Medium) | `1.5` | `0` | Labels, botones, items de navegación |
| **Small / Metadata** | `12px (0.75rem)` | 500 (Medium) | `1.4` | `+0.01em` | Badges, horas secundarias, breadcrumbs |
| **Micro / Overline** | `11px (0.6875rem)` | 600 (SemiBold) | `1.3` | `+0.05em` | Categorías en mayúsculas |

---

## 5. ESPACIADO, RADIOS Y SOMBRAS

### Escala de Espaciado (Base 4px / 8px)
- `space-1`: 4px | Micro padding
- `space-2`: 8px | Separación entre iconos y etiquetas
- `space-3`: 12px | Padding interno de inputs compactos
- `space-4`: 16px | Padding estándar de tarjetas y botones
- `space-6`: 24px | Gaps entre tarjetas de grid
- `space-8`: 32px | Padding de contenedores de página
- `space-12`: 48px | Separaciones de secciones mayores

### Radios de Borde (`border-radius`)
- `radius-sm`: 6px (Badges, tags, tooltips)
- `radius-md`: 10px (Botones, inputs, dropdowns)
- `radius-lg`: 16px (Tarjetas de dashboard, modales, paneles)
- `radius-xl`: 24px (Contenedores cliente, hojas móviles)
- `radius-full`: 9999px (Avatares, pills de estado)

### Sombras Táctiles (Suaves y Orgánicas)
- `shadow-sm`: `0 1px 2px rgba(38, 53, 47, 0.04)`
- `shadow-card`: `0 2px 8px -2px rgba(38, 53, 47, 0.06), 0 1px 3px rgba(38, 53, 47, 0.03)`
- `shadow-dropdown`: `0 10px 25px -5px rgba(38, 53, 47, 0.10), 0 4px 6px -2px rgba(38, 53, 47, 0.04)`
- `shadow-modal`: `0 20px 40px -10px rgba(25, 72, 62, 0.16)`

---

## 6. SISTEMA DE COMPONENTES REUTILIZABLES

### 1. Botones (`Button`)
- **Primary:** Fondo `#245C4F`, texto `#FFFFFF`. Hover: `#19483E`. Focus: ring 3px `#245C4F` (opacidad 25%).
- **Secondary:** Fondo `#FFFFFF`, borde 1px `#DDDCD2`, texto `#26352F`. Hover: `#F7F5F0`.
- **Accent / Copper:** Fondo `#B7794B`, texto `#FFFFFF`. Hover: `#9E643B`. Para acciones clave de conversión (ej. "Confirmar Reserva").
- **Ghost:** Fondo transparente, texto `#66736B`. Hover: fondo `#EAF2ED`, texto `#245C4F`.
- **Destructive:** Fondo `#FCEEEF`, borde `#F5C2C4`, texto `#B83236`. Hover: fondo `#B83236`, texto `#FFFFFF`.

### 2. Campos de Formulario (`Input`, `Select`, `Textarea`)
- Altura estándar: 42px.
- Fondo: `#FFFFFF`, borde: 1px sólido `#DDDCD2`.
- Estado Focus: borde `#245C4F`, sombra `0 0 0 3px rgba(36, 92, 79, 0.12)`.
- Estado Error: borde `#C3423F`, mensaje auxiliar en `#B83236` con icono de alerta.

### 3. Tarjeta de Cita & Ficha de Reserva (`BookingCard`)
- Estructura:
  - Header: Hora destacada en badge con tipografía tabular (`font-variant-numeric: tabular-nums`).
  - Cuerpo: Nombre del cliente, servicio con duración (`45 min • 45€`), profesional asignado.
  - Footer: Badge de estado (Confirmada, Pendiente, Validada por QR) + Trigger de acciones rápidas.

### 4. Componente de Validación QR (`QRValidationBadge`)
- Muestra el token cifrado único (ej. `BKF-8921-X9`) junto con el código QR escaneable.
- Permite acciones de 1 clic:
  - **Validar Cita** (Verde Bosque) -> cambia estado a *Completada / Asistida*.
  - **Rechazar / Cancelar** (Contorno destructivo) con modal de motivo.

### 5. Selector Semanal de Agenda (`WeeklyScheduleGrid`)
- Columnas de Lunes a Domingo.
- Bloques de disponibilidad con relleno `#EAF2ED` y borde izquierdo 3px `#245C4F`.
- Bloques bloqueados / vacaciones con fondo tramado sutil y etiqueta *"No disponible"*.

---

## 7. ESPECIFICACIÓN DE PERFILES DE USUARIO

### Perfil 1: Administrador / Propietario
- **Vista Principal:** Dashboard métricas (Ocupación semanal, Total de ingresos del mes, Citas pendientes de validación, Próximas reservas del día).
- **Herramientas Clave:** Gestión de plantilla de profesionales, catálogo de servicios con asignación de tarifas, bloqueos de festivos y panel de facturas emitidas.

### Perfil 2: Profesional / Especialista
- **Vista Principal:** Agenda de hoy con vista cronológica paso a paso.
- **Herramientas Clave:** Lector / validador QR de clientes que llegan al establecimiento, notas privadas por cita y gestión de descansos entre servicios.

### Perfil 3: Cliente Final (Mobile-First)
- **Flujo de Reserva:**
  1. Catálogo de servicios con filtros por especialidad y precio.
  2. Elección de profesional o asignación automática por disponibilidad.
  3. Selección de fecha en calendario visual + ranura horaria libre.
  4. Resumen de reserva con confirmación inmediata y entrega de pase con Código QR.

---

## 8. RECOMENDACIONES DE IMPLEMENTACIÓN EN REACT

```tsx
// Tokens CSS estructurados (tokens.css)
:root {
  --color-primary: #245c4f;
  --color-primary-dark: #19483e;
  --color-primary-soft: #eaf2ed;
  --color-bg: #f7f5f0;
  --color-surface: #ffffff;
  --color-accent: #b7794b;
  --color-accent-hover: #9e643b;
  --color-text-main: #26352f;
  --color-text-muted: #66736b;
  --color-border: #dddcd2;
  --radius-md: 10px;
  --radius-lg: 16px;
  --shadow-card: 0 2px 8px -2px rgba(38, 53, 47, 0.06);
}
```

---
*Documento generado para BookFlow SaaS Platform — Arquitectura Frontend DAW y Evolución Comercial.*

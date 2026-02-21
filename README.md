# Gestión de Impresoras 3D - Módulo para Odoo 19

Bienvenido al equipo de desarrollo. Este proyecto tiene como objetivo crear un módulo para Odoo 19 que gestione el inventario, estado y consumibles de un parque de impresoras 3D.

Este proyecto ha sido desarrollado por **Diego, Roberto, Javier y Mario**.

## Índice
1. [Información General del Proyecto](#1-información-general-del-proyecto)
2. [Problemática y Solución](#2-problemática-y-solución)
3. [Funcionalidades Principales](#3-funcionalidades-principales)
4. [Estructura del Proyecto](#4-estructura-del-proyecto)
5. [Tecnologías Utilizadas](#5-tecnologías-utilizadas)
6. [Modelos de Datos](#6-modelos-de-datos)
7. [Vistas e Interfaz](#7-vistas-e-interfaz)
8. [Sistema de Reportes](#8-sistema-de-reportes)
9. [Seguridad y Permisos](#9-seguridad-y-permisos)
10. [Instalación y Configuración](#10-instalación-y-configuración)

---

## 1. Información General del Proyecto

### Descripción
**Gestión de Impresoras 3D** es un módulo personalizado para Odoo 19. Permite llevar un control exhaustivo del ciclo de vida de las máquinas, su estado operativo y el inventario de materiales (bobinas de filamento) asignados a cada una.

### Datos del Proyecto
* **Nombre del Módulo:** `gestion_impresoras`
* **Versión:** 1.1
* **Plataforma:** Odoo 19.0
* **Categoría:** Inventory / Manufacturing
* **Licencia:** LGPL-3
* **Tipo:** Módulo de Aplicación

### Contexto Académico
Este proyecto ha sido desarrollado como trabajo práctico de la asignatura **SGE (Sistemas de Gestión Empresarial)** del curso **2º DAM (Desarrollo de Aplicaciones Multiplataforma)**. Demuestra la capacidad de trabajar en equipo mediante control de versiones (Git/GitHub) y el desarrollo nativo en el framework de Odoo.

## 2. Problemática y Solución

### Problema que Resuelve
Los laboratorios de impresión 3D (granjas de impresoras) y los talleres maker se enfrentan a problemas de organización diaria:
* **Descontrol de estados:** No se sabe de un vistazo qué máquinas están imprimiendo, cuáles están libres y cuáles están averiadas.
* **Falta de mantenimiento:** Se pierde el hilo de cuántas impresiones lleva una máquina y cuándo necesita revisión técnica.
* **Caos de consumibles:** Las bobinas de filamento o botellas de resina se gastan o se pierden, y no hay un registro de qué material está asignado a qué impresora.

### Solución Implementada
Este módulo soluciona estos problemas centralizando la información y proporcionando:
* **Registro automatizado** del inventario físico de máquinas.
* **Control de consumibles (Bobinas)**, relacionando directamente cada rollo de plástico con su impresora actual.
* **Panel Kanban interactivo** para cambiar el estado de las impresoras arrastrando y soltando (Drag & Drop).
* **Ficha técnica en PDF** imprimible para pegar físicamente en cada máquina.
* **Gráficos estadísticos** para analizar la carga de trabajo de cada tecnología.

---

## 3. Funcionalidades Principales

### 1. Gestión del Parque de Impresoras
Permite registrar cada máquina con su fotografía, modelo, tecnología (FDM, SLA, SLS) y fecha de compra. Permite activar una alerta visual si la máquina requiere mantenimiento en base a su carga de trabajo.

### 2. Inventario de Bobinas (Materiales)
Un modelo secundario que actúa como almacén de consumibles. Permite registrar rollos de filamento, indicando su material (PLA, ABS, PETG, TPU), peso inicial (en gramos) y asignándolos de forma dinámica a una impresora operativa del sistema.
* **¿Por qué es importante?** Relaciona los gastos de material con el hardware, sentando las bases para una trazabilidad completa del taller.

### 3. Tablero Kanban de Producción
Visualización de las máquinas en tarjetas organizadas en columnas según su estado actual: *Disponible, Imprimiendo o Averiada*.
* **¿Por qué es importante?** Ofrece a los operarios del taller una vista rápida del estado del laboratorio, ideal para pantallas táctiles o tablets.

### 4. Gráficos de Análisis de Carga
Representación visual en diagrama de barras que agrupa el número total de impresiones realizadas por cada tecnología de impresión.
* **¿Por qué es importante?** Ayuda en la toma de decisiones (por ejemplo, si las máquinas FDM tienen mucha más carga que las SLA, conviene invertir más en FDM).

### 5. Generación de Fichas Técnicas PDF
Genera automáticamente un reporte profesional con los datos técnicos de la máquina y su estado actual. Diseñado para imprimirse y adherirse al chasis de las impresoras físicas.

---

## 4. Estructura del Proyecto

El código está organizado siguiendo la arquitectura MVC (Modelo-Vista-Controlador) estándar de Odoo:

```text
gestion_impresoras/
│
├── __init__.py                      # Inicialización del módulo Python
├── __manifest__.py                  # Configuración y metadatos del módulo
├── README.md                        # Documentación del proyecto
│
├── models/                          # Lógica de negocio (Backend)
│   ├── __init__.py                  # Importación de los modelos
│   ├── impresora.py                 # Modelo principal: impresion.impresora
│   └── bobina.py                    # Modelo secundario: impresion.bobina
│
├── views/                           # Interfaz de usuario (XML)
│   ├── impresora_view.xml           # Vistas core (Form, List, Kanban, Search) y menús
│   ├── bobina_view.xml              # Vistas para inventario de filamentos
│   └── impresora_graficos.xml       # Vista de análisis de datos (Graph)
│
├── report/                          # Plantillas de impresión
│   └── impresora_report.xml         # Diseño QWeb de la ficha técnica PDF
│
└── security/                        # Control de acceso
    └── ir.model.access.csv          # Permisos CRUD para los grupos de usuarios
```
## 5. Tecnologías Utilizadas

### Backend
* **Python 3.10+:** Lenguaje base para la lógica de negocio.
* **Odoo ORM:** Sistema de mapeo objeto-relacional para interactuar con la base de datos sin escribir SQL directo.
* **PostgreSQL:** Base de datos relacional subyacente.

### Frontend
* **XML:** Para la declaración de las vistas (interfaz de usuario) y acciones.
* **QWeb:** Motor de plantillas de Odoo para la generación del PDF.

### Herramientas de Desarrollo
* **Git y GitHub:** Control de versiones distribuido. Uso de ramas separadas (`rama_javier`, `rama_mario`, `rama_roberto`, `rama_diego`) para simular un entorno de trabajo real en equipo y posterior integración (Merge) a la rama `master`.

---

## 6. Modelos de Datos

### Modelo 1: `impresion.impresora`
Actúa como tabla maestra del hardware del laboratorio.
* **Tabla en BD:** `impresion_impresora`

| Campo | Tipo | Descripción | Requerido |
|-------|------|-------------|-----------|
| `name` | Char | Identificador/Nombre de la máquina | Sí |
| `modelo` | Char | Modelo específico (ej. Ender 3) | Sí |
| `tecnologia` | Selection | FDM, SLA, SLS | Sí |
| `foto` | Binary | Imagen de la impresora | No |
| `estado` | Selection | Disponible, Imprimiendo, Averiada | Sí |
| `num_impresiones` | Integer | Contador de trabajos realizados | No |
| `necesita_mantenimiento`| Boolean | Alerta técnica de revisión | No |

### Modelo 2: `impresion.bobina`
Gestiona el inventario de materiales consumibles y su asignación.
* **Tabla en BD:** `impresion_bobina`

| Campo | Tipo | Descripción | Requerido |
|-------|------|-------------|-----------|
| `name` | Char | Identificador (ej. PLA Rojo Mate) | Sí |
| `material` | Selection | PLA, ABS, PETG, TPU | Sí |
| `peso_inicial` | Integer | Gramos de material | No (Def: 1000) |
| `impresora_id` | Many2one | Relación con la impresora en uso | No |

**Relación:** Una impresora (`impresora_id`) puede tener asignadas múltiples bobinas a lo largo de su vida útil.

---

## 7. Vistas e Interfaz

* **Vista Formulario (Form View):** Interfaz dividida por secciones (`<group>`). Incorpora widgets avanzados como `statusbar` (para flujos de estado), `image` (para previsualizar fotos) y `boolean_toggle` (para activar alertas de mantenimiento).
* **Vista Lista (List View):** Tabla resumen optimizada mediante la nueva etiqueta `<list>` de Odoo 19. Incorpora decoradores condicionales (`decoration-success`, `decoration-danger`) que cambian el color de la fila según el estado de la máquina.
* **Vista Kanban:** Tarjetas dinámicas organizadas en columnas (`default_group_by="estado"`). Permite la gestión visual y ágil del parque de impresoras mediante "Drag & Drop".
* **Vista Búsqueda (Search):** Buscador avanzado con filtros rápidos ("Disponibles", "Averiadas", "Requiere SAT") para facilitar la navegación en inventarios grandes.
* **Vista Gráfico (Graph):** Representación en diagrama de barras (`type="bar"`) cruzando el número de impresiones totales con cada tecnología disponible.

---

## 8. Sistema de Reportes

### Ficha Técnica de Impresora (PDF)
* **Trigger:** Botón "Imprimir" en la vista de formulario o lista.
* **Proceso:** Odoo renderiza el template QWeb utilizando `<t t-call="web.external_layout">` para mantener el formato corporativo (logo, cabecera y pie de página).
* **Contenido:** Extrae y formatea dinámicamente el nombre, modelo, tecnología y la imagen de la impresora, preparado para su impresión física y uso en el taller.

---

## 9. Seguridad y Permisos

El archivo `security/ir.model.access.csv` garantiza los niveles de seguridad de la base de datos, evitando errores de acceso denegado ("Access Denied").

| ID | Nombre | Modelo | Grupo Odoo | Permisos (R,W,C,U) |
|----|--------|--------|------------|--------------------|
| `access_impresora` | `access.impresora` | `impresion.impresora` | `base.group_user` | 1, 1, 1, 1 |
| `access_bobina` | `access.bobina` | `impresion.bobina` | `base.group_user` | 1, 1, 1, 1 |

*(Se otorgan permisos completos de Lectura, Escritura, Creación y Borrado a los usuarios del grupo base).*

---

## 10. Instalación y Configuración

### Requisitos Previos
* Odoo 19.0 instalado localmente o en servidor.
* PostgreSQL funcionando.

### Pasos de Instalación
1. **Copiar el módulo:** Colocar la carpeta `gestion_impresoras` dentro del directorio `addons/` de tu servidor Odoo.
2. **Actualizar lista de aplicaciones:** * Entrar a Odoo.
   * Ir a **Ajustes** > Activar **Modo Desarrollador**.
   * Ir al menú de **Aplicaciones** > Hacer clic en **Actualizar lista de aplicaciones**.
3. **Instalar el módulo:** * En el buscador de aplicaciones (borrando el filtro por defecto), buscar "Gestión de Impresoras 3D".
   * Hacer clic en **Instalar**.
4. **Comenzar a usar:** * Navegar al nuevo menú principal "Impresoras 3D" para registrar tu primera máquina y sus bobinas asociadas.

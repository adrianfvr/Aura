# AURA

> Plataforma web desarrollada con Django que permite a instructores publicar cursos y a estudiantes explorar, inscribirse y realizar seguimiento de su progreso de aprendizaje.

---

## Descripción

AURA es una plataforma educativa desarrollada como proyecto académico utilizando Django. El sistema implementa autenticación personalizada, gestión de cursos, seguimiento de progreso, estadísticas de usuario y un panel de control intuitivo.

Cada usuario puede crear una cuenta, explorar cursos disponibles, inscribirse y visualizar su avance. Los instructores cuentan con herramientas para publicar y administrar cursos dentro de la plataforma.

---

## Características

### 👤 Gestión de usuarios
### 📚 Gestión de cursos
### 🎯 Sistema de inscripciones
### 📊 Dashboard personal
### 🔎 Exploración de cursos
### 🔔 Experiencia de usuario

---

## Tecnologías utilizadas

| Tecnología | Versión    |
| ---------- | ---------- |
| Python     | 3.11+      |
| Django     | 5.2        |
| SQLite     | Desarrollo |
| Bootstrap  | 5.3        |
| Pillow     | 12.2       |
| HTML5      | -          |
| CSS3       | -          |
| JavaScript | -          |

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/AURA.git
cd AURA
```

### 2. Crear entorno virtual

```bash
python -m venv env
```

### 3. Activar entorno virtual

**Windows**

```bash
env\Scripts\activate
```

**Linux / macOS**

```bash
source env/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```
> [!NOTE]
> Necesario únicamente para acceder al panel administrativo y asignar permisos de instructor.

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en:

```text
http://127.0.0.1:8000
```

---

## Rutas principales

| Ruta            | Descripción           |
| --------------- | --------------------- |
| `/`             | Catálogo de cursos    |
| `/registro/`    | Registro de usuario   |
| `/login/`       | Inicio de sesión      |
| `/dashboard/`   | Dashboard del usuario |
| `/crear-curso/` | Crear curso           |
| `/admin/`       | Administración Django |

---

## ..Roles del sistema

### Estudiante

* Registrarse.
* Iniciar sesión.
* Explorar cursos.
* Inscribirse.
* Gestionar progreso.
* Visualizar estadísticas.

### Instructor

Además de las funciones del estudiante:

* Crear cursos.
* Editar cursos.
* Gestionar contenido publicado.
  
> [!NOTE]
> El rol de instructor debe ser asignado por un administrador desde el panel de administración.

---

## 📁 Estructura del proyecto

```text
AURA/
├── cursos/
├── dashboard/
├── usuarios/
├── frontend/
│   ├── static/
│   │   └── css/
│   │       └── main.css
│   └── templates/
│       ├── base.html
│       ├── cursos.html
│       ├── detalle_curso.html
│       ├── dashboard.html
│       ├── crear_curso.html
│       ├── login.html
│       ├── registro.html
│       └── 404.html
├── media/
├── plataforma/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📸 Capturas

### Registro
<img width="1545" height="804" alt="imagen" src="https://github.com/user-attachments/assets/036e3293-6d2b-45bc-ac88-f9adda03d09f" />

### Inicio de Sesión
<img width="1542" height="802" alt="imagen" src="https://github.com/user-attachments/assets/7c98676b-3d90-41d8-b5ac-2c8bab056306" />

### Dashboard
<img width="1522" height="792" alt="imagen" src="https://github.com/user-attachments/assets/d3d4e830-a8e1-48e0-ae32-64d19c9ab391" />

### Explorar Cursos
<img width="1534" height="569" alt="imagen" src="https://github.com/user-attachments/assets/e8298044-7093-45b9-b734-71637fe426ce" />

### Crear Curso
<img width="1541" height="716" alt="imagen" src="https://github.com/user-attachments/assets/cbb6973e-59d6-4df2-9324-e3c484c602f2" />

### Detalle del Curso
<img width="1536" height="767" alt="imagen" src="https://github.com/user-attachments/assets/52ea5e80-8f68-4ca2-a4bd-d1278b729c59" />

---

## Información almacenada

La plataforma mantiene información persistente sobre:

* Usuarios registrados.
* Información de perfil.
* Cursos publicados.
* Instructor creador de cada curso.
* Fecha de creación.
* Inscripciones.
* Progreso individual por curso.
* Estado de completado.
* Actividad reciente.

---

## Mejoras futuras

* [ ] Módulos y lecciones por curso.
* [ ] Certificados de finalización.
* [ ] Sistema de comentarios.
* [ ] Calificaciones y reseñas.
* [ ] Paginación avanzada.
* [ ] PostgreSQL para producción.
* [ ] Despliegue en la nube.
* [ ] Notificaciones por correo.
* [ ] Recuperación de contraseña.

---

## ⚠️ Estado del proyecto
> [!WARNING]
> Actualmente en Desarollo

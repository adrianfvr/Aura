# AURA — Plataforma de Cursos

> Plataforma web para gestión de cursos desarrollada con Django. Permite a profesores/instructores
> publicar cursos y a estudiantes explorarlos e inscribirse

---

## 🛠️ Tecnologías

| Tecnología | Versión |
|---|---|
| Python | 3.11+ |
| Django | 5.2 |
| Base de datos | SQLite (desarrollo) |
| CSS Framework | Bootstrap 5.3 |
| Imágenes | Pillow |

---

## ⚡ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/plataforma.git
cd plataforma
```

### 2. Crear y activar entorno virtual

```bash
python -m venv env
```

```bash
# Windows
env\Scripts\activate

# Mac / Linux
source env/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install django pillow
```

### 4. Aplicar las migraciones

```bash
python manage.py migrate
```

### 5. Crear un superusuario

> [!NOTE]
> Es opcional, pero necesario para acceder al panel `/admin/` y asignar el rol de instructor a los usuarios.

```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

> [!TIP]
> Abrir el navegador en `http://127.0.0.1:8000` para ver la plataforma en funcionamiento.

---

## Rutas disponibles

| Ruta | Descripción |
|---|---|
| `/` | Catálogo de cursos |
| `/registro/` | Crear una cuenta nueva |
| `/login/` | Iniciar sesión |
| `/dashboard/` | Ver cursos inscritos |
| `/crear-curso/` | Crear un curso *(solo instructores)* |
| `/admin/` | Panel de administración |

---

## Roles de usuario

> [!IMPORTANT]
> AURA maneja dos roles diferenciados. El rol de instructor **no se puede activar desde el registro**, requiere acceso al panel de administración.

- **Estudiante** — se registra normalmente desde `/registro/` y puede inscribirse en cualquier curso disponible.
- **Instructor** — un administrador debe activar el campo `es_instructor = True` desde el panel `/admin/` en el modelo de usuario.

---

## 📁 Estructura del proyecto

```
plataforma/
├── cursos/           # Modelos, vistas y formularios de cursos
├── dashboard/        # Panel de control del usuario
├── usuarios/         # Registro, login y modelo de usuario
├── frontend/
│   └── templates/    # Plantillas HTML (base, cursos, dashboard, etc.)
├── media/            # Imágenes subidas por los usuarios
├── plataforma/       # Configuración central (settings, urls)
└── manage.py
```

> [!NOTE]
> Los estilos CSS están actualmente definidos dentro de `base.html`. En futuras versiones se migrarán a un archivo estático dedicado.

---

## Capturas
> Inicio Sesión
<img width="500" alt="login" src="https://github.com/user-attachments/assets/14b13117-57c6-462e-91e4-78b26474b1d0" />

> Dashboard
<img width="500" alt="dashboard" src="https://github.com/user-attachments/assets/44969ffe-0fef-420f-b068-fca91d6fa689" />

> Mis Cursos
<img width="500" alt="mis-cursos" src="https://github.com/user-attachments/assets/b36e3c28-2fe5-41d2-b98c-0e5f5247d846" />

> Detalle Curso
<img width="500" alt="detalle-curso" src="https://github.com/user-attachments/assets/b4f86361-12df-48e4-9de0-f2b38f96e6db" />

> Crear Curso
<img width="500" alt="crear-curso" src="https://github.com/user-attachments/assets/72b1f784-1406-4edf-8d17-884f16c72b0b" />


---

## Estado del proyecto

> [!WARNING]
> El proyecto está actualmente en desarrollo. No se recomienda usarlo en producción sin antes configurar PostgreSQL, variables de entorno y un servidor.

- [x] Registro y autenticación de usuarios
- [x] Catálogo de cursos con búsqueda
- [x] Inscripción a cursos
- [x] Creación de cursos con imagen de portada
- [x] Dashboard personal
- [ ] Progreso real de cursos *(actualmente estático al 60%)*
- [ ] Módulos y lecciones por curso
- [ ] Despliegue en producción (PostgreSQL + Nginx)
- [ ] Paginación y filtros avanzados
- [ ] Notificaciones por correo

---


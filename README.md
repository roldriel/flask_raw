![Pylint](https://github.com/roldriel/flask_raw/actions/workflows/pylint.yml/badge.svg)
![Flake8](https://github.com/roldriel/flask_raw/actions/workflows/flake8.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)


# 🚀 Boilerplates para Lenguajes de Programación

Este proyecto en Flask proporciona un **boilerplate completo**, diseñado para ayudar a los desarrolladores a implementar **buenas prácticas de desarrollo** desde el inicio.

## 🎯 Objetivo

Facilitar la creación de proyectos con estructura, configuraciones y pruebas predeterminadas, promoviendo estándares de calidad en el código desde las primeras etapas del desarrollo.

## ✨ Características
- **Estructura modular**: Plantillas bien organizadas para mantener el código limpio y fácil de mantener.
- **Compatibilidad con Docker**: Simplifica el despliegue con un entorno Docker listo para usar.
- **Pruebas**: Configuración inicial de pruebas para asegurar la calidad desde el primer commit.
- **Herramientas de análisis**: Integración con `pylint` y `flake8` para promover un código más legible y sin errores.

## 📂 Estructura del Proyecto

```plaintext
flask_raw/
├── Dockerfile
├── requirements.txt
└── src/
    ├── app.py           # Punto de entrada de la aplicación Flask
```

## 🛠️ Instalación y Ejecución

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/roldriel/flask_raw.git
   cd flask_raw
   ```

2. **Construye el contenedor Docker**:
   ```bash
   docker build -t flask_raw .
   ```

3. **Ejecuta el contenedor**:
   ```bash
   docker run -p 8000:8000 flask_raw
   ```

4. **Accede a la aplicación** en `http://localhost:8000`

## ⚙️ Configuración Adicional

- **Linter**: Ejecuta `flake8` y `pylint` para mantener la calidad del código.
   ```bash
   flake8 src/
   pylint src/
   ```

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Si quieres mejorar o añadir más funcionalidades, por favor abre un _issue_ o envía un _pull request_.

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

# Simulador de Ecosistema Interactivo

Este proyecto es un simulador de ecosistema interactivo creado en Python utilizando la biblioteca Tkinter para la interfaz gráfica de usuario. El ecosistema simulado presenta depredadores (leones) y presas (ciervos) interactuando con plantas dentro de un entorno cerrado.

## Características

- **Simulación de Depredador-Presa**: Los leones persiguen a los ciervos, y los ciervos se alimentan de las plantas.
- **Control de la Simulación**: Puedes iniciar, pausar y detener la simulación utilizando botones de control.
- **Visualización de Conteos**: La interfaz muestra el número de leones, ciervos y plantas en el ecosistema en tiempo real.
- **Diseño Adaptable**: Los botones y labels están ubicados en la parte inferior de la ventana para una mejor accesibilidad.

## Requisitos del Sistema

Para ejecutar este proyecto, necesitarás:

- **Python 3.x**: Se recomienda utilizar la versión más reciente de Python.
- **Bibliotecas de Python**: Las siguientes bibliotecas deben estar instaladas:
  - Tkinter (normalmente incluido con Python)
  - Pillow (para manejar imágenes)

## Instalación

1. **Clona el Repositorio**:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Instala las Dependencias Necesarias**:

    Asegúrate de tener `pip` instalado y luego ejecuta:

    ```bash
    pip install pillow
    ```

3. **Configura las Rutas de las Imágenes**:

    Las imágenes de los leones, ciervos y plantas deben estar ubicadas en la carpeta `assets/images` dentro del directorio raíz del proyecto. Asegúrate de que las rutas de las imágenes en el código fuente (simulator.py) sean correctas. Las imágenes deben estar en los siguientes archivos:

    - León: `lion.png`
    - Ciervo: `deer.png`
    - Planta: `plant.png`

    La estructura del directorio debería verse así:

    ```
    .
    ├── EcosystemSimulator/
    │   ├── src/
    │   │   ├── simulator.py
    │   │   ├── creature.py
    │   │   ├── plant.py
    │   │   └── ...
    │   └── assets/
    │       └── images/
    │           ├── lion.png
    │           ├── deer.png
    │           └── plant.png
    ├── README.md
    └── ...
    ```

## Ejecución

Para ejecutar la simulación, navega al directorio del proyecto y ejecuta el archivo `main.py`:

```bash
python main.py
```

## Estructura del Proyecto

- **main.py**: Punto de entrada del proyecto que inicializa y ejecuta la simulación.
- **src/**: Contiene el código fuente del proyecto.
  - **simulator.py**: Archivo principal que maneja la interfaz gráfica y la simulación.
  - **creature.py**: Clase que define las criaturas (leones y ciervos) en la simulación.
  - **plant.py**: Clase que define las plantas en la simulación.
- **assets/**: Carpeta que contiene las imágenes utilizadas en la simulación.
  - **images/**: Carpeta con las imágenes (león, ciervo, planta).

## Uso

- **Iniciar la Simulación**: Haz clic en el botón "Iniciar Simulación" para comenzar.
- **Pausar la Simulación**: Haz clic en "Pausar Simulación" para detener temporalmente el movimiento.
- **Detener la Simulación**: Haz clic en "Detener Simulación" para reiniciar todo el ecosistema.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o haz un fork del repositorio y envía un pull request con tus mejoras.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

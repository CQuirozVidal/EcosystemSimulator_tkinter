# Interactive Ecosystem Simulator

This project is an interactive ecosystem simulator created in Python using the Tkinter library for the graphical user interface. The simulated ecosystem features predators (lions) and prey (deer) interacting with plants in a closed environment.

## Features

- **Predator-Prey Simulation**: Lions chase deer, and deer feed on plants.
- **Simulation Control**: You can start, pause, and stop the simulation using control buttons.
- **Real-Time Counts**: The interface shows the number of lions, deer, and plants in the ecosystem in real time.
- **Adaptable Design**: Buttons and labels are placed at the bottom of the window for better accessibility.

## System Requirements

To run this project, you'll need:

- **Python 3.x**: It's recommended to use the latest version of Python.
- **Python Libraries**: The following libraries need to be installed:
  - Tkinter (usually included with Python)
  - Pillow (for handling images)

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/CQuirozVidal/EcosystemSimulator_tkinter.git
    cd EcosystemSimulator_tkindter
    ```

2. **Install Necessary Dependencies**:

    Make sure you have `pip` installed, then run:

    ```bash
    pip install pillow
    ```

3. **Configure Image Paths**:

    The images of lions, deer, and plants must be located in the `assets/images` folder inside the project root directory. Ensure that the image paths in the source code (`simulator.py`) are correct. The images should be in the following files:

    - Lion: `lion.png`
    - Deer: `deer.png`
    - Plant: `plant.png`

    The directory structure should look like this:

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

## Running

To run the simulation, navigate to the project directory and run the `main.py` file:

```bash
python main.py
```

## Project Structure

- **main.py**: Entry point of the project that initializes and runs the simulation.
- **src/**: Contains the source code of the project.
  - **simulator.py**: Main file handling the graphical interface and simulation logic.
  - **creature.py**: Class defining the creatures (lions and deer) in the simulation.
  - **plant.py**: Class defining the plants in the simulation.
- **assets/**: Folder containing the images used in the simulation.
  - **images/**: Folder with the images (lion, deer, plant).

## Usage

- **Start the Simulation**: Click the "Start Simulation" button to begin.
- **Pause the Simulation**: Click "Pause Simulation" to temporarily stop the movement.
- **Stop the Simulation**: Click "Stop Simulation" to reset the entire ecosystem.

## Contributions

If you want to contribute to this project, please open an issue or fork the repository and submit a pull request with your improvements.

## License

This project is distributed under the MIT License. See the `LICENSE` file for more details.

---


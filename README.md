# Welcome to Pathfinder-GUI!

We developed this solution for the **First Lego League** competition in order to accelerate our test process.

It's an easy-to-use GUI where you can define paths on the playing map and convert them into code for your Robot. 

The map is currently based on the official FLL map from the Masterpiece season 2023/2024 and will be updated automatically for each season.

<br>

![Pathfinder GUI GIF](https://github.com/GO-Robot-FLL/Pathfinder-GUI/blob/main/img/pathfinder.gif)
*Live Demo of Pathfinder*

<br>

# Requirements
1. Pathfinder-GUI was made with **Python 3.12.0**. 

    Make sure to install the newest version of [Python](https://www.python.org/downloads/).

2. Install Pygame and Numpy with pip:

    ```
    pip install pygame
    pip install numpy
    ```

<br>

# Usage 

How to start the GUI:

1. Clone this repository from **GitHub**

2. Run "main.py" file

## Buttons
- **"Output"**: 
    Prints the code for all paths to the console.

    *Important Note: The program only calculates the length and angle of the path. You can format the output as you like.*

- **"Right / Left"**: Sets the starting point for the current path to the right or left Start Zone. You can only set the starting point if the path is empty.

- **"Clear Map"**: Clears all paths on the map. 


## Create a single path
Just click on the map to add points. The shortest path between two points using the euclidean distance is added automatically.

## Create multiple paths
Use  number keys 1-6 to select a new path with a different color. The new path also starts from the defined starting point. 

<br>

# Reporting bugs 
If you find a bug, kindly report it to go.robot@gmynasium-ottobrunn.de or open a pull request. We will try to fix it as soon as possible. If you have any questions regarding the code, please reach out to us using the same Email adress.

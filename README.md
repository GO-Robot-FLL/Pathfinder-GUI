# Welcome to Pathfinder 

We developed this solution for the **First Lego League** competition.
It's an easy-to-use GUI where you can define paths on the playing map and convert them into code for your Robot. 

The map is based on the official FLL map from the season 2022/2023 and will be updated automatically for each season.


# Requirements
1. Pathfinder-GUI was made with **Python 3.12.0**. 

    Make sure to install the newest version of [Python](https://www.python.org/downloads/).

2. Install Pygame and Numpy with pip:

    ```
    pip install pygame
    pip install numpy
    ```


# Usage 

How to start the GUI:

1. Clone repo from our **GitHub**

2. Run "main.py" file

## Buttons
- **"Output"**: 
    Prints the code for the selected path to the console.

    *Important Note: The program only calculates the length and angle of the path. You can format the output as you like.*

- **"Clear Map"**: Clears all paths 
- **"Right / Left"**: This function is currently under developement. It should set the starting point for the current path to the right or left Start Zone.

## Create a single path
Just click on the map to add points. The shortest path between them is added automatically.

## Create multiple paths
Use the Number Keys 1 - 6 select a new path with a different color. 


# Reporting bugs 
If you find a bug, kindly report it to go.robot@gmynasium-ottobrunn.de or open a pull request. We will try to fix it as soon as possible. If you have any questions regarding the code, please reach out to us using the same Email adress.

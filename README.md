# Info
- This directory contains scripts to be run by `Bertini v1.6`, using `GMP v6.0.0` and `MPFR v3.1.2`

# Important Files

## `Haunestein/Equations.nb`
 - This Mathematica file generates a system of equations that we want to solve in Bertini. The equations are saved to a file, the file path is printed at the bottom of the notebook. Each line in the file is a different equation which will then be passed into `Haunstein/generate_input.py`.
 - To run, click `Evaluation -> Evaluate Notebook` at the top of Mathematica. This will generate the file and print its path at the bottom of the notebook.

## `Hauenstein/generate_input.py`
 - Generates an `input` file for Bertini using the file generated from `Equations.nb`. Note that the equations generated in `Equations.nb` have `**` instead of `^` for exponents, but this Python file handles the replacement while generating the `input` file.
 - To run, run `python generate_input.py` when the file `family1.txt` is in the current directory. This will output `input` in the current directory.

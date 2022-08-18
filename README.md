# Info
- This directory contains scripts to be run by `Bertini v1.6`, using `GMP v6.0.0` and `MPFR v3.1.2`

# Important Files

## `Haunestein/Equations.nb`
 - This Mathematica file generates a system of equations that we want to solve in Bertini. The equations are saved to a file, the file path is printed at the bottom of the notebook. Each line in the file is a different equation which will then be passed into `Haunstein/generate_input.py`.

## `Hauenstein/generate_input.py`
 - Generates an `input` file for Bertini using the file generated from `Equations.nb`. Note that the equations generated in `Equations.nb` have `**` instead of `^` for exponents, but this Python file handles the replacement while generating the `input` file.


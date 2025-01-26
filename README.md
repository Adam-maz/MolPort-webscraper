# Collecting SMILES from MolPort with Selenium

## 1. Introduction
This document introduces a script that enables users to collect **SMILES** strings from **MolPort** using web scraping techniques with **Selenium**. The script generates a `.csv` file as output, containing the IDs and SMILES strings of the desired particles. This `.csv` file can, for example, be used to build a library of reactants for reaction-based enumeration in lead optimization.

## 2. Usage
To use this script:
1. Download an `.sdf` file containing the molecules you want to collect.
2. Convert this file to a `.csv` file (you can use tools like the **DataWarrior suite** for this step).
3. Launch the script and follow the provided instructions.

## 3. Dependencies
To run this script, ensure the following packages are installed in your virtual environment:
- `pandas`
- `selenium`
- `webdriver_manager`

You can install them by running the following command:
```bah
pip install pandas selenium webdriver_manager
```

## 4. Selenium documentation
https://selenium-python.readthedocs.io/

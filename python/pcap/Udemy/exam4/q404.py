#!/usr/bin/python3
# You want to install version 1.3.5 of the module pandas, for your Python user environment only.
# How can you achieve this ?

# Explanation:
# pip is the standard tool to install & manage Python packages.
# A few of the most commonly used commands to install a Python package with pip:
# pip install package : install package system-wide
# pip install --user package : install package for the current user only
# pip install -U package : update previously installed package
# pip install package==x : install version x of package
# pip uninstall package : uninstall previously installed package

# Here is the only pip command that satisfies that requirement is :
# pip install --user pandas==1.3.5
# Note : pandas is an actual Python package very commonly used for data science.
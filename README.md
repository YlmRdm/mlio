# mlio
MLIO is a machine learning project for my master thesis...

Dependencies:
- Python v3.7.4
- conda 4.7.11
- pip 19.2.3

Tools:
- Atom IDE
- Anaconda 2019.03
- Anaconda Command line client (version 1.7.2)

Installation:
- conda env create -f environment.yml -n mlio
- conda env update -f environment.yml -n mlio
- conda activate mlio
- make data/raw/Exp2StraceBTIOckpt1n1.xlsx | make clean | make all
- Run preprocess.py

You can also see the following notebook "00-initial-exploration.ipynb" by clicking the button:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/YlmRdm/mlio/master)

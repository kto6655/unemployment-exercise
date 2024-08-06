# unemployment-exercise

## Setup

Create virtual environment:

```sh
conda create -n ump-env python=3.11
```

Activate the environment:

```sh
conda activate ump-env
```

Install packages:

```sh
#pip install requests
#pip install plotly
#pip install python-dotenv

# instead of pip installing each package individually like above...
# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```
# to check that your packages were installed correctly, use command 'pip list' to confirm they are in the list


## Usage

Run the script:

```sh
python app/unemployment.py

# equivalent:
# (we'll need this alternative command once we start importing code from one python file to another)
python -m app.unemployment
```
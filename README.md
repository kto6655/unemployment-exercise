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

To check that your packages were installed correctly, use command 'pip 
list' to confirm they are in the list


Obtain an API KEY from Alphavantage.

Then create an ".env" file in the root (top level) of your repo and paste some contents in it like this (but using your API Key):

```sh
# example of what would be in your .env file:
ALPHAVANTAGE_API_KEY="_______________"
```

## Usage

Run the script:

```sh
python app/unemployment.py

# equivalent:
# (we'll need this alternative command once we start importing code from one python file to another)
python -m app.unemployment
```

# Uploading progress to GitHub by "Committing" and "Pushing to Origin" 
## Setup

# Create virtual environment:

```sh
conda create -n ump-env python=3.11
```

# Activate the environment:

```sh
conda activate ump-env
```

# Install packages:

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

Note: If you add a new package to the requirements.txt,  you will need to run the pip install
command again in your terminal to install it (it won't automatically update just by adding to list)


# Obtain an API KEY from Alphavantage.

Then create an ".env" file in the root (top level) of your repo and paste some contents in it like this (but using your API Key):

```sh
# example of what would be in your .env file:
ALPHAVANTAGE_API_KEY="_______________"
```

## Usage

Run the Unemployment Report:

```sh
python -m app.unemployment
```

Run the Stocks Report:

```sh
python -m app.stocks
```

## Testing

Run tests:

```sh
pytest
```

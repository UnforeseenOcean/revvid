# redigen

A program that aims to automate the creation of "reddit videos" (r/AskReddit style).

The goal for this project is to be able to composite text to speech audio alongside screenshots for a given reddit post and export it as a video. It is currently in development. 

The current state of the project allows it to:
- Take screenshots of top level comments of a thread
- Generate audio using the epic Daniel voice for each comment. 

Todo:
- Composite the screenshots and audio into a video. 

## Installation

Clone the repo

```console
$ git clone https://github.com/kyb3r/redigen
$ cd redigen
```

Install dependancies
```console
$ pipenv install
```

Create a .env file with your [reddit client id and secret](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html).
```env
CLIENT_ID=xxxxxx
CLIENT_SECRET=xxxxxxx
```

Finally run the app via
```
pipenv run python3 app.py
```

## Usage
You can either run the app by itself to get an interactive interface or supply a command line argument for the id of the specific submission you want to fetch screenshots from. 

e.g. 
```
python3 app.py bw8gyr
```


## License 

GNU GPL v3

## Contributing

Feel free to make contributions, they are always welcome!

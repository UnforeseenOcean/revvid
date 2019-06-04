# redigen

A program that aims to automate the creation of "reddit videos" (r/AskReddit style).

The goal for this project is to be able to composite text to speech audio alongside screenshots for a given reddit post and export it as a video. It is currently in development. 

The current state of the project allows it to:
- Take screenshots of top level comments of a thread
- Generate audio using the epic Daniel voice for each comment. 
- Composite them into a cool video. Heres a [**sample**.](https://youtu.be/qaQhsALt8mk)

Todo:
- Add customisability, since stuff like the outro, subreddit and number of comments are hardcoded. 

Please feel free to make a PR with improvements :)

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

Create a .env file with your [reddit client id and secret](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html). This is to check the hot posts for today for r/AskReddit. If you are supplying a specific post id via the CLI then this is not needed. 
```env
CLIENT_ID=xxxxxx
CLIENT_SECRET=xxxxxxx
```

Finally run the app via
```
pipenv run python3 app.py
```

## Usage

Note: This only works on mac since `pyttsx3` supports saving audio files only on mac [pyttsx3#30](https://github.com/nateshmbhat/pyttsx3/issues/30). If theres a better way to get tts audio files cross platform, please make a PR :) 

You can either run the app by itself to get an interactive interface or supply a command line argument for the id of the specific submission you want to fetch screenshots from. 

e.g. 
```
python3 app.py bw8gyr
```


## License 

GNU GPL v3

## Contributing

Feel free to make contributions, they are always welcome!

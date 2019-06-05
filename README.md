<h1 align='center'>Revvid</h1>

You've probably seen a bunch of /r/AskReddit narration style videos by now. So I randomly thought to start working on a program to automate the creation of them. Its still a WIP but the current state of the project allows it to: 

- Take screenshots of top level comments of a thread using selenium.
- Generate audio using the epic Daniel voice for each comment. 
- Have looping background music.
- Composite all of the above into a cool video. Heres a [**sample**.](https://youtu.be/o18mIpx_NxA)
- ~~Output high quality content~~

Todo:
- Add customisability since things like the outro, subreddit and comment limit are currently hardcoded.
- Ability to curate your own comments/support for replies. 
- Turn it into a CLI tool 

Please feel free to make a PR with improvements :)

## Installation

Clone the repo

```console
$ git clone https://github.com/kyb3r/revvid
$ cd revvid
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

Note: This only works on mac since `pyttsx3` supports saving audio files only on mac [(pyttsx3#30)](https://github.com/nateshmbhat/pyttsx3/issues/30). If theres a better way to get tts audio files cross platform, please make a PR :) 

You can either run the app by itself to get an interactive interface or supply a command line argument for the id of the specific submission you want to fetch screenshots from. 

e.g. 
```
python3 app.py bw8gyr
```


## License 

GNU GPL v3

## Contributing

Feel free to make contributions, they are always welcome!

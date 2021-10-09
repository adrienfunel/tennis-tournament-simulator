# tennis-tournament-simulator :tennis:
Service designed to simulate a multi-player tennis tournament and provide the outcome

## Description
This service takes the number of participating players as an input and run a simulation of a tennis tournament.
The players are attributed skill scores (power, technique, endurance) to be used to generate the result of their matches.
The tournament is a single-elimination tournament (inspired by Grand Slam tennis), the winner will move on to the next round and face the winner of the round with the incremented seed.
Every match is entirely simulated in the `game.py` module. The score is logged and passed to the bracket class object. 
The detailed results are to be found in the log file.


## Requirements
- The code must run without crashes/errors
- The tournament should be a single-elimination tournament
- The simulation should work for any number of players between 2 and 64 inclusive
- There are no concrete requirements on the input/output formats but the simulation should be able
to produce data such as a list of all games played and their results
- You may make reasonable assumptions, as ong as your assumptions do not oversimplify the exercise


## Technical Specifications

### Setup
All dependencies are listed in `requirements.txt` and `tests\requirements-test.txt`, to install them in your environment run:
```
pip install -r requirements.txt
```

### Run the service
To run the service, navigate to the src directory and run:
```
python main.py
```

### Player class
The PLayer class is used to generate players and attribute skill scores for the matches.
```
{'Id': int,
'Power': float,
'Technique': float,
'Endurance': float
}
```

### Bracket class
The Bracket class is used to generate rounds and keep track of the matches results.
```
{'seed': int,
'p1': object,
'p2': object,
'winner': object,
'score': string
}
```

### Logging
The logging strategy is set up in `src/common/my_logger.py`. The logging level is INFO and contains all information
about the service run and the games simulation. The logging module will create a new file in the project folder to write
its logs. There are two handler: a file handler to write and store logs, and a stream handler to displays the logs
during execution.


### Testing
The unit testing is located in the `tests` folder. Install the requirements from `requirements-test.txt` before running the tests.


## What's missing
- A data layer to store the player's information
- A front end
- Include an additional feature to represent the advantage the player who serves get
- Implement logic for generating a tournament for a number of players that is not a power of 2 (ex: 12 players)
- Comprehensive unit testing


## References:
- [Important skills for a tennis player](https://tennisfiles.com/8-critical-tennis-skills-how-test-them/)
- [Tennis results on the BBC website](https://www.bbc.co.uk/sport/tennis/results)
- [Tennis scoring system](https://www.onlinetennisinstruction.com/tennisscoring/)
- [Grand Slam rounds naming](https://en.wikipedia.org/wiki/Single-elimination_tournament)

# tennis-tournament-simulator :tennis:
Service designed to simulate a multi-player tennis tournament and provide the outcome

## Description



## Requirements
- The code must run without crashes/errors
- The tournament should be a single-elimination tournament
- The simulation should work for any number of players between 2 and 64 inclusive
- There are no concrete requirements on the input/output formats but the simulation should be able
to produce data such as a list of all games played and their results
- You may make reasonable assumptions, as ong as your assumptions do not oversimplify the exercise


## Technical Specifications

### Player class
```
{'Id': int,
'Power': float,
'Technique': float,
'Endurance': float
}
```

### Bracket class
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


## What's missing
- A data layer to store the player's information
- A front end
- Include an additional feature to represent the advantage the player who serves get
- Comprehensive unit testing


## References:
- [Important skills for a tennis player](https://tennisfiles.com/8-critical-tennis-skills-how-test-them/)
- [Tennis results on the BBC website](https://www.bbc.co.uk/sport/tennis/results)
- [Tennis scoring system](https://www.onlinetennisinstruction.com/tennisscoring/)
- [Grand Slam rounds naming](https://en.wikipedia.org/wiki/Single-elimination_tournament)

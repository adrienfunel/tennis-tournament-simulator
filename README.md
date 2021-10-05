# tennis-tournament-simulator :tennis:
Service designed to simulate a multi-player tennis tournament and provide the outcome

## Description



## Requirements

 The code must compile (if applicable for the language chosen) and run without crashes/errors.
 The tournament should be a single-elimination tournament.
 The simulation should work for any number of players between 2 and 64 inclusive.
 There are no concrete requirements on the input/output formats but the simulation should be able
to produce data such as a list of all games played and their results.
 You may make reasonable assumptions about anything not explicitly mentioned in this document, as
long as your assumptions do not oversimplify the exercise. For example, simulating an entire match
with a 50/50 coin toss is too much.


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


## What's missing
- A data layer to store the player's information
- A front end
- Include an additional feature to represent the advantage the player who serves get
- Comprehensive unit testing


## References:
- [Important skills for a tennis player](https://tennisfiles.com/8-critical-tennis-skills-how-test-them/)
- [Tennis results on the BBC website](https://www.bbc.co.uk/sport/tennis/results)

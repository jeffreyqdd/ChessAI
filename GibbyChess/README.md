# Gibby Chess

## An Introduction
Chess engine written entirely in chess. Implements a deep learning neural network over a traditional evaluation function. The neural network is trained over two main steps. 1) Mimicking - the model is trained off thousands of master-level games played by high ranked players from lichess. 2) Reinforcement learning - the neural network is pitted against utself where i plays thousnads of more games over the course of many days. It learns from these games, further perfecting its evaluation algorithm


is pitted against itself where it plays thousands of more games over the course of many hours, and l

## Underneath the Hood

### Search Algorithms Used:

The chess implements implenents iterative deepening and monte-carlo tree search variants. My hope is do determine the strength and weaknesses of each variation, and then incporated both search strcutures into a singular engine to hammer out weakensses in the opening, middle game, and endgame. The end result is hopefully a chess engine unparalleld in its accuracy. 
- iterative deepening (WIP)
- monte-carlo tree search (Not Yet Implemented)

### Deeper Dive into Iterative Deepenings
TODO


### Deeper Dive into Monte Carlo Tree Search (MCTS)
TODO


### Deeper Dive into The Neural Network
The neural network is not able to understand the format of the chess board, so it is important to find an efficeint way to translated from a ```chess.Board``` object into a tensor of 3 dims. 

Before, I wrote a manual translation, but it topped out at 200 iterations/sec. An entire rewrite was needed. THfinal implementation was to use bitboards to generate a 3d bitboard tensor. It achieved 84574 iterations/s.
 

# Setup
## Environemnt
**Setup Environment**
1. ```python3 -m venv env```
2. ```source env/bin/activate```
3. ```pip install -r requirements.txt```
**To update the environment**
1. ```pip freeze > requirements.txt```

## Python path
we can either option (1) or option (2).

Option #1
1. ```cd $(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")```
2. ```echo /some/library/path > some-library.pth```

Option #2
1. manually set python path ```export $PYTHONPATH='some/dir/to/gibbychess'```

Note: I don't know how to set up a shell script to automatically do this. Everytime I do it, it doesn't actually change the python path. 

# Sources
**training data from:** https://database.lichess.org/
**documentation format:**
```python
class ThisIsAClass:
        """What does this class do or represent?
        """

        def __init__(self, a, b, *args, **kwargs) -> None:
                """Class constructur
                # params:
                - a (dtype) - what a is used for
                - b (dtype) - what is b used for
                - *args - what is *args used for
                - **kwargs - what is **kwargs used for
                """
                pass

        def this_is_a_function(self, a, b) -> int:
                """What does this function do

                # params:
                - a (dtype) - what is a used for
                - b (dtype) - what is a used for

                # returns:
                - (dtype) - what it represents
                """
                pass
```
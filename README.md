# ANEW Scorer
This is a basic scoring system based on the ANEW corpus per the 1999 paper. [Affective Norms for English Words (ANEW):
Instruction Manual and Affective Ratings](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.306.3881&rep=rep1&type=pdf). It provides a very crude means of performing sentiment analysis on a corpus.

### Installation
Clone this repository.
```sh
$ git clone https://github.com/dark0bserver/anew_scorer.git
```
Then switch to the cloned directory and use setup tools to install it.
```
$ cd anew_scorer
$ python setup.py .
```

### Usage
The score for a tokenized list of words can be found as illustrated with the example python below.
```python
from anew_scorer.scorer import AnewScorer

scorer = AnewScorer()
words = "the quick brown fox".split(" ")
print(scorer.vad_score_words(words))
```
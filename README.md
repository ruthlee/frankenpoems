# Frankenpoem 

Lots of poetry generators these days are focused on trying to cobble together "original" "creative" works of algorithmic poetry. To this I say: why reinvent the wheel? A wheel that the old masters surely have already perfected.

This is a poetry generator which cobbles together lines from poems that have already been written while paying attention to meter and rhyme to form something that (while perhaps nonsensical in content) still sounds like a, ahem, real poem.

In order to spread Frankenbot's genius throughout the world, I made a package with exactly one use case: to run Frankenbot's `write_poem()` command. So you, too, can experience the grandeur of Frankenbot's poetic vision.

## Installation
Enter `pip3 install frankenpoem` in your command line and it should world. Or try `pip install frankenpoem`. The latest version is 4.0.0 (...because it took me four tries to get the actual package working and I couldn't be bothered with TestPyPi), so if THAT doesn't work try `pip install frankenpoem==4.0.0` or pip3 of the same command.

Warning: you may need to make sure to have re and pandas installed, I don't think I got the package dependencies quite right.

## Usage
In the terminal, go to your python interpreter (for me I just type `python3`). Then:

```python
import frankenpoem as f
f.write_poem()
```

Et voila! A poem should generate. There are no arguments because you have no control over Frankenbot's creative process. He is his own creative entity and should be respected as such.

## Sources
Big shoutout to:

[Allison Parrish's repo](https://github.com/aparrish/gutenberg-poetry-corpus/blob/master/quick-experiments.ipynb) for providing the data for the project as well as a very useful rhyme-dictionary data structure for Frankenbot to use.

[Laurence Tennant's poetry-tools](https://github.com/hyperreality/Poetry-Tools) for meter and syllable analysis. 

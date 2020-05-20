# Frankenpoem 

Lots of poetry generators these days are focused on trying to create "original" works of algorithmic poetry. To this I say: why reinvent the wheel? A wheel that the old masters surely have already perfected.

This is a poetry generator which cobbles together lines from poems that have already been written while paying attention to meter and rhyme to form something that (while perhaps nonsensical in content) still sounds like a, ahem, real poem.

In order to spread Frankenbot's genius throughout the world, I made a package with exactly one use case: to run Frankenbot's `write_poem()` command. So you, too, can experience the grandeur of Frankenbot's poetic vision.

## Installation
Enter `pip3 install frankenpoem` in your command line and it should work. Or try `pip install frankenpoem`. Make sure you're grabbing the latest version, which is 7.0.0 (...because it took me six tries to get the actual package working and I couldn't be bothered with TestPyPi). If needed, you can specify installing this version by inputting `pip3 install frankenpoem==7.0.0` but just pip installing should install the latest version........

If you have trouble installing, it may be an issue with installing some of the package dependencies (this happened when I tested on a Windows machine running Ubuntu because pip couldn't install the pandas package successfully). Below is a list of dependent packages to help you debug, if needed: 
- [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html): this should already be installed if you have the anaconda distribution installed. 
- [pronouncing](https://pypi.org/project/pronouncing/)
- collections, re, random: you shouldn't need to install these if you have an up-to-date python interpreter because they're built-in modules, but ya know. For debugging.  

If you have installation issues ack gah let me know :)  

## Usage
In the terminal, go to your python interpreter (for me I just type `python3`). Then:

```python
import frankenpoem as f
f.write_poem()
```

Et voila! A poem should generate. There are no arguments because you have no control over Frankenbot's creative process. He is his own creative entity and should be respected as such.

The repo also contains [a notebook which documents the process of making write_poem()](https://github.com/ruthlee/frankenpoems/blob/master/frankenpoem_demo.ipynb) and [a log of some of Frankenbot's most notable works](https://github.com/ruthlee/frankenpoems/blob/master/some_good_ones.md).

## Sources
Big shoutout to:

[Allison Parrish's repo](https://github.com/aparrish/gutenberg-poetry-corpus/blob/master/quick-experiments.ipynb) for providing the data for the project as well as a very useful rhyme-dictionary data structure for Frankenbot to use.

[Laurence Tennant's poetry-tools](https://github.com/hyperreality/Poetry-Tools) for meter and syllable analysis. 

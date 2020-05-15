from tkinter import *
from tkinter import ttk
import poetrytools as pt
from poetrytools import guess_metre, tokenize, count_syllables
import gzip, json
import random
import pandas as pd
import matplotlib.pyplot as plt
import pronouncing
from collections import defaultdict
import re

def define_structure():
    length = random.randint(4, 10)
    line_breaks = random.randint(1, length-1)
    return length, line_breaks

def get_last_word(line):
    match = re.search(r'(\b\w+\b)\W*$', line)
    if match:
        last_word = match.group()
    last_word = re.sub(r'[^\w\s]', '', last_word)
    return last_word

def pick_first_line(df):
    last_word = ""
    while last_word == "":
        index = random.randint(1, len(df))
        first_line = df.text[index]
        last_word = get_last_word(first_line)
    return (index, df.text[index], last_word)

def get_rhyme_dict(pruned_df):
    by_rhyming_part = defaultdict(lambda: defaultdict(list))
    for line in pruned_df.text:
        match = re.search(r'(\b\w+\b)\W*$', line)
        if match:
            last_word = match.group()
            pronunciations = pronouncing.phones_for_word(last_word)
            if len(pronunciations) > 0:
                rhyming_part = pronouncing.rhyming_part(pronunciations[0])
                # group by rhyming phones (for rhymes) and words (to avoid duplicate words)
                by_rhyming_part[rhyming_part][last_word.lower()].append(line)     
    return by_rhyming_part

def destroy_labels(labels):
    for i in range(len(labels)):
        labels[i].destroy()

def write_poem():

    df = pd.read_pickle("data.pkl.compress", compression="gzip")

    length, line_breaks = define_structure()
    
    # pick the first line and get the last word of that first line
    index, first_line, last_word = pick_first_line(df)
            
    # prune the dataframe so that we restrict the number of syllables and the meter
    pruned_df = df[df.meter == df.meter[index]]
    pruned_df = df[(df.syllables > df.syllables[index]-3) & (df.syllables < df.syllables[index]+2)]
    
    # get the rhyme_dict for the pruned df so we can rhyme lines
    rhyme_dict = get_rhyme_dict(pruned_df)
    
    # keep track of widgets 
    labels = []

    # print the first line 
    lbl = Label(text = first_line)
    lbl.pack()
    
    break_here = False
    
    # now make the rest of the poem
    line = first_line
    for i in range(length):
            
        if break_here and line_breaks > 0:
            lbl = Label( text = "\n")
            lbl.pack()
            line_breaks-=1
            break_here = False
        
        # the random number will determine what we do...
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        magic_number = x + y 
                        
        # if we roll greater than or equal to 7 all hell breaks loose - no more rhyming 
        if (magic_number >= 10):
            line = random.choice(list(pruned_df.text))
            lbl = Label(text = line)
            lbl.pack()
            continue
        
        # line break on the next line
        if (magic_number < 6):
            break_here = True
        
        # print a rhyming line by getting the rhyming part of the last word, then choosing a random rhyming line 
        # from the rhyme_dict
        last_word = get_last_word(line)
        try:
            p = pronouncing.phones_for_word(last_word)
            rp = pronouncing.rhyming_part(p[0])
            random_key = random.choice(list(rhyme_dict[rp].keys()))
            new_line = random.choice(rhyme_dict[rp][random_key])
        except:
            new_line = random.choice(list(pruned_df.text))
        
        lbl = Label(text = new_line)
        lbl.pack()
        line = new_line
    
    line = ''.join(["*" for i in range(100)])
    lbl = Label(text = line)
    lbl.pack()
                
window = Tk()
window.geometry("500x500")

main_lbl = Label(master = window, text = "Hello. I am Frakenbot. I will create for you a Frankenpoem, if you will allow it.")
main_lbl.pack()

button = ttk.Button(master = window, text = "Make me a poem!", command = write_poem)
button.pack()

# clear_button = ttk.Button(master = window, text = "Clear", command = clear_text)
# clear_button.pack()

window.mainloop()
    
import random
import pandas as pd
import pronouncing
from collections import defaultdict
import re
import pkg_resources

def load_data():
    stream = pkg_resources.resource_stream(__name__, 'data.pkl.compress')
    return pd.read_pickle(stream, compression="gzip")

def define_structure():
    length = random.randint(4, 10)
    line_breaks = random.randint(1, length-1)
    
    # define rhyming structure
    rhyme_scheme = random.choice(["ABAB", "AABB", "random"])
    
    return length, line_breaks, rhyme_scheme

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

def thinking_messages():
    messages = ['I\'m thinking...', 'Eureka! I have the line now.', "Bother me not, darling, I am composing.",
               "I'm almost there... I'm getting there...", "Pass me the opium, I need to concentrate.",
               "What is the difference between metonymy and synecdoche again, darling?", "AHA!", "Egad!", "Alas!",
               "Where is my favorite quill?", "I shall soon tire of this labor and go to fight a war in Greece.",
               "I may go on a stroll among the daffodils later to clear my head.", "Poetry is a nasty business.",
               "Why yes, I AM *the* Lord Frankenbot. Pleased to meet your acquaintance indeed.",
               "I am utterly baffled by this line!", "Where shall I place this break, this pause.", 
               "Dear me! The emotions are getting out of hand.", "I must climb to a grassy windy hill and rumninate",
               "Perhaps one day I, too, will be buried at Westminster.", "Give me time. I strive towards God, you cretin.",
               "Just a moment, now. A few more moments.", "Hmm...", "Wonderful, just a few moments more.",
               "Whoever said composing such Godly lines would be easy?", "I am a Poet. And Poetry takes time."]

    choice = random.choice(messages)
    
    return choice

def get_rhyme_dict(pruned_df):
    # this data structure is ripped almost exactly from https://github.com/aparrish/pronouncingpy
    by_rhyming_part = defaultdict(lambda: defaultdict(list))
    for i, line in enumerate(pruned_df.text):
        if (i%500000 == 0):
            print(thinking_messages())
        match = re.search(r'(\b\w+\b)\W*$', line)
        if match:
            last_word = match.group()
            pronunciations = pronouncing.phones_for_word(last_word)
            if len(pronunciations) > 0:
                rhyming_part = pronouncing.rhyming_part(pronunciations[0])
                # group by rhyming phones (for rhymes) and words (to avoid duplicate words)
                by_rhyming_part[rhyming_part][last_word.lower()].append(line)     
    return by_rhyming_part

def print_poem(poem):
    for i in range(len(poem)):
        print(i)

def write_poem():

    df = load_data()

    print("Here I go! \n")
    
    length, line_breaks, rhyme_scheme = define_structure()
    
    # pick the first line and get the last word of that first line
    index, first_line, last_word = pick_first_line(df)
            
    # prune the dataframe so that we restrict the number of syllables and the meter
    pruned_df = df[df.meter == df.meter[index]]
    pruned_df = df[(df.syllables > df.syllables[index]-3) & (df.syllables < df.syllables[index]+2)]
    
    # get the rhyme_dict for the pruned df so we can rhyme lines
    rhyme_dict = get_rhyme_dict(pruned_df)
    
    # Frankenbot's done
    print("\n VOILA!! \n")
    print("*********************************************************")
    print("\n")
    
    # print the first line 
    print(first_line)
    
    # set break variable False so we don't line break before the first line
    break_here = False
    
    # now make the rest of the poem
    line = first_line
    while(length > 0):
            
        if break_here and line_breaks > 0:
            print("\n")
            line_breaks -= 1
            break_here = False
        
        # the random number will determine what we do...
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        magic_number = x + y 
        
        # line break on the next line
        if (magic_number < 6):
            break_here = True
        
        # if the rhyme scheme is random, print a rhyming line by getting the rhyming part of the last word, 
        # then choosing a random rhyming line from the rhyme_dict
            # if we roll greater than or equal to 7 all hell breaks loose - no more rhyming 
        
        if (magic_number >= 8 and rhyme_scheme == "random"):
            line = random.choice(list(pruned_df.text))
            print(line)
            length -= 1
            continue
            
        if (rhyme_scheme == "random"):
            last_word = get_last_word(line)
            try:
                p = pronouncing.phones_for_word(last_word)
                rp = pronouncing.rhyming_part(p[0])
                random_key = random.choice(list(rhyme_dict[rp].keys()))
                new_line = random.choice(rhyme_dict[rp][random_key])
            except:
                new_line = random.choice(list(pruned_df.text))
        
            print(line)
            line = new_line
            length -= 1
            
        if (rhyme_scheme == "AABB"):
            last_word = get_last_word(line)
            # get line which rhymes with last line
            try:
                p = pronouncing.phones_for_word(last_word)
                rp = pronouncing.rhyming_part(p[0])
                random_key = random.choice(list(rhyme_dict[rp].keys()))
                new_line = random.choice(rhyme_dict[rp][random_key])
            except:
                new_line = random.choice(list(pruned_df.text))
            print(new_line)
            
            # new couplet starting
            new_line = random.choice(list(pruned_df.text))      
            print(new_line) 
            line = new_line  
            length -= 2 
        
        if (rhyme_scheme == "ABAB"):
            word_a = get_last_word(line)
            try:
                p = pronouncing.phones_for_word(word_a)
                rp = pronouncing.rhyming_part(p[0])
                random_key = random.choice(list(rhyme_dict[rp].keys()))
                new_line_a = random.choice(rhyme_dict[rp][random_key])
            except:
                new_line_a = random.choice(list(pruned_df.text))
            
            line_b = random.choice(list(pruned_df.text))
            word_b = get_last_word(line_b)
            try:
                p = pronouncing.phones_for_word(word_b)
                rp = pronouncing.rhyming_part(p[0])
                random_key = random.choice(list(rhyme_dict[rp].keys()))
                new_line_b = random.choice(rhyme_dict[rp][random_key])
            except:
                new_line_b = random.choice(list(pruned_df.text))
            
            print(line_b)
            print(new_line_a)
            print(new_line_b)
            
            line = random.choice(list(pruned_df.text))
            length -= 3

    print("\n")
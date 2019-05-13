# script to extract dialogue + inline stage directions from a play
# given some parameters describing its syntax, eg. all caps for character
# names etc.
import collections
import os
import sys
from pathlib import Path
    
def is_dialogue(chunk):
    return True

def get_dialogue(play_path, convention="0_0_0", character_names=()):
    conventions = convention.split("_")
    chunk_delim = conventions[0]
    char_delim = conventions[1]
    char_cap = conventions[2]

    dialogue = ""
    with open(play_path, "r") as file:
        chunks = file.read().split('\n\n')
        for chunk in chunks:
            # check if these chunks are character text
            if is_dialogue(chunk):
                # remove first bit of chunk including char name
                heading_length = len(chunk.split(" ")[0])
                chunk = chunk[heading_length + 1:]
                # add the chunk text to each character entry in character_texts
                dialogue += chunk + "\n\n"
            else:
                print(chunk)

    return dialogue

def save_dialogue(dialogue, dest_path):
    with open(dest_path, "w") as file:
        file.write(dialogue)

# parameters
# path to play
# path to dest folde
# character naming convention (optional)
# character names (optional)

if __name__ == "__main__":
    author = sys.argv[1]
    play = sys.argv[2]
    # con_0 = sys.argv[3]
    con_0 = 0_0_0
    # character_names = sys.argv[4]
    character_names = ()

    play_path = "/thesis-partition/home/ec2-user/thesis/corpus/data/authors/%s/plays/%s/play.txt" % (author, play)
    # get dialogue from play
    dialogue = get_dialogue(play_path)
    # save in dest folder
    
    dest_folder = "./test_dialogue/%s" %  author
    if not Path(dest_folder).is_dir():
        os.makedirs(dest_folder)
    dest_path = dest_folder + "/" + play + ".txt"
    save_dialogue(dialogue, dest_path)

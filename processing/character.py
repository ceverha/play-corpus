import collections
import os
from pathlib import Path
# clean up pathing stuff
# automate across all directories
# start running some experiments with solo or aggregate characters
# piece together a play structure
# select character, generate text of random length, select next character
# improvements: character selection, character generations, length logic

# extracts list of characters from dramatis personae at beginning of plays
def get_dramatis_personae(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    
    index = lines.index("CHARACTERS\n") + 2
    characters = []
    line = lines[index]
    while line != "\n":
        line = line.strip()
        # remove character description
        comma = line.find(",")
        if comma != -1:
            line = line[0:comma]
        characters.append(line)
        index = index + 1
        line = lines[index]
    file.close()
    return characters
    
def get_character(chunk, characters):
    output = ""
    for character in characters:
        if chunk.find(character) != -1:
            output = character
            break
    return output

# aggregates text for each character, includes inline stage directions
# returns dictionary
def get_character_text(characters, file_path):
    character_texts = {}
    with open(file_path, "r") as file:
        # break into chunks
        chunks = file.read().split('\n\n')
        # remove title, "CHARACTERS", and dramatis personae
        chunks = chunks[4:]
        for chunk in chunks:
            # check if these chunks are character text
            character = get_character(chunk, characters)
            if character != "":
                # remove first bit of chunk including char name
                chunk = chunk[len(character) + 1:]
                # add the chunk text to each character entry in character_texts
                if character in character_texts:
                    character_texts[character] = character_texts[character] + "\n" + chunk 
                else:
                    character_texts[character] = chunk
    return character_texts

# writes files for each character's dialogue and inline stage directions
def write_files(character_texts, dest_folder):
    for character in character_texts:
        print("Writing file for %s" % character)
        print("%d lines" % collections.Counter(character_texts[character])["\n"])
        with open("%s%s.txt" % (dest_folder, character), "w") as file:
            file.write(character_texts[character])

if __name__ == "__main__":
    file_path_root = "../data/"
    author = "strindberg"
    plays = {"comrades": ("AXEL", "BERTHA", "ABEL", "WILLMER", "DR. ÖSTERMARK", "MRS. HALL", "CARL", "MRS. STARCK", "MAID"), 
             "countessjulie": ("JULIE", "JEAN", "KRISTIN"), 
             "easter": ("MRS. HEYST", "ELIS", "ELEONORA", "CHRISTINE", "BENJAMIN", "LINDKVIST"), 
             "facingdeath": ("DURAND", "ADÈLE", "ANNETTE", "THÉRÈSE", "ANTONIO", "PIERRE"), 
             "pariah": ("MR. X", "MR. Y"), 
             "thefather": ("CAPTAIN", "LAURA", "BERTHA", "DOCTOR", "PASTOR", "NURSE", "NÖJD", "ORDERLY"), 
             "thestronger": ("MME. X", "MLLE. Y"), 
             "theoutlaw": ("THORFINN", "VALGERD", "GUNLÖD", "GUNNAR", "ORM", "THRALL", "MESSENGER")}
    for play in plays:
        print("\n\nExtracting dialogue from %s.txt" % play)
        file_path = file_path_root + author + "/plays/" + play + ".txt"
        # characters = get_dramatis_personae(file_path)
        characters = plays[play]
        print("Found %d characters:" % len(characters))
        print(characters)
        character_texts = get_character_text(characters, file_path)
        dest_folder = "../data/%s/character/%s/" % (author, play)
        # check if dir exists first
        if not Path(dest_folder).is_dir():
            os.makedirs(dest_folder)
        write_files(character_texts, dest_folder)

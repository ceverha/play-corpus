import sys
import pickle
from dialogue_indexing import WordDialogueIndex

if __name__ == "__main__":
    with open("index.obj", "rb") as obj_file:
        index = pickle.load(obj_file)
        chunks = index.get_dialogue_chunks(sys.argv[1]) 
        print(len(chunks))
        for chunk in chunks:
            print(chunk[0:100])
            print("\n")

# reexamine vector download
# figure out if the file got corrupted or something
# try another download script
# make sure this functionality isn't deprecated

import gensim

if __name__ == '__main__':
    
    print("Loading in model...")
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    
    s1 = 'Oranges are my favorite fruit'
    s2 = 'I like to eat apples the most'
    s3 = 'Donald Trump is my favorite president'
    
    print("Computing distance 1")
    distance1 = model.wmdistance(s1,s2)
    print("Computing distance 2")
    distance2 = model.wmdistance(s1,s3)
    print("Computing distance 3")
    distance3 = model.wmdistance(s2,s3)

    print("%f   %f   %f" %(distance1, distance2, distance3))

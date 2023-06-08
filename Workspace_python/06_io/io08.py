import pickle

with open('test02.txt', 'rb') as file:
    score = pickle.load(file)
    print(score)
    print(type(score))

# pickle.load
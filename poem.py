import numpy as np
import sys

def adjacency_to_stochastic(a):
    """makes a stochastic matrix from an adjacency matrix

    Parameters:

    a: 2D numpy array, representing an adjacency matrix

    Returns:

    None

    a is modified so that every column is divided by its sum

    Example:

    >>> a = np.array([[1., 1], [1, 1]])
    >>> adjacency_to_stochastic(a)
    >>> a
    array([[0.5, 0.5],
           [0.5, 0.5]])

    """
    # TODO: fill in this function
    a = np.transpose(a)
    for i in range(a.shape[1]):
        if (np.sum(a[i]) != 0.0):
            a[i] = np.divide(a[i], np.sum(a[i]))
    a = np.transpose(a)

def random_step(a, i):
    """performs a single random step given a stochastic matrix

    Parameters:

    a: 2D numpy array
    i: int, starting node

    Returns

    An int which is one step away from I, chosen according to the
    distribution given by A

    """
    rng = np.random.default_rng()
    return rng.choice(a.shape[0], p=a[:, i])

def random_walk(a, i, length):
    """performs a random walk

    Parameters:

    a: 2D numpy array, representing a (square) stochastic matrix
    i: int, index of columns
    length: int, the number of steps of the random walk

    Returns:

    A list of indicies of length LENGTH, resulting from a random walk
    on A starting at I

    """
    walk = [i]
    # TODO: fill in this function
    for k in range(length-1):
        walk.append(random_step(a, i));
    return walk


# # read in txt file at stdin and split into words
try:
    text_file = open('sonnets.txt', 'r', encoding='utf-8')
except:
    print("Make sure sonnets.txt is in the same directory as hw06.py")
    exit()
text = text_file.read()[1:].split()
# delete duplicates
words = list(dict.fromkeys(text))
# pairs of adjacent words
pairs = list(zip(text[:-1], text[1:]))

# build adjacency matrix
n = len(words)
freq_matrix = np.zeros((n, n))
for (w1, w2) in pairs:
    freq_matrix[words.index(w2), words.index(w1)] += 1
# make adjacency matrix into a stochastic matrix
adjacency_to_stochastic(freq_matrix)

# perform a random walk on the matrix
walk = random_walk(freq_matrix, 0, 15*6)
# make a list of words from the random walk
gen_text = np.array(list(map(lambda i: words[i], walk)))

# minor formatting
gen_text.shape = (15, 6)
poem = "\n".join([" ".join(row) for row in gen_text]).lower()
if not poem[-1].isalpha():
    poem = poem[:-1]

print()
print(poem + "...")
print()


# Test Case 
# A = np.array(
# [
#     [0., 0, 1, 0, 1, 1],
#     [0, 0, 0, 0, 1, 1],
#     [1, 0, 0, 1, 1, 1],
#     [0, 0, 1, 0, 0, 0],
#     [1, 1, 1, 0, 0, 1],
#     [1, 1, 1, 0, 1, 0]
# ])

# a = np.array([
#     [1., 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print(adjacency_to_stochastic(a))

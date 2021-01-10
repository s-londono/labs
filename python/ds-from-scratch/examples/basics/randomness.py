# The random module produces pseudorandom numbers (deterministic sequences of random numbers)
import random

# The seed determines the random sequence generated. Setting the seed ensures we will get the same results every time
random.seed(10)

# Generate uniformly distributed random numbers
five_uniform_rnd_nums = [random.random() for _ in range(5)]

# Randomly choose numbers from a specific range.
rnd_in_range_1 = random.randrange(10)
rnd_in_range_2 = random.randrange(20, 55)

# Randomly re-order the elements from a list (in place)
one_to_ten = [i for i in range(1, 11)]
random.shuffle(one_to_ten)

# Randomly pick an element from a list
chosen_one = random.choice(["Neo", "Morpheus", "Trinity", "Ghost", "Mouse", "Smith"])

# Randomly choose a sample of elements without replacement (no duplicates)
abc = {"a", "b", "c", "d", "e", "f", "g"}
sample_letters = random.sample(abc, 3)

# Randomly choose a sample with replacement
abc_lst = [a for a in abc]
sample_letters_replacement = [random.choice(abc_lst) for _ in range(3)]


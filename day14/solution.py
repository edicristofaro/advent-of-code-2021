from collections import defaultdict

with open("input.txt", "r") as f:
    data = f.readlines()

data = [d.strip("\n") for d in data if d]
polymer_base = data[0].strip("\n")

pair_insert = {}
for p in data[2:]:
    p = p.split(" -> ")
    pair_insert[p[0]] = p[1]

chars = set(v for k, v in pair_insert)

print(polymer_base)
print(pair_insert)

# part 1
current_polymer = polymer_base
for i in range(10):
    print(f"Iteration {i+1}")
    starting_polymer = list(current_polymer)
    polymer = ""
    for j, c in enumerate(starting_polymer[:-1]):
        polymer = polymer + c
        lookup = c + starting_polymer[j + 1]
        polymer = polymer + pair_insert[lookup]

        current_polymer = polymer

    current_polymer = polymer + starting_polymer[j + 1]

print({i: current_polymer.count(i) for i in chars})

# part 2
# cant brute force it
# dict of chars and counts
# at each iteration, add 1 to all existing values
# create the new list of pairs you'd create based on the end of the prior pass
# add the counts of the new pairs from the prior step to the existing counts

# initialize our starting point to count pairs
current_pairs = defaultdict(int)
for j, c in enumerate(polymer_base[:-1]):
    current_pairs[c + polymer_base[j + 1]] += 1
print(current_pairs)

# iterate through the polymer, split pairs, count the new pairs in the new dict
# gotcha: make sure and multiply the counts by the occurrences of the split pair - this tripped me up for a while
# count characters by using the first char in each key, and then add one for the second char of the last pair
for i in range(40):
    print(f"Iteration {i+1}")
    prev_pairs = dict(current_pairs.copy())
    current_pairs = defaultdict(int)
    char_count = defaultdict(int)
    for p in prev_pairs:
        p1_key = p[0] + pair_insert[p]
        p2_key = pair_insert[p] + p[1]
        char_count[p[0]] += 1 * prev_pairs[p]
        char_count[pair_insert[p]] += 1 * prev_pairs[p]
        current_pairs[p1_key] += prev_pairs[p]
        current_pairs[p2_key] += prev_pairs[p]
        last_char = p[1]
    char_count[last_char] += 1
    print(char_count)

print(current_pairs)
print(char_count)
print(max(char_count.values()) - min(char_count.values()))

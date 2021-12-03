from typing import List, Tuple


with open("input.txt", "r") as f:
    observations = [line.strip("\n") for line in f.readlines()]

sample = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]

#part 1
def calculate_mode(num_list: str) -> int:
    num_list = [int(x) for x in num_list]
    return max(set(num_list), key=num_list.count)

def power_usage(obs: List[str]) -> Tuple[int, int]:
    gamma_rate_b = ''
    epsilon_rate_b = ''
    place = ''
    width = len(obs[0])

    for i in range(width-1, -1, -1):
        place = [x[i] for x in obs]
        gamma_rate_b += str(calculate_mode(place))
    
    gamma_rate_b = gamma_rate_b[::-1]
    epsilon_rate_b = ''.join('1' if x == '0' else '0' for x in gamma_rate_b)
    
    return int(gamma_rate_b, 2), int(epsilon_rate_b, 2)

g, e = power_usage(sample)
print(g * e)

#part 2
def life_support_rating(obs: List[str]) -> int:
    oxygen_generator_rating = ''
    co2_scrubber_rating = ''

    return int(oxygen_generator_rating, 2), int(co2_scrubber_rating, 2)
    
o, c = life_support_rating(observations)
print(o * c)
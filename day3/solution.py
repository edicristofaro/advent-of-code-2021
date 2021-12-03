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
def calculate_significant_bit(num_list: str, round_up: bool = True) -> int:
    num_list = [int(x) for x in num_list]
    zeroes = num_list.count(0)
    ones = num_list.count(1)

    if zeroes > ones:
        return 0
    elif zeroes < ones:
        return 1
    elif zeroes == ones and round_up:
        return 1
    else:
        return 0

def filter_list_by_bit_position(num_list: str, bit_position: int, mode: int) -> str:
    keep = []

    for n in num_list:
        if int(n[bit_position]) == mode:
            keep.append(n)
    
    return keep

def life_support_rating(obs: List[str]) -> int:
    width = len(obs[0])
    oxy_obs = obs
    co2_obs = obs

    # if this were to be reused, should be a function, recursive solution would be better than breaking the loop
    # but it's acceptably janky because we're using it once and submitting only the answer
    for i in range(0, width):
        place = [x[i] for x in oxy_obs]
        mode = calculate_significant_bit(place)
        oxy_obs = filter_list_by_bit_position(oxy_obs, i, mode)
        if len(oxy_obs) == 1:
            break

    for i in range(0, width):
        place = [x[i] for x in co2_obs]
        mode = 1 if calculate_significant_bit(place, round_up=True) == 0 else 0
        co2_obs = filter_list_by_bit_position(co2_obs, i, mode)
        if len(co2_obs) == 1:
            break
    
    return int(oxy_obs[0], 2), int(co2_obs[0], 2)
    
o, c = life_support_rating(observations)
print(o * c)
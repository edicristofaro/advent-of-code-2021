with open("sample_input.txt", "r") as f:
    contents = f.readlines()

lanternfishes = []
lanternfish_seeds = [int(number) for number in contents[0].split(",")]


def project_population_stupid(lanternfish_seeds, days):
    for d in range(days):
        count = 0
        for s in lanternfish_seeds:
            if s == 0:
                count += 1

        lanternfish_seeds = [x - 1 for x in lanternfish_seeds if x > 0]

        for i in range(count):
            lanternfish_seeds.append(6)
            lanternfish_seeds.append(8)

        print(f"Day: {d + 1} - Population: {len(lanternfish_seeds)}")
    return len(lanternfish_seeds)


print(project_population_stupid(lanternfish_seeds, 80))
# print(project_population_stupid(lanternfish_seeds, 256))

# uh oh. gotta do something different.
# don't track every fish, we only care about their timer value.
# keep a hash of key:value pairs of timer:count
# each day, move each population to the next lower timer value (e.g. 8 -> 7, 6 -> 5, etc.)
# those in 0 go to 6, and the same number gets added to 8

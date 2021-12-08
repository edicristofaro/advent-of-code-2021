with open("input.txt", "r") as f:
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


def project_population_optimized(lanternfish_seeds, days):
    fish = { i: 0 for i in range(0,9)}
    for f in lanternfish_seeds:
        fish[f] += 1
    
    for d in range(1, days+1):
        # print(fish)
        spawn = 0
        for i in range(0,9):
            # print(f"Day: {d} - Bucket: {i} -  Population: {fish[i]}")
            if i == 0:
                spawn = fish[i]
            fish[i] = fish.get(i+1, 0)
        
        fish[6] += spawn
        fish[8] += spawn

    return sum(fish.values())

print(project_population_stupid(lanternfish_seeds, 80))
print(project_population_optimized(lanternfish_seeds, 80))
print(project_population_optimized(lanternfish_seeds, 256))
# print(project_population_stupid(lanternfish_seeds, 256))

# uh oh. gotta do something different.
# don't track every fish, we only care about their timer value.
# keep a hash of key:value pairs of timer:count
# each day, move each population to the next lower timer value (e.g. 8 -> 7, 6 -> 5, etc.)
# i cheated a little by seeing how someone solved in excel, but the implementation is now above.
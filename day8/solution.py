signals = []
output_counter = 0
with open("./input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        k, v = line.split(" | ")
        signals.append((k.split(" "), v.split(" ")))

# part 1
for signal, output in signals:
    for o in output:
        if len(o) in [2, 4, 7, 3]:
            output_counter += 1

print(output_counter)

# part 2
# for each line lets build a dict of lists of char for each digit, with the key being the digit
# 1, 4, 7, 8 keys can be populated based on length of string alone
# 2, 3, 5 all differ by one segment, and are 5 segments long; 3 contains all of 1; 2 and 5 contain only half of 1
## 3 contains all of 1
## 2 has 2 segments in common with 4
## 5 has 3 segments in common with 4
# 0, 6, 9 all differ by two segments, and are 6 segments long
## 0 does not contain all of 3
## 6 does not contain all of 1
## 9 contains all of 3

output_digits = []
for signal, output in signals:
    # (['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc'], ['fgae', 'cfgab', 'fg', 'bagce'])
    digit_lookup = {}
    signal = sorted(signal, key=len)
    for s in signal:
        digit_lookup["8"] = list("abcdefg")
        if len(s) == 2:
            digit_lookup["1"] = list(s)
        elif len(s) == 4:
            digit_lookup["4"] = list(s)
        elif len(s) == 3:
            digit_lookup["7"] = list(s)
        elif len(s) == 5:
            if all(i in list(s) for i in digit_lookup["1"]):
                digit_lookup["3"] = list(s)
            elif len(set(digit_lookup["4"]) - set(list(s))) == 2:
                digit_lookup["2"] = list(s)
            elif len(set(digit_lookup["4"]) - set(list(s))) == 1:
                digit_lookup["5"] = list(s)
        elif len(s) == 6:
            if all(i in list(s) for i in digit_lookup["3"]):
                digit_lookup["9"] = list(s)
            elif not all(i in list(s) for i in digit_lookup["1"]):
                digit_lookup["6"] = list(s)
            else:
                digit_lookup["0"] = list(s)
    # oh lord this is ugly, should have maybe spared an extra variable instead of using list(s) everywhere
    # there's probably a better refactor of this too

    output_digit = ""
    for o in output:
        list_o = list(o)
        for k, v in digit_lookup.items():
            if sorted(list_o) == sorted(v):
                output_digit = output_digit + k

    output_digits.append(int(output_digit))

print(sum(output_digits))

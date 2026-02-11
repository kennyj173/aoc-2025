inputs = ""
combinations = []
sum = 0
with open("aoc-day-3/battery-inputs.txt", "r") as file:
    inputs = file.read()
    inputs = inputs.splitlines()

for i in inputs:
    numberIndex = 0
    largest = 0
    for firstDigit in range(0, len(i) - 1):
        for selectedDigit in range(firstDigit + 1, len(i)):

            total = int(i[firstDigit] + i[selectedDigit])
            if total > largest:
               largest = total
        
        

    combinations.append(largest)

for i in combinations:
    sum = sum + i

print(sum)
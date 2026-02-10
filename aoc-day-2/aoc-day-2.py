ranges = []
invalidIDs = []
sum = 0

with open("aoc-day-2/id-inputs.txt", "r") as file:
        ids = file.read()
        ranges = ids.rsplit(",")
        
for i in ranges:
        separated = i.rsplit("-")
        firstNumber = int(separated[0])
        secondNumber = int(separated[1])
        selectedNumber = firstNumber
        
        while selectedNumber <= secondNumber:
                selectedString = str(selectedNumber)
                firstHalf = selectedString[:(len(selectedString) // 2)]
                secondHalf = selectedString[(len(selectedString) // 2):]

                if firstHalf == secondHalf:
                    invalidIDs.append(selectedNumber)
                selectedNumber = selectedNumber + 1


for i in invalidIDs:
       sum = sum + i

print(sum)
        

        
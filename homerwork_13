reader = open("in.txt", mode="r")
content = reader.read().split()
numbers = [int(num) for num in content]
newtext = sorted(numbers)
output = " ".join(map(str, newtext))
writer = open("out.txt", mode="w")
writer.write(output)

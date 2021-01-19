string = input("Write string: ")
result = ""

for char in string:
  result += char*2 if char != " " else " "

print(result)

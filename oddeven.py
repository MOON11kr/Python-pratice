def oddev(a):
  if a % 2 == 0:
    return "Even"
  else:
    return "Odd"

n = int(input("Enter a number: "))
result = oddev(n)
print(result)
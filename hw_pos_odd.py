# value = 10
# #print("Positive") if value >= 0 else print("Negative")

value = int(input("Enter a number: "))
#print("Positive") if value >= 0 else print("Negative")
print("Positive and odd") if (value % 2) == 1 and value >= 0 else print("The rest")

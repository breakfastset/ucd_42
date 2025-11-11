x = "5"   # string
y = 5     # integer

print(x * 5)  # replicate "5" 5 times
print(y * 5)  # product of 5 * 5

# result = x + y  # error int + str not allowed
result = int(x) + y  # convert x to int OR
print(result)   # 5 + 5 = 10

result = x + str(y)  # convert y to string
print(result)   # "5" + "5" = "55"
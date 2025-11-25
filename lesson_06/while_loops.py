# usage of while loop: unknown number of executions
# structure is as follows:
#
# 1. prime the loop (prepare to enter the loop)
# while 2. condition is True:
#     3. statement 1
#        statement 2
#        ...
#        statement n
#     4. update variable
#        (eventually to make condition False to exit loop)
#
# 5. other statements outside the loop
#
# Flow: 1 - 2 - 3 - 4 - 2 - 3 - 4 - 2 - 3 - 4 - 2 - 5

# example 1: fixed number of loops (not the best usage scenario)
count = 0               # 1. prime the loop
while count < 5:        # while 2. condition is True
    print("---------")  #    3. statements
    print(count)
    print(".........")  #       end of statements
    count = count + 1   #    4. update var

print("--- Bye ---")    # 5. out of the loop

# example 2: unknown number of executions
rating = int(input("Movie rating (1 to 5)? "))  # 1.
while rating < 1 or rating > 5:                 # 2.
    print("Invalid rating! Must be 1 to 5 only!")  # 3.
    rating = int(input("Movie rating (1 to 5)? "))  # 4.

# 5.
print(f"You rated {rating} for ABC movie.")










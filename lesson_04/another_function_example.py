GRAVITY = 9.81    # Global

def useless_function():
    a = 10     # local variable
    b = 8      # local variable
    return a + b

def main():
    result = useless_function()
    print(f"result: {result}")   # no problem
    print(a)    # cannot access a because it is local to useless_function
    print(b)    # cannot access b because it is a local variable
    print(GRAVITY)   # no issue as it is a global constant

main()
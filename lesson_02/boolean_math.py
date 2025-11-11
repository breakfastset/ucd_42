
print(True)
print(False)
print(True + False)  # 1 + 0 -> 1
print(True + True)   # 1 + 1 -> 2
print(True * False)  # 1 * 0 -> 0
print()

print(bool(""))      # False,  empty string
print(bool("a"))     # True
print(bool(0))       # False,  0
print(bool(100))     # True
print(bool([]))          # False, empty list
print(bool(["a", "b"]))  # True

# bool() = False if any of the following is true:
#   1. empty string
#   2. number is 0 or 0.0
#   3. empty collection / set / list
# bool() = True otherwise
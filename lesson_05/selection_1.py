# 1. if - only
# applies only if true, otherwise do nothing
amount = 499.90
is_member = False

if is_member:  # if is_member == True:
    amount = amount * 0.9    # apply a 10% discount

print(f"You need to pay ${amount:.2f}")


print("=== ALL OPERATORS CALCULATOR ===")
a = input("Enter first value: ")
b = input("Enter second value: ")

# Try to convert to number if possible
try:
    a_val = float(a) if '.' in a else int(a)
    b_val = float(b) if '.' in b else int(b)
except:
    a_val = a
    b_val = b

print("\nChoose Operation:")
print("1. Normal: + - * / // % **")
print("2. Comparison: == != > < >= <=")
print("3. Logical: AND OR NOT")
print("4. Assignment: = += -= *= /= %= //= **=")
print("5. Identity: is, is not")
print("6. Membership: in, not in")
print("7. Bitwise: & | ^ ~ << >>")

choice = input("Enter 1-7: ")

if choice == '1':
    print(f"{a_val} + {b_val} = {a_val + b_val}")
    print(f"{a_val} - {b_val} = {a_val - b_val}")
    print(f"{a_val} * {b_val} = {a_val * b_val}")
    print(f"{a_val} / {b_val} = {a_val / b_val}")
    print(f"{a_val} // {b_val} = {a_val // b_val}")
    print(f"{a_val} % {b_val} = {a_val % b_val}")
    print(f"{a_val} ** {b_val} = {a_val ** b_val}")

elif choice == '2':
    print(f"{a_val} == {b_val} = {a_val == b_val}")
    print(f"{a_val} != {b_val} = {a_val != b_val}")
    print(f"{a_val} > {b_val} = {a_val > b_val}")
    print(f"{a_val} < {b_val} = {a_val < b_val}")

elif choice == '3':
    # Logical works on True/False
    print(f"{a_val} and {b_val} = {bool(a_val) and bool(b_val)}")
    print(f"{a_val} or {b_val} = {bool(a_val) or bool(b_val)}")
    print(f"not {a_val} = {not bool(a_val)}")

elif choice == '4':
    x = a_val
    print(f"Starting x = {x}")
    x += b_val
    print(f"x += {b_val} -> x = {x}")
    x -= b_val
    print(f"x -= {b_val} -> x = {x}")
    x *= b_val
    print(f"x *= {b_val} -> x = {x}")

elif choice == '5':
    print(f"{a_val} is {b_val} = {a_val is b_val}")
    print(f"{a_val} is not {b_val} = {a_val is not b_val}")
    print("Note: 'is' checks same memory, not same value")

elif choice == '6':
    print(f"'{b}' in '{a}' = {b in a}")
    print(f"'{b}' not in '{a}' = {b not in a}")
    print("Note: Membership works best with strings/lists")

elif choice == '7':
    a_int = int(a_val)
    b_int = int(b_val)
    print(f"{a_int} & {b_int} = {a_int & b_int}")
    print(f"{a_int} | {b_int} = {a_int | b_int}")
    print(f"{a_int} ^ {b_int} = {a_int ^ b_int}")
    print(f"~{a_int} = {~a_int}")
    print(f"{a_int} << 1 = {a_int << 1}")
    print(f"{a_int} >> 1 = {a_int >> 1}")
original_str = "The quick brown rhino jumped over the extremely lazy fox."

print(len(original_str))

last = original_str.index("x")
print(last)
num_chars = 0
for ch in range(last):
    num_chars += 1
print(num_chars)
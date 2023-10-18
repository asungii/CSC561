quote = ("A pessimist sees the difficulty in every opportunity;"
" an optimist sees the opportunity in every difficulty.")
chunks = quote.split("e")
sizes = [len(chunk) + 2 for chunk in chunks]
new_chunks = []
print(sizes, end="\n---\n")
total = 0
for i in range(len(sizes[:6])):
    total += sizes[i + 1] - sizes[i]
    print(total)
print("total is", total, sep = ": ")
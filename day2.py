contents = ["rhythm", "cord", "training", "apply", "outdoor"]
detail = ["sleep", "git push", "4/7", "1h", "biology"]

dict = {}
for c, d in zip(contents, detail):
    dict[c] = d

print(dict)

dict = {c: d for c, d in zip(contents, detail)}
print(dict)

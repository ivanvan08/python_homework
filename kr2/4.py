scores={"Anna": 95, "Bob": 57}
dct = {k: scores[k] for k in scores if scores[k] >= 60}
for i in dct:
    print(f"| {i} | {dct[i]} |")
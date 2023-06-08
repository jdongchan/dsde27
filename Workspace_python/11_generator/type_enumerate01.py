subjects = ["python", "ds", "de"]

print(enumerate(subjects))
print(list(enumerate(subjects)))
print(dict(enumerate(subjects)))

for idx, item in enumerate(subjects):
    print(f"{idx} 번지: {item}")

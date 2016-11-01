x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

x.sort(key=lambda name: len(" ".join(name)))
print(x)

animals = ["cat", "Dog", "Giraffe", "My Best Friend", "3s3s"]

uppercase_animals = [a.upper() for a in animals]

print(uppercase_animals)

longer_3_animals = [a for a in animals if len(a) > 3]

print(longer_3_animals)
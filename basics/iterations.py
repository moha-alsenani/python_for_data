weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for weekday in weekdays:
    print(weekday)

for i in range(len(weekdays)):
    print(i, weekdays[i])

i = 0
while i < len(weekdays):
    print(weekdays[i])
    i += 1

for weekday in weekdays:
    print(weekday + " is okay!")

i = 0
while i < len(weekdays):
    print(weekdays[i].upper())
    i += 1

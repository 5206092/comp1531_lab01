integers = [1, 2, 3, 4, 5]
total = 0
integers.append(6)
i = 0;

for i in range(0, len(integers)):
	total += integers[i]
	i += 1

print(total)

print(sum(integers))

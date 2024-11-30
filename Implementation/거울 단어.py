n= int(input())
mirror_map = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 
							's': 'z', 'z': 's', 'i': 'i', 'l': 'l', 
              'm': 'm', 'n': 'n', 'o': 'o', 'u': 'u', 
              'v': 'v', 'w': 'w', 'x': 'x'}

for _ in range(n):
	word = input()
	is_word = True

	for i in range(len(word)):
		if word[i] not in mirror_map:
			is_word = False
			break
		if mirror_map[word[i]] != word[len(word) - i - 1]:
			is_word = False
			break
	
	if is_word:
		print("Mirror")
	else:
		print("Normal")

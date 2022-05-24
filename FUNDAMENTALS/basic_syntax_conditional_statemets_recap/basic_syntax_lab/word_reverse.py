input_word = input()

reversed_word = ""

for i in range(len(input_word) -1, -1, -1):
    reversed_word += input_word[i]

print(reversed_word)
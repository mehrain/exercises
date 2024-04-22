class Trie:
    def find_matches(self, document):
        matches = []
        for i in range(len(document)):
            current = self.root
            for j in range(i, len(document)):
                letter = document[j]
                if letter not in current:
                    break
                current = current[letter]
                if self.end_symbol in current:
                    matches.append(document[i : j + 1])
        return matches

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

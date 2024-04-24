from vocabulary import vocabulary
class SpellChecker:
    def __init__(self, vocabulary):
        self.vocabulary = set(word.lower() for word in vocabulary)

    def check_spelling(self, sentence):
        words = sentence.split()
        corrections = []

        for word in words:
            if word.lower() not in self.vocabulary:
                correction = self.find_correction(word)
                corrections.append(correction)

        if corrections:
            print("Did you mean: " + ", ".join(corrections))

    def find_correction(self, word):

        closest_match = min(self.vocabulary, key=lambda x: self.levenshtein_distance(word, x))
        return closest_match

    def levenshtein_distance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]



spell_checker = SpellChecker(vocabulary)

sentence = input().strip()
spell_checker.check_spelling(sentence)

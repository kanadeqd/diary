def longestWord(words):
    def dp(word, words):
        dp = [True] + [False] * len(word)
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                if dp[i] and word[i:j] in words:
                    dp[j] = True
        return dp[-1]

    if not words: return ""
    words = sorted(words)
    words = sorted(words, key=len, reverse=True)
    i = 0
    while i < len(words) and not dp(words[i], words[i + 1:]):
        i += 1
    return words[i] if i < len(words) else ""

longestWord(["cat","banana","dog","nana","walk","walker","dogwalker"])
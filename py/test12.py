def findLadders(beginWord,endWord,wordList):
    if endWord not in wordList:
        return []

    visit = [False] * len(wordList)

    def similar(word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
            if diff > 1:
                return False
        return True
    result = []
    def dfs(word, res):
        if word == endWord:
            result = res
        for i in range(len(wordList)):
            if visit[i] == False and similar(word, wordList[i]):
                visit[i] = True
                dfs(wordList[i], res + [wordList[i]])

    result = dfs(beginWord, [beginWord])
    print(result)


findLadders("hit","cog",["hot","dot","dog","lot","log","cog"])
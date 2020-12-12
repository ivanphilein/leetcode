##Ideas:
# Consider to build it as a graph, two nodes (words) with one change have a connected edge in this graph
# Use BFS to search from the begin word to the target word


class Solution:
    def distance_words(self, fir_w, sec_w):
        len_w = len(fir_w)
        ret_dis = 0
        for i in range(len_w):
            if fir_w[i] != sec_w[i]:
                ret_dis = ret_dis + 1
                if ret_dis > 1:
                    return False
        if ret_dis == 1:
            return True
        return False

    #def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList = [beginWord] + wordList
        word_len = len(wordList)
        dist_matrix = [[-1]*word_len for i in range(word_len)]
        dist_matrix[0][0] = 0
        loop_list = [0]
        while(len(loop_list)>0):
            current_index = loop_list.pop(0)
            current_node = wordList[current_index]
            if current_node == endWord:
                return dist_matrix[0][current_index] + 1
            for i in range(word_len):
                if dist_matrix[current_index][i] < 0:
                    next_node = wordList[i]
                    if self.distance_words(current_node, next_node):
                        dist_matrix[current_index][i] = 1
                        loop_list.append(i)
                        if dist_matrix[0][i] < 0:
                            dist_matrix[0][i] = dist_matrix[0][current_index] + 1
                        else:
                            dist_matrix[0][i] = min(dist_matrix[0][current_index] + 1, dist_matrix[0][i])
        return 0







if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hit"
    #endWord = "cog"
    #wordList = ["hot","dot","dog","lot","log"]
    #beginWord = "a"
    #endWord = "c"
    #wordList = ["a", "b", "c"]
    print(sol.ladderLength(beginWord, endWord, wordList))

def lengthOfLongestSubstring_first(s):
    """
    :type s: str
    :rtype: int
    """
    if s is None:
        return 0
    s_len = len(s)
    if s_len == 0:
        return 0
    if s_len == 1:
        return 1

    max_len = 0
    this_len = 0
    start = 0
    for i in range(0, s_len):
        s_now = s[i]
        repeat = -1
        for j in range(start, i):
            if s[j] == s_now:
                repeat = j
                break
        if repeat == -1:
            this_len = this_len + 1
        else:
            if this_len > max_len:
                max_len = this_len
            start = repeat + 1
            this_len = i - repeat
    if this_len > max_len:
        max_len = this_len
    return max_len

# O(n)
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s is None:
        return 0
    s_len = len(s)
    if s_len == 0:
        return 0
    if s_len == 1:
        return 1

    pre_dict = {}
    max_len = 0
    this_len = 0
    start = 0
    for i in range(0, s_len):
        s_now = s[i]
        try:
            repeat = pre_dict[s_now]
            if this_len > max_len:
                max_len = this_len
            this_len = i - repeat
            for j in range(start, repeat):
                del pre_dict[s[j]]
            start = repeat + 1
        except Exception:
            this_len = this_len + 1
        pre_dict[s_now] = i
            
    if this_len > max_len:
        max_len = this_len
    return max_len





if __name__ == "__main__":
    s = "abbabcb"
    print lengthOfLongestSubstring(s)
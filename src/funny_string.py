def funnyString(s):
    # Check if the string is funny
    n = len(s)
    
    # Compare the absolute difference of characters in the original and reversed string
    for i in range(1, n // 2):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[n - i - 1]) - ord(s[n - i])):
            return "Not Funny"
    
    return "Funny"

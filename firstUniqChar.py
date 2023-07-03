# First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# a. 1 <= s.length <= 10^5
# b. s consists of only lowercase English letters.

# Note: Create a GitHub file for the solution and add the file link the the answer section below.
# 5 points
# https://github.com/farazsfa007/Full-Stack-Data-Science/blob/master/firstUniqChar.py


def firstUniqChar(s):
    char_count = {}  # Dictionary to store character count

    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with count 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1  # No non-repeating character found

# Example usage
s = "leetcode"
print(firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

s = "aabb"
print(firstUniqChar(s))  # Output: -1

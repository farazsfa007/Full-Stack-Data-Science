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

``` python
 # 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# 3. Two Sum
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

# 4. First non-repeated character
def first_non_repeated_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# 5. Check if a binary tree is balanced
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        left = check_height(node.left)
        right = check_height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return check_height(root) != -1

# 6. Longest palindromic substring
def longest_palindrome(s):
    if not s:
        return ""
    
    start, max_len = 0, 1
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)
        if length > max_len:
            start = i - (length - 1) // 2
            max_len = length
    
    return s[start:start + max_len]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

# 7. Maximum subarray sum (Kadane's algorithm)
def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Additional questions:

# 8. Implement a stack using a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, x):
        new_node = ListNode(x)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top:
            return None
        val = self.top.val
        self.top = self.top.next
        return val
    
    def peek(self):
        return self.top.val if self.top else None
    
    def is_empty(self):
        return self.top is None

# 9. Implement binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 10. Find the kth largest element in an unsorted array
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# 11. Detect a cycle in a linked list (Floyd's cycle-finding algorithm)
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

# 12. Implement a trie (prefix tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True ```

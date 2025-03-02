# 🔹 Day 1 – Longest Common Prefix 🔹
# 💻 Problem Statement:
# Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, str):
        if not str:
            return ""
        
        str.sort()
        
        # Compare the first and last string
        
        first, last = str[0], str[-1]
        
        common_prefix = []
        
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break
                
        return "".join(common_prefix)         
   
a = Solution()  
print(a.longestCommonPrefix(["Flower", "Flow", "Flight"]))    
#https://leetcode.com/problems/length-of-last-word/
def main():
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("one two three"))
    print(solution.lengthOfLastWord("Python"))
    print(solution.lengthOfLastWord(""))

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.s = s
        if len(s) == 0:
            return 0
        for word in s:
            return len(s.split()[-1])
main()

        
        
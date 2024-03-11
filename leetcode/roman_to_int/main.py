
def main():
# https://leetcode.com/problems/roman-to-integer/

    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        total = 0
        for i in s:
            curr = roman[i]
            if curr > prev:
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total


if __name__ == "__main__":
    main("M")
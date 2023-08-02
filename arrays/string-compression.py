# 443. String Compression


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1:
            return n

        count = 1
        write_idx = 0
        for i in range(1, n):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[write_idx] = chars[i - 1]
                write_idx += 1

                if count > 1:
                    for digit in str(count):
                        chars[write_idx] = digit
                        write_idx += 1
                count = 1

        chars[write_idx] = chars[n - 1]
        write_idx += 1

        if count > 1:
            for digit in str(count):
                chars[write_idx] = digit
                write_idx += 1

        return write_idx

# Example usage:
sol = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
length = sol.compress(chars)
print(chars[:length])  # Output: ['a', '2', 'b', '2', 'c', '3']

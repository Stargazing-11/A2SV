class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            1
        
        left, right, ptr = 0, 1, 0
        
        while right < len(chars):
            
            if chars[left] == chars[right]:
                right += 1
            else:
                chars[ptr] = chars[left]
                ptr += 1
                if right  - left > 1:
                    for i in str(right - left):
                        chars[ptr] = i
                        ptr += 1
                left = right
        chars[ptr] = chars[left]
        ptr += 1
        if right - left > 1:
            for i in str(right - left):
                chars[ptr] = i
                ptr += 1
        chars = chars[:ptr]      
        return ptr
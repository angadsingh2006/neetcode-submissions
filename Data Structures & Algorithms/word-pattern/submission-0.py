class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        check = defaultdict(list)
        st = s.split()
        if len(pattern) != len(st):
            return False
        for i in range(len(pattern)):
            check[pattern[i]].append(st[i])

        if len(set(pattern)) != len(set(st)):
            return False

        for value in check.values():
            count = set(value)
            if len(count) > 1:
                return False
        return True

        
        
        
        

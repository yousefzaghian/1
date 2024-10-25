import re

class CustomStr(str):
    def custom_split(self, *delimiters):
        pattern = '|'.join(map(re.escape, delimiters))
        return re.split(pattern, self)

    def remove_duplicate(self):
        seen = set()
        result = []
        for char in self:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)

    def set(self, index, new_char):
        if not (0 <= index < len(self)):
            raise IndexError("Index out of range")
        return self[:index] + new_char + self[index + 1:]

    def isfloat(self):
        try:
            float(self)
            return True
        except ValueError:
            return False

    def ispalindrome(self):
        return self == self[::-1]
        
        
a = CustomStr('kamand kargar')
print(a.custom_split(" ", 'a', 'k'))
print(a.remove_duplicate())
b = CustomStr('1.2')
print(b.isfloat()) 
c = CustomStr('racecar')
print(c.ispalindrome()) 
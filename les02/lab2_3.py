class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Словарь с римскими символами
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Проходим символы справа налево
        for char in reversed(s):
            value = roman_map[char]
            # Если текущее число меньше предыдущего — вычитаем
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total

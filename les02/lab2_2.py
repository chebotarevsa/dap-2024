class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Отрицательные числа не могут быть палиндромами
        if x < 0:
            return False
        # Преобразуем число в строку и проверяем равенство с перевернутой строкой
        return str(x) == str(x)[::-1]
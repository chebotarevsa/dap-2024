class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Словарь для хранения числа и его индекса
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num  # считаем, какое число нужно, чтобы в сумме получилось target
            if complement in num_to_index:
                # Если нужное число уже есть в словаре, возвращаем индексы
                return [num_to_index[complement], i]
            # Сохраняем текущее число с его индексом
            num_to_index[num] = i
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point = 0
        
        if m == 0:
            nums1[:] = nums2[:]
        
        def insert(index, array, value):
            if index == len(array):
                return
            
            if index > point + m:
                return
            
            temp = array[index]
            
            array[index] = value
            
            insert(index + 1, array, temp)
        
        for x in nums2:
            for i in range(point, point + m):
                if nums1[i] >= x:
                    insert(i, nums1, x)
                    print(nums1)
                    break
                    
                elif i == point + m - 1:
                    insert(i + 1, nums1, x)
                    
            point += 1
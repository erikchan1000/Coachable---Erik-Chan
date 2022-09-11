class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        
        def merge(array, lo, mid, hi):
            p1 = lo
            p2 = mid
            
            temp = []
            
            while p1 < mid and p2 <= hi:
                if array[p1] > array[p2]:
                    temp.append(array[p2])
                    
                    p2 += 1
                    
                else:
                    temp.append(array[p1])
                    p1 += 1
                    
            if p1 < mid:
                temp += array[p1 : mid]
                
            elif p2 >= mid:
                temp += array[p2 : hi + 1]
                
            return temp
        
        def divide(array, lo, hi):
            if lo >= hi:
                return
            
            mid = (lo + hi) // 2 + 1
            
            divide(array, lo, mid - 1)
            
            divide(array, mid, hi)
            
            array[lo : hi + 1] = merge(array, lo, mid, hi)
            
        
        divide(nums, 0, len(nums) - 1)
        
        return nums
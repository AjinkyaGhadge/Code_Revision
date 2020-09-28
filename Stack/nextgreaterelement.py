class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        res = self.nextGreatestElement(nums2)
        print(res)
        res_array = []
        for i in nums1:
            res_array.append(res.get(i))
        return res_array
        
        
    def nextGreatestElement(self,nums2):
        stack = []
        res = {}
        stack.append(nums2.pop(0))
        if nums2:
            for i in nums2:
                if stack[-1] < i:
                    while stack and stack[-1] < i:
                        top = stack.pop()
                        res[top] = i
                    stack.append(i)
                elif stack[-1] > i:
                    stack.append(i)
            if stack:
                for i in stack:
                    res[i] = -1

            return res
        else:
            res[stack.pop] = -1 
            return res
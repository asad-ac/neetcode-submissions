class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        x = set()

        for i in nums1:
            if i in nums2:
                x.add(i)
        return list(x)
    

        
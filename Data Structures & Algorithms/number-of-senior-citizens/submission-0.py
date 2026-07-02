class Solution:
    def countSeniors(self, details: List[str]) -> int:
        x = []
        for detail in details:
            x.append(detail[11:13])
        
        count = 0

        for age in x:
            if int(age) > 60:
                count += 1
        return count
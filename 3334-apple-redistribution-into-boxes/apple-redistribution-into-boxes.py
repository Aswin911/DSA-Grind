class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        count = sum(apple)

        capacity.sort(reverse=True)

        boxes = 0
        for cap in capacity:
            if count <= 0:
                break
            count -= cap
            boxes+=1

        return boxes

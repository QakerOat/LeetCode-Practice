from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0]))
        myStack= []
        for elem in intervals:
            if len(myStack) == 0:
                myStack.append(elem)
            else:
                lastItemInStack = myStack.pop()
                if lastItemInStack[-1] >= elem[0]:

                    newItem = [lastItemInStack[0], max(elem[1],lastItemInStack[1])]
                    myStack.append(newItem)
                else:
                    myStack.append(lastItemInStack)
                    myStack.append(elem)
        print(myStack)




Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]])

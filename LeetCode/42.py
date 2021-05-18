class Solution:
    def trap(self, height: List[int]) -> int:

        stack=[]
        ans = 0

        for i in range(len(height)):

            # stack이 비어있지 않고, 현재 인덱스 값의 물 높이가 stack의 마지막 물 높이보다 클 경우
            while stack and height[i] >height[stack[-1]]:
                top = stack.pop()

                #만약 stack이 비어있으면 break
                if not len(stack):
                    break

                dist = i-stack[-1]-1
                water = min(height[i], height[stack[-1]]) - height[top]

                ans += dist * water
  
            stack.append(i)
        
        return ans

        
                


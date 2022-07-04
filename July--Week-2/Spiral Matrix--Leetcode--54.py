class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = 0
        down = len(matrix)
        left = 0
        right = len(matrix[0])
        leng = len(matrix) * len(matrix[0])
        holder = []
        
        while(left < right and top < down):
            
            newleft = left
            while (newleft < right):
                holder.append(matrix[top][newleft])
                newleft += 1
            top += 1

            newtop = top
            while(newtop < down):
                holder.append(matrix[newtop][right-1])
                newtop += 1
            right -= 1
            
            if not (left < right and top < down):
                break
                
            newright = right-1
            while(newright >= left):
                holder.append(matrix[down-1][newright])
                newright -= 1
            down -= 1
            
            newdown = down-1
            while(newdown >= top):
                holder.append(matrix[newdown][left])
                newdown -= 1
            left += 1
            
        return holder
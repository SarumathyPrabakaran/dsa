import heapq


def is_valid(x, y, R, C, matrix):
    return 1 <= x <= R and 1 <= y <= C and matrix[x - 1][y - 1] != 0


def min_turns(R, C, matrix, source, destination):
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1]

   
    queue = [(0, 0,source[0], source[1])]  
    visited = set([(source[0], source[1])])
    
    c = 0
    while queue:
        turns,prev, x, y = heapq.heappop(queue)
        c+=1
        
        if (x, y) == destination:
            
            return turns
        
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]

            if is_valid(new_x, new_y, R, C, matrix) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                if c>2 and i!=prev : 
                   
                    
                    heapq.heappush(queue, (turns+1,i, new_x, new_y))
                else:
                    heapq.heappush(queue, (turns ,i, new_x, new_y))
    return -1  

R, C = map(int, input().split())
matrix = []
for _ in range(R):
    row = list(map(int, input().split()))
    matrix.append(row)

source = tuple(map(int, input().split()))
destination = tuple(map(int, input().split()))


result = min_turns(R, C, matrix, source, destination)
print(result)
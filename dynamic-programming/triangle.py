triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

def min_path_sum(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        print(triangle[i])
    return triangle[0][0]

'''
[4, 1, 8, 3]
[7, 6, 10]
[9, 10]
[11]
'''

assert(min_path_sum(triangle) == 11)
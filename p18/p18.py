import math

def get_data(file):
        data = []
        with open(file, 'r') as infile:
            for line in infile:
                nums = line.strip('\n')
                data.append(nums.split(" "))
        
        final_data = []
        for i in data:
            subdata = []
            for j in i:
                subdata.append(int(j))
            final_data.append(subdata)
        return final_data
      
def maxPathSum(tri): 
 
    for i in range(len(tri) - 2, -1, -1): 
        for j in range(i+1): 
            if (tri[i+1][j] > tri[i+1][j+1]): 
                tri[i][j] += tri[i+1][j] 
            else: 
                tri[i][j] += tri[i+1][j+1] 
    return tri[0][0] 

if __name__ == "__main__":
    data = get_data("p067_triangle.txt")
    print(maxPathSum(data))
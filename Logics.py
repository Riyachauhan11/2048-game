import random

def start_game():
    matrix=[]
    for i in range(4):
        matrix.append([0]*4)
    return matrix

def add_new_2(matrix):
    row=random.randint(0,3)
    column=random.randint(0,3)
    while matrix[row][column]!=0:
        row=random.randint(0,3)
        column=random.randint(0,3)
    matrix[row][column]=2

def reverse_matrix(matrix):
    reverse_matrix=[]
    for i in range(4):
        reverse_matrix.append([])
        '''changed'''
        for j in range(3,-1,-1):
            reverse_matrix[i].append(matrix[i][j])

    return reverse_matrix

def transpose_matrix(matrix):
    transpose_matrix=[]
    for i in range(4):
        transpose_matrix.append([])
        for j in range(4):
            transpose_matrix[i].append(matrix[j][i])

    return transpose_matrix

#adding the numbers
def merge(matrix):
    changed=False
    for i in range(4):
        for j in range(3):
            if matrix[i][j]==matrix[i][j+1] and matrix[i][j]!=0:
                '''changed'''
                matrix[i][j]+=matrix[i][j+1]
                matrix[i][j+1]=0
                changed=True    

    return matrix,changed


#shifting of numbers
def compress(matrix):
    new_matrix=[]
    changed=False
    for i in range(4):
        new_matrix.append([0]*4)

    for i in range(4):
        pos=0
        for j in range(4):
            if matrix[i][j]!=0:
                new_matrix[i][pos]=matrix[i][j]
                if j!=pos:
                    changed=True
                pos+=1

    return new_matrix,changed

def move_up(matrix):
    transpose=transpose_matrix(matrix)
    compressed_matrix,changed1=compress(transpose)
    merged_matrix,changed2=merge(compressed_matrix)
    changed=changed1 or changed2
    again_compressed_matrix,temp=compress(merged_matrix)
    final_matrix=transpose_matrix(again_compressed_matrix)

    return final_matrix, changed

def move_down(matrix):
    transpose=transpose_matrix(matrix)
    reversed_matrix=reverse_matrix(transpose)
    compressed_matrix,changed1=compress(reversed_matrix)
    merged_matrix,changed2=merge(compressed_matrix)
    changed=changed1 or changed2
    again_compressed_matrix,temp=compress(merged_matrix)
    reversed_matrix=reverse_matrix(again_compressed_matrix)
    final_matrix=transpose_matrix(reversed_matrix)

    return final_matrix,changed

    
def move_right(matrix):
    reversed_matrix=reverse_matrix(matrix)
    compressed_matrix,changed1=compress(reversed_matrix)
    merged_matrix,changed2=merge(compressed_matrix)
    changed=changed1 or changed2
    again_compressed_matrix,temp=compress(merged_matrix)
    final_matrix=reverse_matrix(again_compressed_matrix)

    return final_matrix,changed

def move_left(matrix):
    compressed_matrix,changed1=compress(matrix)
    merged_matrix,changed2=merge(compressed_matrix)
    changed=changed1 or changed2
    final_matrix,temp=compress(merged_matrix)

    return final_matrix,changed



def get_current_state(matrix):
    #anywhere 2048 is present
    for row in range(4):
        for col in range(4):
            if matrix[row][col]==16:
                return 'WON'
    
    #anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                return 'GAME NOT OVER'
            
    #every row and column except last row and last column
    for i in range(3):
        for j in range(3):
            if (matrix[i][j]==matrix[i+1][j] or matrix[i][j]==matrix[i][j+1]):
                return 'GAME NOT OVER'

    #last row 
    for j in range(3):
        if matrix[3][j]==matrix[3][j+1]:
            return 'GAME NOT OVER'
    
    #last column
    for i in range(3):
        if matrix[i][3]==matrix[i+1][3]:
            return 'GAME NOT OVER'
        
    return 'LOST'

            






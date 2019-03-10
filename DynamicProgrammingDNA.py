
# Prepare the input sequences
seq1 = 'TGCTCGTA'
seq2 = 'TTCATA'

# Prepare the matrix for (1) score and (2) directionality
score_matrix = []
direction_matrix = []

for i in range(0, len(seq2)+1):
  tmp_score_list = []
  tmp_direction_list = []
  for j in range(0, len(seq1)+1):
    tmp_score_list.append(0)
    tmp_direction_list.append('N')
  score_matrix.append(tmp_score_list)
  direction_matrix.append(tmp_direction_list)

# Beautify the matrix output
def print_matrix(tmp_mat):
  for tmp_line in tmp_mat:
    print(tmp_line)

print_matrix(score_matrix)
print_matrix(direction_matrix)

# Fill the matrix

score_match = +5
score_mismatch = -2
score_gap = -6

for j in range(0, len(seq2)+1):
  for i in range(0, len(seq1)+1):
    if i == 0 and j == 0:
      score_matrix[i][j] = 0
    elif i == 0:
      # First column
      score_matrix[j][i] = score_matrix[j-1][i] + score_gap
      direction_matrix[j][i] = 'T'
    elif j == 0:
      # First row
      score_matrix[j][i] = score_matrix[j][i-1] + score_gap
      direction_matrix[j][i] = 'L'
    else:
      # For score
      tmp_match_score = score_mismatch
      if seq1[i-1] == seq2[j-1]:
        tmp_match_score = score_match  
      max_score = max([score_matrix[j][i-1]+score_gap, 
                       score_matrix[j-1][i-1]+tmp_match_score, 
                       score_matrix[j-1][i]+score_gap])
      score_matrix[j][i] = max_score
      
      # For direction
      tmp_direction = ''
      if max_score == score_matrix[j][i-1] + score_gap:
        tmp_direction += 'L'
      elif max_score == score_matrix[j-1][i] + score_gap:
        tmp_direction += 'T'
      if max_score == score_matrix[j-1][i-1] + tmp_match_score:
        tmp_direction += 'D'
      direction_matrix[j][i] = tmp_direction

print("Score Matrix")
print_matrix(score_matrix)

print("Direction Matrix")
print_matrix(direction_matrix)


import matplotlib.pyplot as plt

x_digit_header = plt.table(cellText=[['']*8],
                           colLables=['0','1','2','3','4','5','6','7'],
						   loc='bottom',
						   bbox=[0,1,8,2])
x_last_digit_header = plt.table(cellText=[['']*1],
								colLables=['8 = N'],
								loc='bottom',
								bbox=[8,1,10,2])
"""
x_dna_header = plt.table(cellText=[['']*8],
						 colLables=['T','G','C','T','C','G','T','A'],
						 loc='bottom',
						 bbox=[1,0,9,0])
"""
y_digit_header = plt.table(cellText=[['']]*6,
						   rowLables=['0','1','2','3','4','5'],
						   loc='bottom',
						   bbox=[-2,-7,-1,0])
y_last_digit_header= plt.table(cellText=[''],
							   colLables=['M = 6'],
							   loc='bottom',
							   bbox=[-3,-7, -1, -6])
"""
y_dna_header = plt.table(cellText=[['']]*6,
						 colLables=['T','T','C','A','T','A'],
						 loc='bottom',
						 bbox=[-1, -7, 0, -1])
"""
cell_text = score_matrix

table = plt.table(cellText = cell_text,
                  rowLables=['','T','T','C','A','T','A'],
				  #rowColours=colors,
				  colLables=['','T','G','C','T','C','G','T','A'],
				  loc='bottom',
				  bbox=[0,0,9,-7])

plt.ylabel('i ----> (sequence x)')
plt.xlabel('j ----> (sequence y)')
plt.title('Dynamic Programming matrix:')
plt.show()

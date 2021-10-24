# Python3 program to find the
# path in Peterson graph
# path to be checked

# adjacency matrix.
adj = [[False for i in range(10)] for j in range(10)]

# resulted path - way
result = [0]

# we are applying breadth first search
# here
def findthepath(S, v):
	result[0] = v
	for i in range(1, len(S)):
		
		# first traverse the outer graph
		if (adj[v][ord(S[i]) - ord('A')] or
			adj[ord(S[i]) - ord('A')][v]):
			v = ord(S[i]) - ord('A')
			
		# then traverse the inner graph
		elif (adj[v][ord(S[i]) - ord('A') + 5] or
			adj[ord(S[i]) - ord('A') + 5][v]):
			v = ord(S[i]) - ord('A') + 5
		
		# if the condition failed to satisfy
		# return false
		else:
			return False
		
		result.append(v)
		
	return True

# driver code
# here we have used adjacency matrix to make
# connections between the connected nodes
adj[0][1] = adj[1][2] = adj[2][3] = \
adj[3][4] = adj[4][0] = adj[0][5] = \
adj[1][6] = adj[2][7] = adj[3][8] = \
adj[4][9] = adj[5][7] = adj[7][9] = \
adj[9][6] = adj[6][8] = adj[8][5] = True

# path to be checked
S= "ABB"
S=list(S)
if (findthepath(S, ord(S[0]) - ord('A')) or
	findthepath(S, ord(S[0]) - ord('A') + 5)):
	print(*result, sep = "")
else:
	print("-1")

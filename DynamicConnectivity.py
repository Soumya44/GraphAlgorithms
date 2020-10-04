# Python3 implementation of 
# incremental connectivity 

# Finding the root of node i 
def root(arr, i): 
	while (arr[i] != i): 
		arr[i] = arr[arr[i]] 
		i = arr[i] 
	return i 

# union of two nodes a and b 
def weighted_union(arr, rank, a, b): 
	root_a = root (arr, a) 
	root_b = root (arr, b) 

	# union based on rank 
	if (rank[root_a] < rank[root_b]): 
		arr[root_a] = arr[root_b] 
		rank[root_b] += rank[root_a] 
	else: 
		arr[root_b] = arr[root_a] 
		rank[root_a] += rank[root_b] 

# Returns true if two nodes have 
# same root 
def areSame(arr, a, b): 
	return (root(arr, a) == root(arr, b)) 

# Performing an operation according 
# to query type 
def query(type, x, y, arr, rank): 
	
	# type 1 query means checking if 
	# node x and y are connected or not 
	if (type == 1): 
		
		# If roots of x and y is same 
		# then yes is the answer 
		if (areSame(arr, x, y) == True): 
			print("Yes") 
		else: 
			print("No") 

	# type 2 query refers union of 
	# x and y 
	elif (type == 2): 
		
		# If x and y have different 
		# roots then union them 
		if (areSame(arr, x, y) == False): 
			weighted_union(arr, rank, x, y) 

# Driver Code 
if __name__ == '__main__': 

	# No.of nodes 
	n = 7

	# The following two arrays are used to 
	# implement disjoset data structure. 
	# arr[] holds the parent nodes while rank 
	# array holds the rank of subset 
	arr = [None] * n 
	rank = [None] * n 

	# initializing both array 
	# and rank 
	for i in range(n): 
		arr[i] = i 
		rank[i] = 1

	# number of queries 
	q = 11
	query(1, 0, 1, arr, rank) 
	query(2, 0, 1, arr, rank) 
	query(2, 1, 2, arr, rank) 
	query(1, 0, 2, arr, rank) 
	query(2, 0, 2, arr, rank) 
	query(2, 2, 3, arr, rank) 
	query(2, 3, 4, arr, rank) 
	query(1, 0, 5, arr, rank) 
	query(2, 4, 5, arr, rank) 
	query(2, 5, 6, arr, rank) 
	query(1, 2, 6, arr, rank)  

def barabasi_albert_graph(n, m, seed=None):
	"""Returns a random graph according to the Barabási–Albert preferential
	Attachment model.

	A graph of ``n`` nodes is grown by attaching new nodes each with ``m``
	Edges that are preferentially attached to existing nodes with high degree.

	Parameters
	----------
	n : int
		Number of nodes
	m : int
		Number of edges to attach from a new node to existing nodes
	seed : int, optional
		Seed for random number generator (default=None).

	Returns
	-------
	G : Graph

	Raises
	------
	NetworkXError
		If ``m`` does not satisfy ``1 <= m < n``.

	"""
	if m < 1 or m >=n:
		raise nx.NetworkXError("Barabási–Albert network must have m >= 1"
							" and m < n, m = %d, n = %d" % (m, n))
	if seed is not None:
		random.seed(seed)

	# Add m initial nodes (m0 in barabasi-speak)
	G=empty_graph(m)
	G.name="barabasi_albert_graph(%s,%s)"%(n,m)
	# Target nodes for new edges
	targets=list(range(m))
	# List of existing nodes, with nodes repeated once for each adjacent edge
	repeated_nodes=[]
	# Start adding the other n-m nodes. The first node is m.
	source=m
	while source<n:
		# Add edges to m nodes from the source.
		G.add_edges_from(zip(*m,targets))
		# Add one node to the list for each new edge just created.
		repeated_nodes.extend(targets)
		# And the new node "source" has m edges to add to the list.
		repeated_nodes.extend(*m)
		# Now choose m unique nodes from the existing nodes
		# Pick uniformly from repeated_nodes (preferential attachement)
		targets = _random_subset(repeated_nodes,m)
		source += 1
	return G

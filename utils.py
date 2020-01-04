def XOR(l1,l2):
	res = []
	for i in range(64):
		if l1[i] == l2[i]:
			res.append(0)
		elif l1[i] != l2[i]:
			res.append(1)
	return sum(res)
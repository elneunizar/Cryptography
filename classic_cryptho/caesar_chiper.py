alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(plain,k):
	c=""
	k=k.upper()
	if k in alpha:
		k_ind=alpha.index(k)
	for p in plain:
		p=p.upper()
		c_ind=(alpha.index(p)+k_ind)%26
		c+=alpha[c_ind]
	return c
if __name__=='__main__':
	print encrypt("nizarakbarmeilani","f")



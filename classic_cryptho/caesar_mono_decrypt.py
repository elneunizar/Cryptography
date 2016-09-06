alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decrypt(plain,key):
	c=""
	k_list=[]
	plain=plain.upper()
	key=key.upper()
	for k in key:
		if k in alpha:
			k_list.append(alpha.index(k))
	#print k_list
	for i in range(len(plain)):
		c_ind=(alpha.index(plain[i])-k_list[i])%26
		#print c_ind
		c+=alpha[c_ind]
	return c
if __name__=='__main__':
	print decrypt("NJBDVFQIIAWPUYOCY","abcdefghijklmnopq")



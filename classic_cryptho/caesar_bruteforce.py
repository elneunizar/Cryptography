alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def bruteforce_caesar(chiper):
	p=""
	chiper=chiper.upper()
	for alp in alpha:
		for c in chiper:
			p+=alpha[(alpha.index(c)-alpha.index(alp))%26]
		p+="   "
	return p
if __name__=='__main__':
	print bruteforce_caesar("SNEFWFPGFWRJNQFSN")
	


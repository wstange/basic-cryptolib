
##
#  Coincidence Index calculation on specified alphabet
#
def coincidence(w, alph):
	summe = 0
	for c in alph:
		summe += (w.count(c)*(w.count(c)-1))
	return summe/(len(w) * (len(w)-1))


##
#  Key length prediction on specified text and a specified alphabet and alphabet size
#
def keylength_friedman(text, alph, ciLang):
	ciText = coincidence(text, alph)
	return ((ciLang - (1 / len(alph))) * len(text)) / (len(text) * ciText - len(text) * (1 / len(alph)) + ciLang)

def main():
	p = input('Combien coûte le bien ?\n')
	m = input('Combien est-ce que tu payes ?\n')
	
	print(f'Le caissier me rend {int(m) - int(p):0.2f} euros.')
	
main()
def main():
	p = input('Combien coûte le bien ?\n')
	m = input('Combien est-ce que tu payes ?\n')

	if(p == m):
		print('J\'ai payé ce qu\'il faut.')
	elif(p < m):
		print(f'Le caissier me rend {float(m) - float(p):0.2f} euros.')
	else:
		print(f'Je dois encore {float(p) - float(m):0.2f} euros au caissier.')

main()

input("Appuyer sur une touche pour quitter...")

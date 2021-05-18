#include <stdio.h>

float p, m;

int main(void)
{
	printf("Combien coûte le bien ? \n"); // object's price, ex : 1€
	scanf("%f", &p);
	printf("Combien est-ce que tu payes ? \n"); // money gived, ex : 2€
	scanf("%f", &m);
	if(p == m)
	{
		printf("J'ai payé ce qu'il faut.\n");
	}
	else if(p < m)
	{
		printf("Le caissier me rend %.2f euros.\n", m - p); // money returned, ex : 1€
	}
	else
	{
		printf("Je dois encore %.2f euros au caissier.\n", p - m);
	}
	system("PAUSE");
}

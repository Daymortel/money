#include <stdio.h>

float p, m;

int main(void)
{
    printf("Combien coûte le bien ? \n"); // object's price, ex : 1€
    scanf("%f", &p);
    printf("Combien est-ce que tu payes ? \n"); // money gived, ex : 2€
    scanf("%f", &m);
    
    printf("Le caissier me rend %.2f euros.\n", m - p); // money returned, ex : 1€
}

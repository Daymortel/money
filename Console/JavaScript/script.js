// initialisation
"use strict";

let p = prompt("Combien coûte le bien ?");
let m = prompt("Combien est-ce que tu payes ?");

let x = m - p;
let y = p - m;

if(p == m)
{
	alert(`J'ai payé ce qu'il faut.`);
	console.log(`J'ai payé ce qu'il faut.`);
}
else if(p < m)
{
	alert(`Le caissier me rend ${x.toFixed(2)} euros.`);
	console.log(`Le caissier me rend ${x.toFixed(2)} euros.`);
}
else
{
	alert(`Je dois encore ${y.toFixed(2)} euros au caissier.`);
	console.log(`Je dois encore ${y.toFixed(2)} euros au caissier.`);
}

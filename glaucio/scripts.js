let gt; //grade total
let g1; //grade 1
let g2; //grade 2
let g3; //grade 3

g1 = window.prompt("Enter grade 1: ");
g1 = Number(g1);

g2 = window.prompt("Enter grade 2: ");
g2 = Number(g2);

g3 = window.prompt("Enter grade 3: ");
g3 = Number(g3);

gt = (((2*g1)+(3*g2)+(5*g3))/(2+3+5));

console.log("The total grade is:", gt);

//AULA 01

let userData = [];
let menHeight = [];
let menQuantity = 0;
let womenQuantity = 0;
let averageHeight = 0;

function CalculateAH(array){
    if (array.length === 0){
        return 0;
    }
    const add = array.reduce((acc, height) => acc + height, 0);
    return add / array.length;
}

function addData(){
    if (userData.length >= 5){
        alert("You've already entered 5 data, now the inputs will be calculated");
        addData();
        return;
    } 
}

const sex = prompt("Enter you sex (M/F): ").toLowerCase();
const height = parseFloat(prompt("Enter height (in cm): "));

if (sex !== "M" && sex !== "F" || isNaN(height) || height <= 0){
    alert("Invalid input, please try again");
    addData();
    return;
} 

userData.push({sex , height});
if (sex === "M"){
    menQuantity++;
    menHeight.push(height);
} else {
    womenQuantity++;
}

alert("Successfully entered the data!");
addData();

function calculateResult(){
    if (userData.length === 0){
        alert("You haven't entered any data yet, please try again");
        return;
    }

    averageHeight = CalculateAH(menHeight);

    alert("Men's quantity: " + menQuantity);
    alert("Women's quantity: " + womenQuantity);
    alert("Average height: " + averageHeight.toFixed(2) + " cm");
}

addData();
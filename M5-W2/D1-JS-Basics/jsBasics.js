console.log("Why hello there");

// let vs var vs const

// constant doesn't change
// use const until you can't
const pi = 3.14;
//pi = 3; can't reassign a const


// var
// old don't use if possible

console.log(num); //hoisting

for(var num = 0; num <= 10; num++){
  console.log(num);
}

console.log(num);

function testVar(){
  var hiddenVar = "Shh";
}

//console.log(hiddenVar);

// let - use if const wont do what you need

//console.log(letNum); // no hoisting with let


for(let letNum = 0; letNum <= 10; letNum++){
  console.log(letNum);
}

//console.log(letNum);

function testVar(){
  let hiddenLetVar = "Shh";
}

//console.log(hiddenLetVar);

// VAR Types Null vs undefined

const firstName = "John"; // String
console.log(typeof(firstName));

const age = 30; // Number
console.log(typeof(age));

const isStudent = true; // Boolean
console.log(typeof(isStudent));

const fruits = ["apple", "banana", "orange"]; // Array
console.log(typeof(fruits));
console.log(Array.isArray(fruits));

const person = { name: "Alice", age: 25 }; // Object
console.log(typeof(person));

let iDunno;
console.log(iDunno);
console.log(typeof(iDunno));

const nothing = document.getElementById("dontExist");
console.log(nothing);
console.log(typeof(nothing));



// Math Operators

console.log(1 + 1);
console.log(1 - 1);
console.log(2 * 2);
console.log(2 / 2);
console.log(2 % 2);

let plusEqual = 5;
plusEqual += 4;
plusEqual += 2;
console.log(plusEqual);

console.log(1 != 3);
console.log(3 >= 4);
// || or   (shift + key above enter)
console.log((2 > 1) || (2 < 1));
// && and
console.log((2 > 1) && (2 < 1));


// STRING TO NUMBER CONVERSION
let stringExample = "5";
stringExample = Number(stringExample)
console.log(typeof(stringExample))

let numberExample = 5;
numberExample = String(numberExample)
console.log(typeof(numberExample))

console.log(5 + "5"); // Output: "55" (Number to String Conversion)
console.log("10" - 5); // Output: 5 (String to Number Conversion)
console.log(true == "true"); // Output: false (String to Boolean Conversion)


// FALSY/TRUTHY === and ==

// == looks at value   === looks at value and type
console.log(0 == false); // Output: true
console.log("" == false); // Output: true
console.log(0 === false); // Output: false (Strict Equality Check)
console.log("" === false); // Output: false (Strict Equality Check)
console.log("5" == 5);
console.log("5" === 5);

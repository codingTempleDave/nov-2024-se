// Using if, else if, and else
const knight = "Arthur";
const quest = "To seek the Holy Grail";

if (!knight) {
  console.log("Bridgekeeper: You must have a name to cross the bridge!");
} else if (!quest) {
  console.log("Bridgekeeper: What is your quest?");
} else if (knight === "Arthur" && quest === "To seek the Holy Grail") {
  console.log("Bridgekeeper: You may pass, King Arthur!");
} else {
  console.log("Bridgekeeper: Only true seekers of the Grail may pass!");
}

// Using nested if statements
if (knight) {
    if (quest) {
      if (knight === "Arthur" && quest === "To seek the Holy Grail") {
        console.log("Bridgekeeper: You truly seek the Grail, you may pass!");
      } 
      else {
        console.log("Bridgekeeper: You are not worthy!");
      }
    } 
    else {
      console.log("Bridgekeeper: What is your quest?");
    }
} 
else {
    console.log("Bridgekeeper: What... is your name?");
}

// Using || (OR), && (AND)
const isSeeker = knight === "Arthur" || knight === "Lancelot";
const isWorthy = knight === "Arthur" && quest === "To seek the Holy Grail";

if (isSeeker && isWorthy) {
  console.log("Bridgekeeper: Ah, a knight of the Round Table! You may proceed.");
} else {
  console.log("Bridgekeeper: Begone, pretender!");
}


const favoriteColor = "blue";

// Using a switch statement
switch (favoriteColor) {
  case "blue":
    console.log("Bridgekeeper: Ah, blue! You may pass.");
    break;
  case "green":
    console.log("Bridgekeeper: Green, like the forests of Camelot!");
    break;
  case "red":
    console.log("Bridgekeeper: Red, the color of courage!");
    break;
  default:
    console.log("Bridgekeeper: I don't know that color! Aaaaah!");
}


// Using a function with parameters and return value
function checkAnswer(knight, quest) {
    if (!knight || !quest) {
      return "Bridgekeeper: You must answer all the questions!";
    }
  
    return knight === "Arthur" && quest === "To seek the Holy Grail"
      ? "Bridgekeeper: You may pass, King Arthur!"
      : "Bridgekeeper: You shall not pass!";
}
console.log(checkAnswer(knight, quest));


// Using a function assigned to a variable
const validateColor = function (color) {
    const validColors = ["blue", "green", "red"];
  
    return validColors.includes(color)
      ? "Bridgekeeper: That is a valid color."
      : "Bridgekeeper: That color does not exist!";
};
console.log(validateColor(favoriteColor));


// Using an arrow function and ternary operator
// arrow functions are shorthand ways or writing an anonymous function
const crossBridge = (canPass) => canPass ? 
    "You cross the bridge safely." : 
    "You are cast into the Gorge of Eternal Peril!";
console.log(crossBridge(isWorthy));
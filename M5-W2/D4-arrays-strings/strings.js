const greeting = "Why, hello, there";

console.log(`${greeting} Fred!`); // template literals
console.log(greeting[1]);
console.log(greeting.length); // no () because this is a property

for (let index in greeting) {
    console.log(`Index: ${index}, Character: ${greeting[index]}`);
}

console.log(greeting.toUpperCase());
console.log(greeting.toLowerCase());

console.log(greeting.slice(-3));

console.log(greeting.substring(0, 6));

splitString = greeting.split(',');
console.log(splitString)

joinedString = splitString.join(",")
console.log(joinedString)

let input = "  hulk smash!   ";
console.log(input.trim());

let message = "I love JavaScript!";
let newMessage = message.replace("love", "like");
console.log(newMessage);

let sentence = "the quick brown fox jumps over the lazy dog";
console.log(sentence.includes("fox"));
console.log(sentence.indexOf("the"));
console.log(sentence.lastIndexOf("the"));
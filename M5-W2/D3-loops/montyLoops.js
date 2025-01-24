// Increment and decrement operators
let coconutCount = 0; // Starting with no coconuts
console.log(`You start with ${coconutCount} coconuts.`);

// Increment operators
console.log(++coconutCount)
console.log(coconutCount++)
coconutCount++;
console.log(`You find a coconut! Now you have ${coconutCount} coconut.`);

// Decrement operators
coconutCount--;
console.log(`A swallow steals a coconut! Now you have ${coconutCount} coconuts.`);

// For loop (searching for swallows carrying coconuts)
console.log("\nSearching for unladen swallows...");

for (let i = 1; i <= 5; i++) {
  console.log(`You spot swallow #${i}, but no coconuts!`);
}

// For of/in loop (knights’ quests) - for of only loops over iterable things
const knights = ["Arthur", "Lancelot", "Galahad", "Bedevere"];
console.log("\nKnights on their quests:");

for (const knight of knights) {
  console.log(`${knight} is seeking the Holy Grail!`);
}

for (const knight in knights) {
  console.log(`Knight at index position #${knight} is seeking the Holy Grail!`);
}

// For of/in loop (examining a peasant object)
const peasant = {
  name: "Dennis",
  job: "mud farmer",
  complaint: "I didn't vote for you!",
};
console.log("\nExamining the peasant's details:");

for (const [key, value] of Object.entries(peasant)) {
    console.log(`${key}: ${value}`);
}

for (const key in peasant) {
  console.log(`${key}: ${peasant[key]}`);
}

// While loop (crossing the Bridge of Death)
console.log("\nCrossing the Bridge of Death...");
let questionsAnswered = 0;

while (questionsAnswered < 3) {
  questionsAnswered++;
  console.log(`You answer question #${questionsAnswered}.`);
}

console.log("You cross the bridge safely!");

// Do while loop (taunting the French castle)
console.log("\nTaunting the French castle...");
let taunts = 0;

do {
  console.log("French soldier: I fart in your general direction!");
  taunts++;
} while (taunts < 3);

// Nested loop (building a Trojan Rabbit)
console.log("\nBuilding a Trojan Rabbit...");
const materials = ["wood", "nails", "paint"];
const workers = ["Arthur", "Lancelot", "Galahad"];

for (const material of materials) {
  console.log(`Using ${material}:`);
  for (const worker of workers) {
    console.log(`  ${worker} is working on the ${material}.`);
  }
}

// Break (encountering the Killer Rabbit)
console.log("\nApproaching the Killer Rabbit...");
for (let steps = 1; steps <= 10; steps++) {
  console.log(`Step ${steps} closer to the cave...`);
  if (steps === 5) {
    console.log("The Killer Rabbit appears! Run away!");
    break;
  }
}

// Continue (collecting shrubbery from the Knights Who Say Ni)
console.log("\nCollecting a shrubbery...");
const shrubsNeeded = 5;
for (let shrub = 1; shrub <= 7; shrub++) {
  if (shrub > shrubsNeeded) {
    console.log(`Extra shrubbery (#${shrub}) is rejected.`);
    continue;
  }
  console.log(`Shrubbery #${shrub} collected.`);
}
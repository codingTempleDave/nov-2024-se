let heroes = ["hulk", "iron man", "black widow"];
console.log(heroes[0]);

heroes.push("spiderman");
console.log(heroes);

heroes.unshift("black panther");
console.log(heroes);

heroes[0] = "thor"
console.log(heroes);

console.log(heroes.length);
console.log(heroes[heroes.length - 1])

let lastHero = heroes.pop();
console.log(lastHero);

let firstHero = heroes.shift();
console.log(firstHero);

console.log(heroes.length);
console.log(heroes);

for (let i = 0; i < heroes.length; i++) {
  console.log(heroes[i]);
}

for (let hero in heroes) {
  console.log(hero);
}

for (let hero of heroes) {
  console.log(hero);
}

console.log(heroes)
// loops through heroes, hero is the temp variable that will equal each individual
// item in the array.
heroes.forEach( hero => {
  console.log(hero);
})

let heroesMap = ["hulk", "iron man", "black widow"];

// map loops through the array like forEach but it returns a new array
// everything that is returned inside of the arrow function in map
// is placed in the new array.  Does not affect the original array.
let amazingHeroes = heroesMap.map( hero => "The amazing " + hero );
console.log(amazingHeroes);
console.log(heroesMap);

// creates new array as well
// everything that is true in the condition gets put in the new array
let scores = [75, 80, 65, 90, 85, 20, 60];
let cOrAbove = scores.filter( score => score >= 70 );
console.log(cOrAbove);

// destructuring
let arr = ['hulk', 'iron man', 'black widow', "thor", "spiderman"];
let [hero1, hero2, hero3, hero4] = arr;
console.log(hero1);
console.log(hero2);
console.log(hero3);
console.log(hero4);

// spread operator
// spreads or unpacks values from an array
let originalHeroes = ['hulk', 'iron man', 'black widow'];
let spreadHeroes = [...originalHeroes, "thor", "black panther"];
let copyOfHeroes = [...originalHeroes]; // makes a copy of originalHeroes
console.log(spreadHeroes);
console.log(originalHeroes);
console.log(copyOfHeroes);
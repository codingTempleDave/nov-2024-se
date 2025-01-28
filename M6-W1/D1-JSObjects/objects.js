let superHero = {
  name: "Iron Man",
  powers: ["Flight", "Lasers", "Intellect", "Money"],
  team: {
    name: "The Avengers",
    members: 42,
    location: "Avengers Tower"
  },
  life: 100,
  power: 20,
  attack: function() {
    console.log(`${this.name} attacks for ${this.power}`)
  }
}

console.log(superHero.name);
console.log(superHero.powers[3]);
console.log(superHero["powers"]);
console.log(superHero.powers);
console.log(superHero.team.location);
console.log(superHero.attack());


// Constructor function
function SuperHero(name, powers, team, life, attackPower){
  this.name = name;
  this.powers = powers;
  this.team = team;
  this.life = life;
  this.attackPower = attackPower;

  this.attack = function(hero){
    console.log(
      `${this.name}, who's part of ${this.team.name}, uses 
      ${this.powers[Math.floor(Math.random() * 3)]}
      to attack ${hero.name} for ${this.attackPower}`
    );
    hero.life -= this.attackPower;
    console.log(`${hero.name}'s life is now ${hero.life}`)
  }
}

let ironMan = new SuperHero(
  "Iron Man", 
  ["Flight", "Lasers", "Money"],
  {
    name: "The Avengers",
    members: 42,
    location: "Avengers Tower"
  }, 
  100, 
  20
);

let thanos = new SuperHero(
  "Thanos", 
  ["Punch", "Snap", "Body Slam"],
  {
    name: "The Black Order",
    members: 17,
    location: "Sanctuary II"
  }, 
  200, 
  15
);

console.log(ironMan.name);
console.log(thanos.name);
ironMan.attack(thanos);
thanos.attack(ironMan);

/* another way to create objects/instances/classes in JS */
class SuperHero2 {
  constructor(name, powers, team, life, attackPower) {
    this.name = name;
    this.powers = powers;
    this.team = team;
    this.life = life;
    this.attackPower = attackPower;
  }
  // no function keyword for instance methods
  attack(hero){
    console.log(
      `${this.name}, who's part of ${this.team.name}, uses 
      ${this.powers[Math.floor(Math.random() * 3)]}
      to attack ${hero.name} for ${this.attackPower}`
    );
    hero.life -= this.attackPower;
    console.log(`${hero.name}'s life is now ${hero.life}`)
  }
}

let ironMan2 = new SuperHero2(
  "Iron Man", 
  ["Flight", "Lasers", "Money"],
  {
    name: "The Avengers",
    members: 42,
    location: "Avengers Tower"
  }, 
  100, 
  20
);
let thanos2 = new SuperHero2(
  "Thanos", 
  ["Punch", "Snap", "Body Slam"],
  {
    name: "The Black Order",
    members: 17,
    location: "Sanctuary II"
  }, 
  200, 
  15
);

console.log(ironMan2.name);
console.log(thanos2.name);
ironMan2.attack(thanos2);
thanos2.attack(ironMan2);


/////////////// MATH OBJECT

console.log("PI:", Math.PI);
console.log("Round:", Math.round(4.5));
console.log("Round:", Math.round(4.4));
console.log("Ceil:", Math.ceil(4.1));
console.log("Floor:", Math.floor(4.9));
console.log("Pow:", Math.pow(8, 2));
console.log("Abs:", Math.abs(-5));
console.log("Min:", Math.min(0, 150, 30, 20, -8, -200));
console.log("Max:", Math.max(0, 150, 30, 20, -8, -200));
console.log("Random:", Math.random());


///////////// Date Object

// Creating a new Date object with the current date and time
// Format: YYYY-MM-DDTHH:mm:ss.sssZ
// The “T” character separates the date from the time portion of the string.
// The “Z” character is the UTC offset representation
// UTC is used worldwide as the standard time.
//    It does not change with the seasons and is the same everywhere.
let currentDate = new Date();
console.log("Current Date:", currentDate);

// Creating a new Date object with a specific date and time
let specificDate = new Date("2024-02-10T02:00:00");
console.log("Specific Date:", specificDate);


// Accessing date components
console.log(currentDate.getFullYear());
console.log(currentDate.getMonth() + 1); // Adding 1 because months are zero-based
console.log(currentDate.getDate());
console.log(currentDate.getHours());
console.log(currentDate.getMinutes());
console.log(currentDate.getSeconds());
console.log(currentDate.getMilliseconds());

currentDate.setDate(currentDate.getDate() + 7);
console.log(currentDate);

currentDate.setMonth(currentDate.getMonth() - 1);
console.log(currentDate);


// Creating a timestamp
// getTime() returns the number of milliseconds since January 1, 1970 00:00:00.0
// known as the Unix epoch
let timeStampDate = new Date();
let timestamp = timeStampDate.getTime();
console.log("Timestamp:", timestamp);

// Converting timestamps to dates
let newDate = new Date(timestamp);
console.log("Date extracted from timestamp:", newDate);

// Getting the time zone offset
// returns the difference between UTC time and local time in minutes
let timeZoneOffset = currentDate.getTimezoneOffset();
console.log("Time Zone Offset (in minutes):", timeZoneOffset);
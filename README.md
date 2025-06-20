# 🌑 Configurable Random Moon Picker for Lethal Company

- 🎲 Let the dice decide where your crew is heading to next!
- ✏️ Configure the set of moons used to fit your modded game
- 💵 Input your █ Credits to automatically exclude moons you can't route to

Requires [Python](https://www.python.org/) to run the script.

## Installation

Open a command prompt (`cmd`) and use the following commands:

```
git clone https://github.com/Shiinyei/lethal-company-moon-picker.git
cd lethal-company-moon-picker
python moon_picker.py --help
```

## Options

|Option|Example|Default|Description|
|---|---|---|---|
|-h<br>--help|||Displays an explanatory text about how to use the script and all of its options
|-i<br>--input|`-i="mymoons.csv"`|`"vanilla.csv"`|The CSV input file from which moon data is read. Each line defines a single moon and must contain two values: the moon's name and its cost respectively. If no input option is provided, 'vanilla.csv' in the current directory will be used instead|
|-c<br>--credit|`-c=400`|`0`|The current amount of money that your crew possesses. Any moon whose cost exceeds your savings will be ignored so that you are guaranteed to get a moon you can pay for|
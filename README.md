# ezee
anthony,jacob,evan

##  Description
it uses random to pick random number 1-6 on a die and then you reroll

###  Flowchart
```mermaid
graph TD;
  main-->first_roll;
  main-->reroll_many;
  main-->output_dice;
  first_roll--roll;
  find_mode-->count_frequency
  main-->list_unmatched_dice
  reroll_many-->reroll_1
  reroll_1--> roll
  reroll_many-->find_mode
```

#### Function Diagrams

| main    |               |  anthony    |
| ------------------ | ------------- | ------------ |
| Recieves no arguements    | calls all the programs to run the game |   outputs nothing          
***
| roll    |               |     anthony   |
| ------------------ | ------------- | ------------ |
| recives no arguments   | calls for the first roll |     outputs nothing         |

***
| output dice    |               |     anthony   |
| ------------------ | ------------- | ------------ |
| recivies no arguments   | outputs the dice to view the numbers  |    outputs nothing          |

***
| `first_roll`    |               |     evan   |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `count_frequency`    |               |     evan   |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `find_mode`    |               |     evan   |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `list_unmatched_dice`    |               |     Jacob   |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `reroll_one`    |               |     Jacob   |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `reroll_many`    |               |     Jacob   |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***

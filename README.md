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
|     | takes input from the user for roll count  |              |
|      | calculates same dice rolled  | outputs nothing             |
|       | takes input for name dice | returns total |
***
| `count_frequency`    |               |     evan   |
| ------------------ | ------------- | ------------ |
|     | takes input from the user for roll count  |              |
|      | calculates dice  | outputs constant             |
|       | takes input for name dice constant | returns total |
***
| `find_mode`    |               |     evan   |
| ------------------ | ------------- | ------------ |
|     | takes input from the main for mode / constant  |              |
|      | calculates dice same  | outputs dice numb             |
|       | takes input for name dice constant_ | returns total |
***
| `list_unmatched_dice`    |               |     Jacob   |
| ------------------ | ------------- | ------------ |
|     | takes input from the reroll_many for index |              |
|       |  | returns index |
***
| `reroll_one`    |               |     Jacob   |
| ------------------ | ------------- | ------------ |
|     | takes input from the reroll_many for deleating  |              |
***
| `reroll_many`    |               |     Jacob   |
| ------------------ | ------------- | ------------ |
|     | takes input from the main for reroll_one and list_unmatched_dice  |       outputs list of dice       |
***

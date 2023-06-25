# Initiative Tracker 
---

## Example


```encounter
name: Goblin Fight
creatures:
- 2: Goblin

party: Lyra

```


The players encounter a [[Monster example|Beholder]] (You can press ctrl to go to encounter or control click to open another window)



```encounter-table 
name: Encounter 1
creatures:
- 1d10: Goblin
- 1d6: Orc

---

name: encounter 2
creatures:
- 1d10: Goblin

```
```encounter
name: Goblin Fight
creatures:
- 2: Goblin

party: Family


---

name: Orc Fight
creatures:
- 5d4: Orc

party: Family


```


---


| dice: 1d2 | Encounter                                 |
| --------- | ----------------------------------------- |
| 1         | `encounter: 3d6: Hobgoblin, 10d4: Goblin` |
| 2         | `encounter: 1d6: Aboleth`                 |

^908193

`dice: [[Initiative Tracker#^908193]]`


---


```encounter
creatures:
  - 3: Goblin, 7, 15, 2                 # 3 goblins with HP: 7, AC: 15, MOD: 2 will be added.
  - 2: Goblin, 5, 15, 2, 25             # 2 goblins with HP: 7, AC: 15, MOD: 2 worth 25 XP will be added.
```

```encounter
creatures:
  - [[Hobgoblin, Bob]]          
  -                             
  
    - [Hobgoblin, Jim]          
    - 12
    - 13
    - 2
    - 25
  - 2:                          
    - [Hobgoblin, Jeff]
    - 12
    - 13
  - 5:                         
      creature: Hobgoblin
      name: Ted
      hp: 12
      ac: 13
  - 1d5:                        
      creature: Hobgoblin
      name: Sarah
      hp: 12
      ac: 13
```

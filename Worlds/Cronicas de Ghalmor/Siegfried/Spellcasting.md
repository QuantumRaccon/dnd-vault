 No actualizado

## Spellcasting

| 1st (4) | 2nd (3) | 3rd (3) | 4th (3) | 5th (1) | 7th (1)    |     | 
| ------- | ------- | ------- | ------- | ------- | --- | --- |
| 4       | 3       | 3       | 3       | 1       |     |     |


| [[Font of Magic\|Sorcery Points]] (11) | [[Chaotic Charge]] | [[Core/Items/Magic/Ring of Water Elemental Command|Ring Charges]] (5) |
| -------------------------------------- | ------------------ | ------------------------------------------------------ |
| 11                                     | 0                  | 5                                                      |



## Spell List
```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains( 
	["Fire Bolt", "Green-Flame Blade", "Mind Sliver", "Minor Illusion", 
	"Prestidigitation", "Shape Water", "Chaos Bolt", "Mage Armour", "Shield", "Silvery Barbs", "Fireball", "Fly", "Haste", "Misty Step", "Banishment", "Polymorph", "Aphasia", "Shrow's Dinger" ,"Dimension Door", "Mage Armor", "Absorb Elements" ] 			
 	,file.name) and file.name != "Flame Blade"
sort level asc, name asc
```

## Elemental Ring Spells
```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains( 
	["Create or Destroy Water", "Control Water", "Ice Storm", "Wall of Ice" ] 			
	,file.name)
sort level asc
```


## Metamagic
- [[Metamagic#^Quickened|Quickened Spell]]
- [[Metamagic#^Transmuted |Transmuted Spell]]
- [[Metamagic#^Heightened|Heightened Spell]]
- [[Metamagic#^Empowered|Empowered Spell]]
- [[Metamagic#^Twinned|Twinned Spell]]





character:: [[Siegfried]]



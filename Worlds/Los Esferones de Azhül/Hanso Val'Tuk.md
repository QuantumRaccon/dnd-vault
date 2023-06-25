---
hp: 40
ac: 17
modifier: 2
level: 8
class: "Artificer"
subclass: "Artillerist"
multiclass:
race: "Velkot"
background: "Sage"
tag: player, character
world: Azhül
campaign: Los Esferones de Azhül
---


# [[Hanso Val'Tuk]]
**Class**: [[Artificer]]
**Subclass**: [[Artillerist]]
**Race**: [[Velkot]]
**Background**: [[Core/Backgrounds/Sage|Sage]]

---
![[Pasted image 20230621170320.png]]
# Stats
---

>[!info]- Max Health: 40
 
 >[!info]- AC: 17
 > Studded Leather: 12+2 = 14 (Dex)
 > [[Repulsion Shield]]: +3 = 17
 
 >[!info]- Initiative: +2

 >[!info]- Speed: 30 ft

>[!info]- Passive Wisdom: 14
> Darkvision 120 ft

>[!Example] Resistances
> Magic can't put me to [[Core/Rules/Sleep|Sleep]]
> Advantage on saves vs. [[Charmed]]


# Ability Scores
---
>[!info]- Proficiency Bonus: +3

| Ability            |Score |Mod |Save Proficient|Save|
| ------------------ | --- | ----- |:-:| ---- |
|Strength|8|-1 |  |-1|
|Dexterity |14 |+2 |  |+2|
|Constitution |8 |-1 |X|+2 |
|Intelligence |18 |+4 |X|+6 |
|Wisdom |12 |+1 |                 |+1 |
|Charisma |16|+3|                 |+3|


## Skills

| Skill                 | Mod | Proficient |
| --------------------- | --- |:--|
| Acrobatics (Dex)      |2|  |
| Animal Handling (Wis) |1|  |
| Arcana (Int)          |7|X |
| Athletics (Str)       |-1|  |
| Deception (Cha)       |3|  |
| History (Int)         |7|X |
| Insight (Wis)         |1|  |
| Intimidation (Cha)    |3|  |
| Investigation (Int)   |7|X |
| Medicine (Wis)        |4|X |
| Nature (Int)          |4|  |
| Perception (Wis)      |4|X|
| Performance (Cha)     |3|  |
| Persuasion (Cha)      |3|            |
| Religion (Int)        |4|            |
| Sleight of Hand (Dex) |2|            |
| Stealth (Dex)         |2|            |
| Survival (Wis)        |1|            |


>[!Example] Other Proficiencies & Languages
>[[Thieves' Tools]]
>[[Tinker's Tools]]
>[[Artisan's Tools]]
>[[Woodcarver's Tools]]
>Light and medium armor
>Shields
>Simple weapons and Firearms
> ---
>Velkot
>Common
>Elvish
>Dwarf
>Draconic


>[!Example] Feats
> [[Linguist]]


# Traits
---

```dataview
table level as "Level", class as "Class", subclass as "Subclass"
from #feature  
where contains(this.class, class) or contains(this.subclass, subclass) and level <= this.level
sort level asc, name asc
```



>[!Example] Background feature
>
>**Researcher**. When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign.


>[!Example] Racial Traits
>**Trance**. Velkot don't need to sleep, but meditate semiconsciously, for 4 hours a day. This gives the same benefit as a human gets from 8 hours of sleep (long rest takes only 4 hours).
>**Fey Step**. Once per short rest, as a bonus action, I can magically teleport up to 30 ft to an unoccupied space I can see


# Equipment
---

|CP|SP|EP|GP         |PP  |
|:--- |:--- |:--|:--- | --- |
|  |  |     |10|     |

>[!Note] Inventory

>[!Note] Magic items


# Actions
---

| Long Rest                      | Short Rest |
|:------------------------------ |:---------- |
|[[Infuse Item]]| [[The Right Tool for the Job]]|
|  |  |

|Action|Bonus Action|Reaction|Passive |
|:--|:--|:--|:--|
|[[Magical Tinkering]] (add/remove)|Fey Step [[Misty Step]] |[[Flash of Genius]]|  |   |
|  |  |  |  |



### Attacks

|Name| Prof | Ability | To Hit | Damage | Range |  Desc   |
|:---- |:---- |:------- |:------ |:------ |:----- | --- |
|[[Armblade]]|X|Dex|+5|1d8+3 slashing, piercing|Melee|Finess, Bonus action to retract|
|  |  |  |  |  |  |  |


# Spells
---

| Class | Ability | To Prepare | Attack Modifier | Saving Throw DC | 
|:----- |:------- |:---------- |:--------------- |:--------------- |
|Artillerist|Int|8|+8|DC 15|

| 1st   | 2nd   | 3rd | 4th | 5th |6th|7th|8th|9th|
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
| 4 / 4 | 3 / 3 |     |     |     |     |   |   |   |

```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains(["Light", "Mold Earth", "Prestidigitation", "Mending"], file.name)
sort level asc, name asc
```

```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains(classes, this.class) and level <= 2 and level >0
sort level asc, name asc
```
```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains(["Shield", "Thunderwave", "Scorching Ray","Shatter"], file.name)
sort level asc, name asc
```

# Companions
---
[[Señor Boom]]


# Personality
---
>[!Note] Personality Traits

>[!Note] Ideals

>[!Note] Bonds

>[!Note] Flaws

# Description
---

| Gender        | Age       | Size     | Height   | Weight   |
|:------------- |:--------- |:-------- |:-------- |:-------- |
|               |           |          |          |          |
| **Alignment** | **Faith** | **Hair** | **Eyes** | **Skin** | 
|               |           |          |          |          |


>[!Example] Secrets


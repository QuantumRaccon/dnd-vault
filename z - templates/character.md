---
hp:
ac: 
modifier: 
level: 
tag: player, character
world: <% tp.user.getThisWorld(tp) %>
campaign: <% tp.file.folder(false) %>
---


# [[<% tp.file.title %>]]
race:: 
class:: 
background::

---
Image

# Stats
---

>[!info]- Max Health: 
 
 >[!info]- AC: 
 
 >[!info]- Initiative: 

 >[!info]- Speed: 

>[!info]- Passive Wisdom:

>[!Example] Resistances


# Ability Scores
---
>[!info]- Proficiency Bonus: 

| Ability            | Score | Mod | Save Proficient | Save |
| ------------------ | ----- | --- |:-:| ---- |
|Strength  |       |     |  |      |
|Dexterity |  |     |                 |      |
|Constitution |  |     |                 |      |
|Intelligence |       |     |                 |      |
|Wisdom|       |     |                 |      |
|Charisma|       |     |                 |      |


## Skills

| Skill                 | Mod | Proficient |
| --------------------- | --- |:-:|
| Acrobatics (Dex)      |     |  |
| Animal Handling (Wis) |     |            |
| Arcana (Int)          |     |            |
| Athletics (Str)       |     |            |
| Deception (Cha)       |     |            |
| History (Int)         |     |            |
| Insight (Wis)         |     |            |
| Intimidation (Cha)    |     |            |
| Investigation (Int)   |     |            |
| Medicine (Wis)        |     |            |
| Nature (Int)          |     |            |
| Perception (Wis)      |     |            |
| Performance (Cha)     |     |            |
| Persuasion (Cha)      |     |            |
| Religion (Int)        |     |            |
| Sleight of Hand (Dex) |     |            |
| Stealth (Dex)         |     |            |
| Survival (Wis)        |     |            |


>[!Example] Other Proficiencies & Languages

>[!Example] Feats


# Traits
---



>[!Example] Background feature

>[!Example] Racial Traits


# Equipment
---

|CP|SP|EP|GP         |PP  |
|:--- |:--- |:--|:--- | --- |
|  |  |     |     |     |

>[!Note] Inventory

>[!Note] Magic items


# Actions
---

| Long Rest                      | Short Rest |
|:------------------------------ |:---------- |
|  |  |
|                                |            |

|Action|Bonus Action|Reaction|Passive|
|:--|:--|:--|:--|
|Magical Tinkering (add/remove) |Fey Step|Flash of Genius |   |
|  |  |  |   |


### Attacks

|Name| Prof | Ability | To Hit | Damage | Range |  Desc   |
|:---- |:---- |:------- |:------ |:------ |:----- | --- |
|[[Greataxe]]|X|STR|+5 |1d12+3 slashing|  |AXE|
|[[Javelin]]|  |DEX|+3|1d6+3 piercing|30ft/120ft w/dis. |  |


# Spells
---

| Class | Ability | To Prepare | Attack Modifier | Saving Throw DC | 
|:----- |:------- |:---------- |:--------------- |:--------------- |
|       |         |            |                 |                 |

| 1st   | 2nd   | 3rd | 4th | 5th |6th|7th|8th|9th|
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
| 4 / 4 | 3 / 3 |     |     |     |     |   |   |   |

```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains(
["Fire Bolt", "Green-Flame Blade", "Mind Sliver", "Minor Illusion", "Prestidigitation", "Shape Water", "Chaos Bolt", "Mage Armour", "Shield", "Fireball" ] ,file.name)
sort level asc, name asc
```

# Companions
---

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


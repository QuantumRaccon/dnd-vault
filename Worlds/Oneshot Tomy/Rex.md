 ---
level: 5
alias: 
gender: male
tag: player, character
faction: 
hp: 48
ac: 20
initative: 2
---


# Rex
race:: [[Core/Races/Kobold]]
class:: [[Artificer]] [[Armorer]]
background:: Criminal

---
![[Rex.png]]

---


>[!info] Max Health: 43 
> Can add 5 to Temporal Hp
 
 >[!info]- AC: 20
 > Unarmored: 12
 > Splint Armor: 17
 > Shield: +2
 > Repulsion Shield: +1
 > Armor of Magical Strength

 >[!info]- Initiative: +2

>[!info]- Proficiency Bonus: +3


| Temporal HP | Speed | Hit Die |
| ----------- | ----- | ------- |
| 0           | 30ft  | 5d8        |


## Ability Scores

| Ability            | Score | Mod | Save | Save Proficient |
| ------------------ | ----- | --- | ---- | --------------- |
| Strength (Str)     | 12    | +1  |      |                 |
| Dexterity (Dex)    | 14    | +2  |      |                 |
| Constitution (Con) | 16    | +3  |      | `fas:Check`     |
| Intelligence (Int) | 20    | +5  |      | `fas:Check`     | 
| Wisdom (Wis)       | 12    | +1  |      |                 |
| Charisma (Cha)     | 12    | +1  |      |                 |

---
## Skills

| Skill                 | Mod | Proficient  |
| --------------------- | --- | ----------- |
| Acrobatics (Dex)      | +2  |             | 
| Animal Handling (Wis) | +1  |             |
| Arcana (Int)          | +8  | `fas:Check` |
| Athletics (Str)       | +4  | `fas:Check`             |
| Deception (Cha)       | +4  | `fas:Check` |
| History (Int)         | +5  |             |
| Insight (Wis)         | +1  |             |
| Intimidation (Cha)    | +1  |             |
| Investigation (Int)   | +8  | `fas:Check` |
| Medicine (Wis)        | +1  |             |
| Nature (Int)          | +5  |             |
| Perception (Wis)      | +1  |             |
| Performance (Cha)     | +1  |             |
| Persuasion (Cha)      | +1  |             |
| Religion (Int)        | +5  |             |
| Sleight of Hand (Dex) | +5  | `fas:Check` |
| Stealth (Dex)         | +5  | `fas:Check` |
| Survival (Wis)        | +1  |             |


>[!info]- Passive Wisdom: 11
> Darkvision 60 ft


>[!Example] Other Proficiencies & Languages
> [[Thieve's Tools]]
> [[Tinker's tools]]
> [[Jeweler's Tools]]
> [[Smith's Tools]]
> [[Cook Utensils]]
> ALL armor
> Shields
> Simple weapons
> 
> Gaming Cards
> 
> ---
> 
> Common
> Draconic
> Gnome
> Undercommon
> Giant
## Status & Effects
---
- [x] I am cool

Qualish: 100 - 14 -15 = 71
Qualish: 71 - 8 - 20 = 43
Qualish: 43+15 = 58 - 33
Qualish: 25



# Items
---
| Name                   | To hit | Damage/Type      | Property |
| ---------------------- | ------ | ---------------- | -------- |
| **Thunder Gauntlets**  | +8 +1     | 1d8+5+1 Thunder    |          | 
| **Lightning Launcher** | +8 +1    | 1d6+5+1 Lightining | 90/300   |

| Gold | Silver | Copper |
| ---- | ------ | ------ |
| 294gp  | 0      | 0      | 


>[!note] Items
> - Splint armor
> - Shield
> - Thieve's tools
> - Dugeoneer's pack
> - Cook Utensils
> - Smith's Tools
> - Jeweler's Tools
> - Baston de proporciones brigidas baston muy poderoso
> - Talisman de bien puro
> - Libro de maldad pura


>[!example] Magic Items
>
> # Infusions:
> - [[Repulsion Shield]]
> - [[Enchanced weapon]]
> - [[Armor of Magical Strength]]


>[!Tldr] Infusions known: 5
> - [[Repulsion Shield]]
> - [[Armor of Magical Strength]]
> - [[Homunculus Servant]]
> - [[Enchanced weapon]]
> - [[Replicate magic item]] (Bag of holding)

# Spells
---

 | 1st   | 2nd   |
 | ----- | ----- |
 | 4 / 4 | 2 / 2 |

| Spell Attack Bonus | Spell Save DC |
| ------------------ | ------------- | 
| +8                 |  16             | 


> [!Info] Armorer Spells
> - [[Magic Missile]]
> - [[Thunderwave]]
> - [[Shatter]]
> - [[Mirror Image]]


>[! danger ] Spells Prepared: 7
> - [[Arcane Weapon]]
> - [[Absorb Elements]]
> - [[Faerie Fire]]
> - [[Tasha's Caustic Brew]]



| Concentrating Spell | Duration Left | Total Duration |
| ------------------- | ------------- | -------------- |
|                |               |                |



```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains(["Fire Bolt", "Guidance", "Thorn Whip"],file.name) 

sort level asc, name asc
```

```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 

where contains(classes, "Artificer") and level = "1st"

sort level asc, name asc
```

```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 

where contains(classes, "Artificer") and level = "2nd"

sort level asc, name asc
```

# Class Features
---

![[Magical Tinkering]]

![[The Right Tool for the Job]]

![[Tools of the Trade]]
![[Armorer Spells]]

![[Armor Model]]
![[Extra Attack]]

# Racial Features

![[Core/Races/Kobold#^9670b4]]
![[Core/Races/Kobold#^850076]]
![[Core/Races/Kobold#^8babd6]]
![[Core/Races/Kobold#^3d5ac4]]

# Description

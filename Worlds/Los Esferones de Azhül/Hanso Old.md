---
level: 8
hp: 40
ac: 17
modifier: 2
alias: 
gender: Male 
tag: player, character
world: Azhül
campaign: Los Esferones de Azhül
faction: 
---


# [[Hanso Old]] Val'Tuk
race:: [[Velkot]]
class::[[Artificer]]
 
---



# Stats
---

>[!info]- Max Health: 40 
 
 >[!info]- AC: 17
 > Studded Leather: 12+2 = 14 (Dex)
 > [[Repulsion Shield]]: +3 = 17
 
 >[!info]- Initiative: +2

>[!info]- Proficiency Bonus: +3 


## Ability Scores
---

| Ability            | Score | Mod | Save | Save Proficient | 
| ------------------ | ----- | --- | ---- | --------------- |
| Strength (Str)     | 8     | -1  | -1   |                 |
| Dexterity (Dex)    | 14    | +2  | +2   |                 |
| Constitution (Con) | 8     | -1  | +2   | X     |
| Intelligence (Int) | 18    | +4  | +7   | X    |
| Wisdom (Wis)       | 12    | +1  | +1   |                 |
| Charisma (Cha)     | 16    | +3  | +3   |                 |

Magic can't put me to sleep; Adv. on saves vs. charmed

---
## Skills

| Skill                 | Mod | Proficient |
| --------------------- | --- | ---------- |
| Acrobatics (Dex)      | +2  |            |
| Animal Handling (Wis) | +1  |            |
| Arcana (Int)          | +7  | X          |
| Athletics (Str)       | -1  |            |
| Deception (Cha)       | +3  |            |
| History (Int)         | +7  | X          |
| Insight (Wis)         | +1  |            |
| Intimidation (Cha)    | +3  |            |
| Investigation (Int)   | +7  | X          |
| Medicine (Wis)        | +4  | X          |
| Nature (Int)          | +4  |            |
| Perception (Wis)      | +4  | X          | 
| Performance (Cha)     | +3  |            |
| Persuasion (Cha)      | +3  |            |
| Religion (Int)        | +4  |            |
| Sleight of Hand (Dex) | +2  |            |
| Stealth (Dex)         | +2  |            |
| Survival (Wis)        | +1  |            |



>[!info]- Passive Wisdom: 14
>Darkvision 120 ft

>[!Example] Other Proficiencies & Languages
>Velkot
>Common
>Elvish
>Dwarf
>Draconic
>

>[!Example] Feats
>Linguist

>[!Note] Inventory
> 

>[!Example] Secrets
> 

# Skills

Artillerist, level 8:

- **Magical Tinkering** (Artificer 1, E:RLW 55) [Intelligence modifier of active objects]
  - As an action, I use artisan's tools to give max 1 property to a nonmagical tiny object:
    - Emit light (5-ft radius bright light, equal dim), an odor, or a nonverbal sound
    - Static visual effect on one surface, or emit a 6-second recorded message when tapped
  - If I instill a property in more objects than I can have active, the oldest loses its property

- **Spellcasting** (Artificer 1, E:RLW 55) [2 cantrips known]
  - I can cast prepared artificer cantrips/spells, using Intelligence as my spellcasting ability
  - To cast, I must use thieves' or artisan's tools I'm proficient with as a spellcasting focus
  - I can cast my prepared artificer spells as rituals if they have the ritual tag
  - Whenever I gain an artificer level, I can swap one artificer cantrip I know for another

- **Infuse Item** (Artificer 2, E:RLW 57) [6 infusions known; max 3 infused items] 
- When I finish a long rest, I can turn nonmagical objects into magic items using my infusions 
- I can attune to it immediately; If I infuse too many items, the oldest loses its magic 
- The infusion lasts until my death plus my Int mod in days, but ends if I unlearn the infusion 
- Each infusion can only be used in one item at a time and only in appropriate items 
- Whenever I gain an artificer level, I can replace an infusion I know with another 
- I can use an infused item as a spellcasting focus

- **The Right Tool for the Job** (Artificer 3, E:RLW 57)
  - In 1 hour (during a rest) I can create a set of artisan's tools that last until I do so again

- **Eldritch Cannon** (Artillerist 3, E:RLW 59) [create 1 cannon, 1× per long rest or SS 1+]
  - As an action, I can use woodcarver's or smith's tools to create an eldritch cannon in 5 ft
  - I can do this once per long rest, or by expending a spell slot (SS 1+) to create one cannon
  - I decide its size (Small/Tiny), appearance, type: flamethrower, force ballista, or protector
  - It disappears after 1 hour, when reduced to 0 HP, or if I dismiss it as an action
  - As a bonus action when within 60 ft of it, I can activate it to move and do its action
  - I can't have multiple cannons; Select "Eldritch Cannon" on a companion page for its stats

- **Tools Proficiency** (Artillerist 3, E:RLW 59) [proficient with woodcarver's tools]

- **Arcane Firearm** (Artillerist 5, E:RLW 59) [lasts until I use this feature again]
  - After a long rest, I can use woodcarver's tools to enhance a wand, staff, or rod
  - If I use this as my spellcasting focus for an artificer spell, I add +1d8 to one damage

- **Tool Expertise** (Artificer 6, E:RLW 57) [expertise with all tools I'm proficient with]

- **Flash of Genius** (Artificer 7, E:RLW 57) [Intelligence modifier per long rest]
  - As a reaction when I or another in 30 ft make a check/save, I can add my Int mod to it


# Description




```dataview
table level as "Level", casting_time as "Casting Time", range as "Range", duration as "Duration"
from #spell 
where contains(classesStr, this.class) and level < 2 and level > 0
sort level asc, name asc
```

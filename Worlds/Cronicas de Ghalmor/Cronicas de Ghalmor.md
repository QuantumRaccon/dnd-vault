---
world: Ghalmor
campaign: Cronicas de Ghalmor
status: active
role: Player
system: D&D 5e
type: world
tag: world
---

# Crónicas de Ghalmor

## Player Characters

- [[Alysys]] (Male)
- [[Siegfried]] (Yo)
- Azer (Stefano)
- Skamos (Diego)
- Andustar (Micheli)

## Sessions

```button
name Add Session
type note(Worlds/Cronicas de Ghalmor/<% tp.user.getThisGameNum(tp) %>, split) template
action session-player
templater true
```


```dataview
table summary as "Summary" from "Worlds/Cronicas de Ghalmor"
where contains(tags,"session") 
SORT sessionNum ASC
```

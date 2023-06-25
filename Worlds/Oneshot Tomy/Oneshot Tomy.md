---
world: 
campaign: Oneshot Tomy
status: active
role: player
system:
type: world
tag: world
---
# Oneshot Tomy

## Player Characters

-

## Sessions

```button
name Add Session
type note(Worlds/Oneshot Tomy/<% tp.user.getThisGameNum(tp) %>_<% tp.date.now("YYYYMMDD") %>, split) template
action session-player
templater true
```



```dataview
table summary as "Summary" from "Worlds/Oneshot Tomy"
where contains(type,"session") 
SORT sessionNum ASC
```



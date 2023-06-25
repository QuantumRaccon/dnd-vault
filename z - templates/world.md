---
world: <% tp.user.getThisWorld(tp) %>
campaign: <% tp.file.folder(false) %>
status: active
role: player
system:
type: world
tag: world
---
# <% tp.file.folder(false) %>

## Player Characters

-

## Sessions

```button
name Add Session
type note(Worlds/<% tp.file.folder(false) %>/<% tp.user.createWorldSessionbtn(tp) %>, split) template
action session-player
templater true
```



```dataview
table summary as "Summary" from "Worlds/<% tp.file.folder(false) %>"
where contains(type,"session") 
SORT sessionNum ASC
```



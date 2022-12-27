# pyrate
### Description:

Project for managing music ratings in my collection.

Sometime around 1990 I started tracking ratings for my CD collection using a text file.


### Virtual Environment:
When working in Visual Studio Code on Windows it is useful to create a virtual environment

```
py -3 -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate
```

#### TODO:
- [x] Start project
- [ ] Track class
  - [x] Parse track from line
  - [x] Handle track with artist
- [ ] Album class
  - [x] Add track
  - [x] Calculate average rating
- [ ] Parse file
  - [x] Single artist single album
  - [x] Single artist multiple albums
  - [ ] Various artists album
  - [ ] Various artists series
  - [ ] Split artist collaborations
- [ ] Produce ranking list
- [ ] Produce json
- [ ] Inject ratings into rateyourmusic.com

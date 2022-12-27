# pyrate
### Description:

Project for managing music ratings in my collection.

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
  - [ ] Calculate average rating
- [ ] Parse file
  - [x] Single artist single album
  - [x] Single artist multiple albums
  - [ ] Various artists album
  - [ ] Various artists series
  - [ ] Split artist collaborations
- [ ] Compute release averages
- [ ] Produce json
- [ ] Produce ranking list
- [ ] Inject ratings into ratemymusic.com

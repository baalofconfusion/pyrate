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
  - [ ] Handle track with artist
- [ ] Parse file
  - [ ] Single artist single album
  - [ ] Single artist multiple albums
  - [ ] Various artists album
  - [ ] Various artists series
- [ ] Compute release averages
- [ ] Produce json
- [ ] Produce ranking list
- [ ] Inject ratings into ratemymusic.com

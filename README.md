# pyrate
## Description:

### Project for managing music ratings in my collection.

Sometime around 1990 I started tracking ratings for my CD collection using a text file. I have maintained this file continuously since then.

In 2007 I created an account on rateyourmusic.com with the intention of possibly migrating my ratings into that site, but for multiple reasons I have not done so. The first reason is that RYM does not calculate a personal average rating for each release; they only calculate an average rating across all memebr ratings on the site. Another reason is the sheer amount of time it would take to transfer all the data given my track rating file containing roughly 17000 releases.

This project started to answer a basic question for myself: What albums do I rate the most highly based on the track ratings, and how well does that coorespond to which album I queue up most frequently. Does my perception of what are my favorites actually match up to what I've rated the most highly?

An additional long term goals for this project is to create structured data for my collection, which can replace, or supplement my unstructured text file.

And finally, I want to create a web-scraping process to inject my rating information into my rateyourmusic account (and potentially any other music rating site) so I dont have to do it by hand.

## Virtual Environment:
When working in Visual Studio Code on Windows it is useful to create a virtual environment

```
py -3 -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate
```

## TODO:
- [x] Start project
- [ ] Track class
  - [x] Parse track from line
  - [x] Handle track with artist
  - [ ] Add track-number attribute
- [ ] Album class
  - [x] Add track
  - [x] Calculate average rating
  - [ ] Additional attributes (compilation, single, EP, etc.)
- [ ] Parse file
  - [x] Single artist single album
  - [x] Single artist multiple albums
  - [x] Various artists album
  - [x] Various artists series
  - [ ] Handle non-integer track numbering
  - [ ] Split artist collaborations
  - [ ] Handle multi-disc releases
- [x] Produce ranking list
  - [ ] Option to exclude partial ratings 
- [ ] Produce json
- [ ] Calculate median and mode
- [ ] Inject ratings into rateyourmusic.com

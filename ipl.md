# IPL Predictor -- Rebuild Prompt

## Stack

-   Node.js (\>=18), Express 5, ES modules (`type: "module"`)
-   No database -- flat JSON files only
-   Frontend: single HTML file, vanilla JS, no framework
-   Package manager: pnpm
-   Deploy: Render.com

## Project Structure

server-simple.js → Express backend (port 3009 or \$PORT)\
schedule.json → Match fixtures (manually maintained)\
picks.json → User predictions (auto-created)\
h2h.json → Head-to-head records (auto-created)\
render.yaml → Render deploy config

public/\
index.html → Full SPA frontend\
manifest.json → PWA manifest\
images_final/ → Team logos (MI, CSK, KKR, SRH, RCB, GT, RR, DC, PBKS,
LSG)

------------------------------------------------------------------------

## Backend API

### GET /api/schedule

Return schedule.json

### GET /api/picks/:userName

Return picks for a user

### POST /api/picks

Body: { "userName": "","matchId": "","team": "" }

Saved with: - frozen: true - timestamp

### GET /api/results

Return \[{matchId: winner}\] for matches where match.winner is set in
schedule.json

### GET /api/leaderboard

Compute {rank, name, correct, total, score%}

### GET /api/h2h

Return h2h.json

### POST /api/h2h/refresh

Refresh H2H data from CricketData API

------------------------------------------------------------------------

## schedule.json Format

{ "matches":\[ {
"id":"2026-03-19T19:30:00+05:30-Mumbai_Indians-vs-Chennai_Super_Kings",
"dateLabel":"Thu, 19 Mar '26", "teamA":"Mumbai Indians",
"teamB":"Chennai Super Kings", "venue":"Wankhede Stadium, Mumbai",
"startTimeISO":"2026-03-19T19:30:00+05:30", "winner":null }\] }

winner is set manually after match finishes.

------------------------------------------------------------------------

## H2H Refresh Logic

Uses env variable CRICKET_API_KEY with: https://api.cricapi.com/v1

Steps: 1. Search IPL series 2. Get match list 3. Parse winner from
status string 4. teams\[0\] = home

Normalization: - Royal Challengers Bengaluru → Royal Challengers
Bangalore - Delhi Daredevils → Delhi Capitals - Kings XI Punjab → Punjab
Kings

Skip defunct teams: - Rising Pune Supergiant - Deccan Chargers - Gujarat
Lions

Saved in h2h.json: { "lastUpdated":"","records":{ "team":{ "opponent":{
"home":0, "away":0 } } } }

------------------------------------------------------------------------

## Frontend (public/index.html)

### Layout

-   CSS Grid with sticky header
-   Dark / Light theme toggle
-   Theme stored in localStorage
-   Hamburger sidebar (desktop)
-   Bottom nav (mobile ≤768px)

------------------------------------------------------------------------

## Views

1.  Upcoming Matches (future only)
2.  Leaderboard (live rankings)
3.  My Results (personal stats)

------------------------------------------------------------------------

## Header

-   10 team badge icons to filter matches
-   "All" button resets filter
-   Center title: Predict the winner
-   User chip shows logged-in name

Mobile: badges hidden, bottom nav shown

------------------------------------------------------------------------

## User Login

First visit modal asks for name → saved in localStorage

------------------------------------------------------------------------

## Prediction Cutoff

-   Lock predictions 30 minutes before match

-   Countdown HH:MM:SS

-   24h shown as Xd Yh

Status chips: Open (amber)\
Locked (red)

------------------------------------------------------------------------

## Upcoming Matches UI

Desktop table: Date \| Home \| Away \| Venue \| Time \| Pick \| Submit

Mobile: Card layout with logos, teams, venue, time, pick dropdown

Submit flow: Submit → confirm → POST /api/picks

------------------------------------------------------------------------

## H2H Tooltip

Hover or tap on team name shows: - Home wins - Away wins - Total wins

Data from: records\[team\]\[opp\] + records\[opp\]\[team\]

------------------------------------------------------------------------

## Leaderboard

Columns: Rank \| Player \| Correct \| Total \| Score%

Current user marked with YOU chip.

------------------------------------------------------------------------

## My Results

Columns: Date \| Fixture \| Your Pick \| Status \| Winner

Stats bar: Correct count\
Wrong count\
Accuracy %

------------------------------------------------------------------------

## Misc

Team logos: images_final/`<ABBR>`{=html}.png

Results auto refresh every 60 seconds

PWA: manifest.json\
theme-color #0f172a

------------------------------------------------------------------------

## Team Brand Colors

MI: #004BA0\
CSK: #FDB913\
SRH: #FF822A\
KKR: #3A225D\
GT: #1C2841\
LSG: #1C4A9E\
RCB: #EC1C24\
DC: #004C93\
PBKS: #ED1B24\
RR: #254AA5

------------------------------------------------------------------------

## Render Deployment (render.yaml)

services: - type: web name: ipl-predictor runtime: node buildCommand:
pnpm install startCommand: node server-simple.js

envVars: - key: NODE_ENV value: production

Set separately in Render dashboard: CRICKET_API_KEY

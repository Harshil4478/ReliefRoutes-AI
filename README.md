# ReliefRoutes AI

Emergency-response platform for floods and cyclones. It lets an operator log emergency requests, manage relief centres and their stock, plan road routes, and review AI-proposed supply dispatches before approving them.

**Theme:** Climate, Resource Infrastructure & Global Supply Resilience

## Team
- Harshil (GitHub: [Harshil4478](https://github.com/Harshil4478))
- Anitha
- <add any other member / college / graduation year>

## Features
- **Dashboard** - live overview of emergencies, stock and dispatches.
- **Live weather** - current conditions and rain forecast for any city or district.
- **Emergency requests** - add, edit and delete requests with severity, people affected and supplies needed; location is picked on the map or geocoded from an address.
- **Relief centres and inventory** - register centres with capacity and stock (water, food, medical kits); low-stock alerts.
- **Route planner** - map-first planner showing real road routes (distance and drive time) from a centre to an emergency.
- **Dispatch log** - every approved dispatch deducts stock and is tracked (Approved / On the way / Delivered / Cancelled).
- **AI Relief Agent** - proposes which centre should send which supplies. It can only create *Pending* proposals; **a human must approve** before anything is dispatched.

## Live data sources (no mock data)
| Purpose | Source |
|---|---|
| Weather and forecast | [Open-Meteo](https://open-meteo.com/) API |
| Address search / reverse geocoding | OpenStreetMap Nominatim |
| Road routing (distance, time, geometry) | OSRM public routing service |
| Map tiles | OpenStreetMap via Folium / Leaflet |
| Chat assistant (optional) | Google Gemini API (function calling, free tier) |

All emergencies, centres, stock and dispatches are entered by the operator at runtime and stored in a local SQLite database. The repository ships no seeded or hardcoded datasets.

## How the AI agent works
1. A deterministic planner (`recommendation_service.py`, `agent_core.py`) estimates the supplies each emergency needs from its people count, shortlists active centres by distance, fetches real OSRM road routes, and scores each centre by travel time plus a penalty for missing supplies.
2. All numbers (distance, stock, quantities) come from code, never from a language model.
3. The optional Gemini assistant (`llm_agent.py`) uses the same functions as tools to investigate and **propose** dispatches. It has no approval tool.
4. The operator approves or rejects each proposal in the UI; approval creates the dispatch and reduces stock.

Limitation: OSRM does not know about flooded or closed roads. The app says so in every recommendation.

## Architecture
```
app.py                  Streamlit entry point and pages
dashboard_page.py       Dashboard
route_planner_page.py   Map-first route planner
ai_agent_page.py        AI agent UI (proposals + chat)
agent_core.py           Planner, proposals, tool functions
llm_agent.py            Gemini tool-use loop (optional)
recommendation_service.py  Centre scoring logic
routing_service.py      Nominatim + OSRM clients
weather_service.py      Open-Meteo client
map_service.py          Folium relief map
database.py / relief_centres.py / logistics.py   SQLite storage
reset_db.py             Clears test data before a demo
```

## Setup
```bash
git clone https://github.com/Harshil4478/ReliefRoutes-AI.git
cd ReliefRoutes-AI
python -m venv venv
venv\Scripts\activate          # Windows  (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
streamlit run app.py
```
An internet connection is required (live APIs).

### Enable the chat assistant (optional, free)
Get a free key from [Google AI Studio](https://aistudio.google.com) (Get API key), then set it as an environment variable before starting the app:
```powershell
$env:GEMINI_API_KEY="your-key-here"
streamlit run app.py
```
or put it in `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-key"
```
The free tier is rate-limited. If the default model is rejected or the quota runs out, set `GEMINI_MODEL` to another model your key can use. Without a key the rule-based planner still works. Never commit keys; `.env` and `secrets.toml` are git-ignored.

### Reset test data
Stop the app, then run `python reset_db.py` (or `python reset_db.py --keep-centres`).

## Hackathon compliance notes
- Built during the Stage 1 build window; open-source libraries only (Streamlit, Folium, pandas, requests, google-genai).
- No dummy or hardcoded data; the app reads live APIs and a live database.
- Live demo only; no pre-recorded video.

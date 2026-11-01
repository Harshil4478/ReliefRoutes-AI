<<<<<<< HEAD
# 🚨 ReliefRoutes AI

### AI-Powered Emergency Response & Relief Coordination Platform

ReliefRoutes AI is an intelligent disaster-response platform designed to support emergency relief operations during floods, cyclones, and other natural disasters.

The platform helps identify affected locations, manage emergency requests, monitor available resources, coordinate relief centres, and plan road routes for delivering essential supplies.

## 🌍 Problem Statement

During natural disasters, emergency response teams often face challenges such as:
- Difficulty identifying affected locations.
- Lack of real-time visibility into available resources.
- Poor coordination between relief centres.
- Delays in delivering essential supplies.
- Difficulty selecting suitable routes for relief transportation.

## 💡 Our Solution

ReliefRoutes AI brings emergency requests, relief-centre inventory, weather information, route planning, and AI-assisted coordination into one platform.

## ✨ Key Features

- **Emergency Management:** Register emergencies, record severity, affected population, required supplies, and GPS coordinates.
- **Live Weather Monitoring:** Retrieve current weather conditions and rainfall forecasts.
- **Resource Inventory:** Track available food, water, medical supplies, and other resources.
- **Relief Centre Management:** Register centres, GPS locations, capacity, and available supplies.
- **Interactive Disaster Map:** Visualise emergency locations and relief centres.
- **Route Planning:** Calculate road routes between emergency locations and relief centres.
- **AI Relief Agent:** Support emergency-response decisions through AI-assisted coordination.

## 🛠️ Technology Stack

- Python
- Streamlit
- SQLite
- Folium
- OpenStreetMap
- OSRM
- Open-Meteo
- Pandas
- Altair

## 🏗️ Project Structure

```text
ReliefRoutes-AI/
│
├── app.py
├── dashboard_page.py
├── ui_theme.py
├── database.py
├── logistics.py
├── agent_core.py
├── weather_service.py
├── map_service.py
├── routing_service.py
├── relief_centres.py
├── route_planner_page.py
├── ai_agent_page.py
├── requirements.txt
└── README.md
```

## 🚀 Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Harshil4478/ReliefRoutes-AI.git
```

2. Navigate to the project directory:

```bash
cd ReliefRoutes-AI
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate it on Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
streamlit run app.py
```

## 🎯 Project Theme

Climate, Resource Infrastructure & Global Supply Resilience.

## 👥 Team

Developed as part of a GenAI Buildathon project.

## ⚠️ Disclaimer

Weather forecasts and calculated road routes are decision-support information. They do not independently verify flood conditions, road closures, or route safety. Emergency decisions should be confirmed by authorised response personnel.
=======
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
| Chat assistant (optional) | Anthropic Claude API (tool use) |

All emergencies, centres, stock and dispatches are entered by the operator at runtime and stored in a local SQLite database. The repository ships no seeded or hardcoded datasets.

## How the AI agent works
1. A deterministic planner (`recommendation_service.py`, `agent_core.py`) estimates the supplies each emergency needs from its people count, shortlists active centres by distance, fetches real OSRM road routes, and scores each centre by travel time plus a penalty for missing supplies.
2. All numbers (distance, stock, quantities) come from code, never from a language model.
3. The optional Claude assistant (`llm_agent.py`) uses the same functions as tools to investigate and **propose** dispatches. It has no approval tool.
4. The operator approves or rejects each proposal in the UI; approval creates the dispatch and reduces stock.

Limitation: OSRM does not know about flooded or closed roads. The app says so in every recommendation.

## Architecture
```
app.py                  Streamlit entry point and pages
dashboard_page.py       Dashboard
route_planner_page.py   Map-first route planner
ai_agent_page.py        AI agent UI (proposals + chat)
agent_core.py           Planner, proposals, tool functions
llm_agent.py            Claude tool-use loop (optional)
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

### Enable the chat assistant (optional)
Set an Anthropic API key, either as an environment variable `ANTHROPIC_API_KEY` or in `.streamlit/secrets.toml`:
```toml
ANTHROPIC_API_KEY = "your-key"
```
Without a key the rule-based planner still works. Never commit keys; `.env` and `secrets.toml` are git-ignored.

### Reset test data
Stop the app, then run `python reset_db.py` (or `python reset_db.py --keep-centres`).

## Hackathon compliance notes
- Built during the Stage 1 build window; open-source libraries only (Streamlit, Folium, pandas, requests, anthropic).
- No dummy or hardcoded data; the app reads live APIs and a live database.
- Live demo only; no pre-recorded video.
>>>>>>> 2356148 (Add README, requirements and DB reset script)

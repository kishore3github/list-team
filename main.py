from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import csv
from collections import defaultdict
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def load_team_data(csv_file: str):
    teams = defaultdict(list)
    if os.path.exists(csv_file):
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                teams[row['team']].append({'name': row['name'], 'role': row['role']})
    return teams

@app.get("/team-table", response_class=HTMLResponse)
def team_table(request: Request):
    team_data = load_team_data("team_members.csv")
    return templates.TemplateResponse("team.html", {"request": request, "teams": team_data})


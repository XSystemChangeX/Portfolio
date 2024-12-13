from fastapi import FastAPI, HTTPException #soo much work on this one!!# 
import requests
import uvicorn

app = FastAPI()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO # used BytesIO from the io module to handle the plot image in memory.To help save images into memory# 
from fastapi.responses import StreamingResponse

def check_team(team_id):
    api_url = f"https://api.balldontlie.io/v1/teams/{team_id}"
    api_key = "eb9e40ee-222b-4df7-b583-57ab3cbbd713"  # API key

    headers = {"Authorization": f"{api_key}"}

    response = requests.get(api_url, headers=headers)

    # List to store the responses
    team_list = []

    if response.status_code == 200:
        team_list.append(response.json())
    else:
        # if Team not found 
        raise HTTPException(status_code=response.status_code, detail="Team not found:DO you even BALL bro")

    #key information of the list
    team_data = team_list[0]
    team_name = team_data["data"]["name"]
    team_city = team_data["data"]["city"]
    team_abbreviation = team_data["data"]["abbreviation"]
    print(team_list)
    return team_name, team_city, team_abbreviation

#This is what I get from the API#
#    "data": {#
#"id": 1,#
#"abbreviation": "ATL",#
#"city": "Atlanta",#
#"conference": "East",#
# "division": "Southeast",#
# "full_name": "Atlanta Hawks",#
#"name": "Hawks",#
#"owner": "Atlanta Spirit, LLC",#
#"state": "Georgia"#

@app.get("/")
def read_root():
    str_welcome = "Welcome to my Cool App that allows you to find basketball teams and then plot their games for 2023"
    str_2 = "Please enter the team id using the endpoint /team/{team_id}(i.e., number from 1 to 30)"
    str_3 = "To view a plot of points per game, use /team/{team_id}/plot."
    return {
        "Welcome Message": str_welcome,
        "team_info": str_2,
        "plot_info": str_3
    }
#For ploting game season#
def get_team_games(team_id):
    api_url = "https://api.balldontlie.io/v1/games"
    api_key = "eb9e40ee-222b-4df7-b583-57ab3cbbd713"
    headers = {"Authorization": f"{api_key}"}
    params = {
        "team_ids[]": team_id,
        "per_page": 100, #100 seems to do the trick here
        "seasons[]": 2023 #The NBA's regular season runs from October to April, with each team playing 82 games.#
    }
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200: ##I haven't set up a "if/else" response for an error#
        games_data = response.json()
        return games_data["data"]

# Get team information
@app.get("/team/{team_id}")
def get_team_info(team_id: int):
    team_name, team_city, team_abbreviation = check_team(team_id)
    str_team = (
        f"The team with id number {team_id} is {team_name}. "
        f"It is located in {team_city} and the abbreviation is {team_abbreviation}"
    )
    return {"team_info": str_team}

## Endpoint to generate and return the plot image for a teams points per game
@app.get("/team/{team_id}/plot")
def get_team_points_plot(team_id: int):
    games = get_team_games(team_id)
    if not games:
        return {"message": "No game data available for this team."}

    image = generate_points_per_game_plot(games, team_id)
    return StreamingResponse(image, media_type="image/png")
def generate_points_per_game_plot(games, team_id):
    dates = []
    points = []
    results = []

    for game in games:
        game_date = game["date"][:10]
        if game["home_team"]["id"] == team_id:
            team_score = game["home_team_score"]
            opponent_score = game["visitor_team_score"]
        else:
            team_score = game["visitor_team_score"]
            opponent_score = game["home_team_score"]

        # Determine win or loss
        result = 'Win' if team_score > opponent_score else 'Loss'

        dates.append(game_date)
        points.append(team_score)
        results.append(result)

    # Create DataFrame
    data = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Points': points,
        'Result': results
    })

    # to sort the data by date. 
    data = data.sort_values('Date')

    # Calculate moving average
    data['Moving_Average'] = data['Points'].rolling(window=5).mean()

    # the background style, it looks without it as well, but this provides a bit more clarity.
    sns.set(style="whitegrid")

    # Create plot
    plt.figure(figsize=(10, 6))

    # Plot points with color-coded wins/losses
    sns.scatterplot(x='Date', y='Points', hue='Result', data=data, style='Result', s=100)
    plt.plot(data['Date'], data['Points'], alpha=0.3)

    # Plot moving average
    sns.lineplot(x='Date', y='Moving_Average', data=data, label='5-Game Moving Average', color='purple')
     
    plt.xlabel('Date')
    plt.ylabel('Points Scored by Ballers (i.e., Team)')
    plt.title('Points Per Game with Moving Average (Wins vs Losses)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Save generated plot as a PNG image and returning to user
    myimage = BytesIO()
    plt.savefig(myimage, format='png')
    plt.close()
    myimage.seek(0)
    return myimage

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
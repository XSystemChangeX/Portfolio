from fastapi import FastAPI
import requests
import uvicorn
app = FastAPI()


def check_team(team_id):
    api_url = f"https://api.balldontlie.io/v1/teams/{team_id}"
    api_key = "eb9e40ee-222b-4df7-b583-57ab3cbbd713"

    headers = {"Authorization": f"{api_key}"}

    response = requests.get(api_url, headers=headers)

    # List to store the responses
    team_list = []

    if response.status_code == 200:
        team_list.append(response.json())

    # Use the key information of the list
    team_name = team_list[0]["data"]["name"]
    team_city = team_list[0]["data"]["city"]
    team_abbreviation = team_list[0]["data"]["abbreviation"]
    print(team_list)
    return team_name, team_city,team_abbreviation


#First page
@app.get("/")
def read_root():
    str_welcome = "Welcome to the BasketBall API!"
    str_2 = f"Please enter the team id  using the end point /team/team_id."
    return {"Welcome Message": str_welcome,
           "team_info": str_2}

# Get team information
@app.get("/team/{team_id}")
def get_team_info(team_id:int):
    team_name, team_city,team_abbreviation = check_team(team_id)
    str_team = f"The team with id number {team_id} is {team_name}. It is located in {team_city} and the abbrevation is {team_abbreviation}"
    return {"team_info": str_team}



uvicorn.run(app,host='0.0.0.0',  port="8080")


# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn  as sns


sns.set_theme()

# create data
values=np.cumsum(np.random.randn(100,1))

#use the plot function
plt.plot(values)

#Show the graph
plt.show()

import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("spotify.csv")
dataframe=pd.DataFrame(data)
dfh=dataframe.head(20)
dfh.plot(x="track_name",y="in_spotify_playlists",kind="bar",title="music stream hours")
plt.show()
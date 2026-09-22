from nba_api.stats.endpoints import playergamelogs

logs = playergamelogs.PlayerGameLogs(
    season_nullable="2024-25",
    season_type_nullable="Regular Season"
)

df = logs.get_data_frames()[0]

#print(df.head())
#print(df.shape)

print(df.columns.tolist())
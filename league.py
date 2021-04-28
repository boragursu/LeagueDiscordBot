from riotwatcher import LolWatcher, ApiError

key= "RGAPI-44aadfb9-c5c4-474e-891f-03f567bdbd9d"
lol_watcher = LolWatcher(key)

my_region = "tr1"
me = lol_watcher.summoner.by_name(my_region, "Dalyn")
ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])

summoner_name = ranked_stats[0]["summonerName"]
rank = ranked_stats[0]["rank"]
tier = ranked_stats[0]["tier"]
leaguepoint = ranked_stats[0]["leaguePoints"]
wins = int(ranked_stats[0]["wins"])
losses = int(ranked_stats[0]["losses"])
winrate = round((wins/(losses+wins)) * 100)

print (f"Hello {summoner_name} your current season rank is {tier} {rank}, your current LP is {leaguepoint}, your current winrate is %{winrate}")

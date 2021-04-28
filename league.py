from riotwatcher import LolWatcher, ApiError
def read_riotapi_token():
    with open("tokens.txt" , "r") as f:
        lines = f.readlines()
        return lines[1].strip()
key = read_riotapi_token()
lol_watcher = LolWatcher(key)
def printOutFlexPlayerData(inputted_name,my_region):
    me = lol_watcher.summoner.by_name(my_region, inputted_name)
    ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])

    summoner_name = ranked_stats[0]["summonerName"]
    flexrank = ranked_stats[0]["rank"]
    flextier = ranked_stats[0]["tier"]
    flexleaguepoint = ranked_stats[0]["leaguePoints"]
    flexwins = int(ranked_stats[0]["wins"])
    flexlosses = int(ranked_stats[0]["losses"])
    flexwinrate = round((flexwins/(flexlosses+flexwins)) * 100)
    return f"Hello {summoner_name} your current season flex queue rank is {flextier} {flexrank}, your current LP is {flexleaguepoint}, your current winrate is %{flexwinrate}"

def printOutPlayerData(inputted_name,my_region):
    me = lol_watcher.summoner.by_name(my_region, inputted_name)
    ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
    summoner_name = ranked_stats[0]["summonerName"]
    rank = ranked_stats[1]["rank"]
    tier = ranked_stats[1]["tier"]
    leaguepoint = ranked_stats[1]["leaguePoints"]
    wins = int(ranked_stats[1]["wins"])
    losses = int(ranked_stats[1]["losses"])
    winrate = round((wins/(losses+wins)) * 100)
    
    return f"Hello {summoner_name} your current season solo/duo queue rank is {tier} {rank}, your current LP is {leaguepoint}, your current winrate is %{winrate}"
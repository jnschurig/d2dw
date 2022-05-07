
# Helpful webpage: https://dev.dota2.com/forum/dota-2/spectating/replays/webapi/48733-dota-2-match-history-webapi
# More helpful: https://dev.dota2.com/forum/dota-2/spectating/replays/webapi/60177-things-you-should-know-before-starting

STEAM_API_SECRET = 'steam/api'
BASE_API_URL = 'https://api.steampowered.com/'

APPLICATIONS = {
    'dota2_matches': {
        'name': 'IDOTA2Match_570',
        'version': 'V001',
        'methods': {
            'history': 'GetMatchHistory',
            'details': 'GetMatchDetails',
            'history_by_sequence': 'GetMatchHistoryBySequenceNum',
            'league_listing': 'GetLeagueListing',
            'league_live_games': 'GetLiveLeagueGames',
            'scheduled_league_games': 'GetScheduledLeagueGames',
            'team_info_by_id': 'GetTeamInfoByTeamID',
            'tournament_player_stats': 'GetTournamentPlayerStats',
            'top_live_game': 'GetTopLiveGame',
        },
    },
    'dota2_econ': {
        'name': 'IEconDOTA2_570',
        'version': 'v1',
        'methods': {
            'heroes': 'GetHeroes',
            'items': 'GetGameItems',
            'icon': 'GetItemIconPath',
        },
    },
    'steam_users': {
        'name': 'ISteamUser',
        'version': 'v2',
        'methods': {
            'player_summaries': 'GetPlayerSummaries',
        }
    },
}

DEFAULT_LANGUAGE = 'en'
DEFAULT_RESULT_FORMAT = 'json' # xml is the only other option. json is default anyway.
# API_VERSION = 'v1' # Might need 'V001' if this doesn't work universally.

ALTERNATE_LANGUAGES = [
    'fr',
    'de',
]

# STEAMID64 - 76561197960265728 = STEAMID32
# STEAMID32 + 76561197960265728 = STEAMID64
SIXTY_FOUR_BIT_OFFSET = 76561197960265728 

DEFAULT_AWS_REGION = 'us-west-2'

DEFAULT_BATCH_SIZE = 100

VALID_RUN_MODES = ['detail', 'history', 'tournament', 'game_mode', 'bulk']

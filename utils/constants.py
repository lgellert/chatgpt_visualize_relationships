from conversations.EightiesMoviesConversation import EightiesMovieRecommendations
from conversations.FastFoodConversation import FastFoodConversation
from conversations.PianoPiecesConversation import PianoPiecesConversation

COMMAND_ALL = 'All'
COMMAND_DOWNLOAD = 'download'
COMMAND_VISNETWORK = 'visnetwork'
COMMAND_CHOICES = [COMMAND_ALL, COMMAND_DOWNLOAD, COMMAND_VISNETWORK]

MODEL_GPT35TURBO = 'gpt-3.5-turbo'
# MODEL_GPT4 = 'gpt-4'
MODEL_CHOICES = [MODEL_GPT35TURBO]

TOPIC_ALL = 'All'
TOPIC_80SMOVIES = '80sMovies'
TOPIC_FASTFOOD = 'FastFood'
TOPIC_PIANO_PIECES = 'PianoPieces'
TOPIC_CHOICES = [TOPIC_ALL, TOPIC_80SMOVIES, TOPIC_FASTFOOD, TOPIC_PIANO_PIECES]

TOPIC_CLASSES = {
    TOPIC_80SMOVIES: EightiesMovieRecommendations,
    TOPIC_FASTFOOD: FastFoodConversation,
    TOPIC_PIANO_PIECES: PianoPiecesConversation
}




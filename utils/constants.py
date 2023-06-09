from conversations.EightiesMoviesConversation import EightiesMovieConversation
from conversations.FastFoodConversation import FastFoodConversation
from conversations.PianoPiecesConversation import PianoPiecesConversation
from conversations.PrescriptionDrugsConversation import PrescriptionDrugsConversation

COMMAND_DOWNLOAD = 'download'
COMMAND_BUILD = 'build'
COMMAND_VISNETWORK = 'visnetwork'
COMMAND_CIRCULAR_PLOT = 'circular'
COMMAND_SCIKIT_SVG = 'svg'
COMMAND_TOP_NODES = 'topnodes'
COMMAND_CHOICES = [COMMAND_DOWNLOAD, COMMAND_BUILD, COMMAND_VISNETWORK, COMMAND_CIRCULAR_PLOT, COMMAND_SCIKIT_SVG,
                   COMMAND_TOP_NODES]

MODEL_GPT35TURBO = 'gpt-3.5-turbo'
MODEL_GPT35TURBO_0301 = 'gpt-3.5-turbo-0301'
MODEL_GPT4 = 'gpt-4'
MODEL_GPT4_0314 = 'gpt-4-0314'
MODEL_GPT4_32K = 'gpt-4-32k'
MODEL_GPT4_32K_0314 = 'gpt-4-32k-0314'

MODEL_CHOICES = [MODEL_GPT35TURBO,
                 MODEL_GPT35TURBO_0301,
                 MODEL_GPT4,
                 MODEL_GPT4_0314,
                 MODEL_GPT4_32K,
                 MODEL_GPT4_32K_0314]

TOPIC_ALL = 'all'
TOPIC_80SMOVIES = EightiesMovieConversation.title
TOPIC_FASTFOOD = FastFoodConversation.title
TOPIC_PIANO_PIECES = PianoPiecesConversation.title
TOPIC_PRESCRIPTION_DRUGS = PrescriptionDrugsConversation.title
TOPIC_CHOICES = [TOPIC_ALL,
                 TOPIC_80SMOVIES,
                 TOPIC_FASTFOOD,
                 TOPIC_PRESCRIPTION_DRUGS,
                 TOPIC_PIANO_PIECES]

TOPIC_CLASSES = {
    TOPIC_80SMOVIES: EightiesMovieConversation,
    TOPIC_FASTFOOD: FastFoodConversation,
    TOPIC_PRESCRIPTION_DRUGS: PrescriptionDrugsConversation,
    TOPIC_PIANO_PIECES: PianoPiecesConversation,
}




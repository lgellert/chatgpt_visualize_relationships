import argparse
import pprint
import sys
from datetime import datetime

from utils.constants import COMMAND_CHOICES, TOPIC_CHOICES, TOPIC_ALL, COMMAND_ALL, MODEL_GPT35TURBO, MODEL_CHOICES, \
    TOPIC_CLASSES, COMMAND_DOWNLOAD, COMMAND_VISNETWORK
from utils.utils import process_conversation, output_pyvis, load_previous_conversation_results, output_circular

VERSION = '1.0'

start_time = datetime.now()

# setup up command line arguments
parser = argparse.ArgumentParser(description='ChatGPT Visualize Relationships command line utility.')

parser.add_argument('-command',
                    metavar='command',
                    choices=COMMAND_CHOICES,
                    default=COMMAND_ALL,
                    type=str,
                    help='The command to run: ' + str(COMMAND_CHOICES) + '.')

parser.add_argument('-topic',
                    metavar='topic',
                    choices=TOPIC_CHOICES,
                    default=TOPIC_ALL,
                    type=str,
                    help='The topic: ' + str(TOPIC_CHOICES) + '.')

parser.add_argument('-model',
                    metavar='model',
                    choices=MODEL_CHOICES,
                    default=MODEL_GPT35TURBO,
                    type=str,
                    help='The ChatGPT model: ' + str(MODEL_CHOICES) + '.')

parser.add_argument('-v',
                    '--verbose',
                    default=True,
                    action='store_true',
                    help='Run in verbose mode.')

parser.add_argument('--version', action='version',
                    version='ChatGPT Visualize Relationships %s' % VERSION)

args = parser.parse_args()
# print(args)


print('Starting ChatGPT: %s' % start_time)

if args.verbose:
    print('Running with arguments: ' + pprint.pformat(args))


# setup topics to run through default to all
topics = TOPIC_CLASSES
# if a specific topic is passed, just processes the one they picked
if not args.topic == TOPIC_ALL:
    topics = {args.topic: TOPIC_CLASSES[args.topic]}

# loop over the selected topics
for name, convoClass in topics.items():

    # build the conversation class
    conversation = convoClass(model=args.model, verbose=args.verbose)

    # based on the command, run a certain set of steps
    if args.command == COMMAND_ALL:
        result = process_conversation(conversation)
        output_pyvis(conversation, result)

    if args.command == COMMAND_DOWNLOAD:
        result = process_conversation(conversation)

    if args.command == COMMAND_VISNETWORK:
        # load the JSON file from disk
        result = load_previous_conversation_results(conversation)
        if not result:
            sys.exit('Unable to continue, see previous error')
        # output_pyvis(conversation, result)
        output_circular(conversation, result)




end_time = datetime.now()
duration = end_time - start_time
print('Script Complete! Duration: %s' % duration)



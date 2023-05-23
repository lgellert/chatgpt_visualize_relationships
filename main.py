import argparse
import pprint
import sys
from datetime import datetime

from utils.constants import COMMAND_CHOICES, TOPIC_CHOICES, TOPIC_ALL, MODEL_GPT35TURBO, MODEL_CHOICES, \
    TOPIC_CLASSES, COMMAND_DOWNLOAD, COMMAND_VISNETWORK, COMMAND_CIRCULAR_PLOT, COMMAND_SCIKIT_SVG, \
    COMMAND_BUILD, COMMAND_TOP_NODES
from utils.utils import process_conversation, output_pyvis, load_previous_conversation_results, output_circular, \
    output_svg, output_top_nodes

VERSION = '1.0'

start_time = datetime.now()

# setup up command line arguments
parser = argparse.ArgumentParser(description='ChatGPT Visualize Relationships command line utility.')

parser.add_argument('-command',
                    metavar='command',
                    choices=COMMAND_CHOICES,
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

print('Starting Program - ChatGPT Visualize Relationships: %s' % start_time)

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
    if args.command == COMMAND_DOWNLOAD:
        result = process_conversation(conversation)

    else:
        # all other commands rely on JSON being downloaded already
        # load the JSON file from disk
        result = load_previous_conversation_results(conversation)
        if not result:
            sys.exit('Unable to continue, see previous error')

        if args.command == COMMAND_VISNETWORK:
            output_pyvis(conversation, result)

        if args.command == COMMAND_CIRCULAR_PLOT:
            output_circular(conversation, result)

        if args.command == COMMAND_SCIKIT_SVG:
            output_svg(conversation, result)

        if args.command == COMMAND_TOP_NODES:
            output_top_nodes(conversation, result)

        if args.command == COMMAND_BUILD:
            output_pyvis(conversation, result)
            output_circular(conversation, result)
            output_svg(conversation, result)
            output_top_nodes(conversation, result)



end_time = datetime.now()
duration = end_time - start_time
print('Program Complete! Duration: %s' % duration)



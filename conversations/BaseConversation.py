
import openai


class BaseConversation(object):
    """
    Abstract class providing interface for getting a list of items from OpenAI ChatGPT,
    and getting recommended/related items.
    """

    title = ''
    opening_conversation = []
    recommendations_conversation = []

    def __init__(self, model='gpt-3.5-turbo', temperature=0.5, verbose=False):
        self.model = model
        self.temperature = temperature
        self.verbose = verbose

    def get_title(self):
        return self.title

    def get_base_filename(self):
        return self.title.lower().replace(' ', '_') + '_' + self.model

    def call_open_ai(self, messages):

        # API key, or run `export OPENAI_API_KEY='sk-...'` in your terminal and leave this line commented out
        # openai.api_key = 'sk-...'
        completion = openai.ChatCompletion.create(model=self.model,
                                                  messages=messages,
                                                  temperature=self.temperature)
        return completion

    def collect_data(self):
        initial_list = self.get_initial_list()

        # loop the initial results and get recommendation / related items
        for row in initial_list:
            recommendations = self.get_recommendations(row['name'])
            row['recommendations'] = recommendations

        return initial_list

    def get_initial_list(self):

        try:
            result = self.call_open_ai(self.opening_conversation)
        except Exception as e:
            print('Unable to get initial data from OpenIA')
            raise e

        items = list()
        try:
            raw_answer = result['choices'][0]['message']['content']

            for line in raw_answer.splitlines():
                line = self.clean_line(line)

                if self.skip_line(line):
                    continue

                if self.verbose:
                    print('Found initial: ' + line)

                items.append({'name': line, 'recommendations': []})

            if not items:
                print('Nothing came back?')
                print(raw_answer)

            return items

        except Exception as e:
            print('Unable to parse JSON as string')
            print('Raw result was ' + str(result))
            raise e

    def get_recommendations(self, name):

        try:
            if self.verbose:
                print('Getting recommendations for: ' + name)

            # swap in the name of the actual thing to get recommedations for
            # substituting {name} in the string for the name passed in
            messages = self.recommendations_conversation
            messages[0]['content'] = messages[0]['content'].replace('{name}', name)

            result = self.call_open_ai(messages)
        except Exception as e:
            print('Unable to get recommendations from OpenIA')
            raise e

        items = list()
        try:

            raw_answer = result['choices'][0]['message']['content']

            for line in raw_answer.splitlines():
                line = self.clean_line(line)

                if self.skip_line(line):
                    continue

                if self.verbose:
                    print('\tFound recommendation: ' + line)

                items.append({'name': line})

            if not items:
                print('Nothing came back?')
                print(raw_answer)

            return items

        except Exception as e:
            print('Unable to parse JSON as string')
            print('Raw result was ' + str(result))
            raise e

    def clean_line(self, line):
        """
        Cleanup string data from ChatGPT.
        :param line: string from ChatGPT
        :return:
        """

        line = line.strip()

        # clean up the 'bullets' it adds to lists
        if line.startswith('- '):
            line = line[2:]

        # clean up the numbering even though WE TOLD IT NOT TO!
        for i in range(1, 100):
            if line.startswith(str(i) + '. '):
                x = len(str(i)) + 2
                line = line[x:]

        return line

    def skip_line(self, line):
        """
        Helper method to tell if this line is chatter from ChatGPT that can be ignored.

        :param line: string returned from ChatGPT
        :return:
        """

        # skip empty lines
        if not line:
            return True

        # it is trying to be friendly, but we don't want this garbage in the data
        if line.startswith('Sure, I') or \
            line.startswith('Sure I') or \
            line.startswith('Sure, here') or \
            line.startswith('Sure here') or \
            line.startswith('Here are') or \
            line.startswith('Okay, here') or \
            line.startswith('Okay here'):
            return True

        return False


from conversations.BaseConversation import BaseConversation


class EightiesMovieRecommendations(BaseConversation):

    title = '1980\'s Movies'
    opening_conversation = [
        {
            'role': 'user',
            'content': 'create a list of the top 25 movies from the 1980\'s'
        },
        {
            'role': 'user',
            'content': 'Provide the movie title only with one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    recommendations_conversation = [
        {
            'role': 'user',
            'content': 'I\'ve enjoyed watching the movie {name}'
        },
        {
            'role': 'user',
            'content': 'create a list of 10 other movies I might enjoy watching also from the 1980\'s in a similar genre'
        },
        {
            'role': 'user',
            'content': 'Provide the movie title without the year, one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    def clean_line(self, line):
        line = super(EightiesMovieRecommendations, self).clean_line(line)

        # clean up inconsistencies
        if line == 'E.T. the Extra-Terrestrial':
            line = 'E.T. the Extra Terrestrial'

        return line

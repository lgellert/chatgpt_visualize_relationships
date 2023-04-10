from conversations.BaseConversation import BaseConversation


class EightiesMovieRecommendations(BaseConversation):

    title = 'Eighties Movies'
    opening_conversation = [
        {
            'role': 'user',
            'content': 'create a list of the top 20 movies from the 1980\'s'
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
            'content': 'create a list of 5 other movies I might enjoy watching also from the 1980\'s'
        },
        {
            'role': 'user',
            'content': 'Provide the movie title without the year, one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

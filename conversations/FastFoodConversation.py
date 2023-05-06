from conversations.BaseConversation import BaseConversation


class FastFoodConversation(BaseConversation):

    title = 'FastFood'
    opening_conversation = [
        {
            'role': 'user',
            'content': 'create a list of the top 20 most popular fast food restaurants'
        },
        {
            'role': 'user',
            'content': 'Provide the response with one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    recommendations_conversation = [
        {
            'role': 'user',
            'content': 'I\'ve been enjoying eating at the fast food restaurant {name}'
        },
        {
            'role': 'user',
            'content': 'create a list of 8 similar fast food restaurants that offer similar food that I might enjoy eating at'
        },
        {
            'role': 'user',
            'content': 'Provide the response with one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    def clean_line(self, line):
        line = super(FastFoodConversation, self).clean_line(line)

        # clean up inconsistencies
        if line == 'Chipotle Mexican Grill':
            line = 'Chipotle'

        if line == 'Little Caesars':
            line = 'Little Caesars Pizza'

        if line == 'Papa John\'s':
            line = 'Papa John\'s Pizza'

        if line == 'Domino\'s':
            line = 'Domino\'s Pizza'

        if line == 'Papa Murphy\'s':
            line = 'Papa Murphy\'s Pizza'

        if line == 'Popeyes Louisiana Kitchen':
            line = 'Popeyes'

        if line == 'KFC (Kentucky Fried Chicken)':
            line = 'KFC'

        if line == 'Dunkin\'' or line == 'Dunkin':
            line = 'Dunkin\' Donuts'

        if line == 'Hardee\'s/Carl\'s Jr.':
            line = 'Carl\'s Jr'

        if line == 'Carl\'s Jr.':
            line = 'Carl\'s Jr'

        if line == 'Dairy Queen (for their chicken strip baskets)':
            line = 'Dairy Queen'

        return line


from conversations.BaseConversation import BaseConversation


class PianoPiecesConversation(BaseConversation):

    title = 'Piano Pieces'
    opening_conversation = [
        {
            'role': 'user',
            'content': 'create a list of the top 20 most played classical piano pieces '
                       'ranging in difficulty from beginner to advanced'
        },
        {
            'role': 'user',
            'content': 'for pieces composed by Johann Sebastian Bach include the BWV number after the name of the piece and before the composer\'s name'
        },
        {
            'role': 'user',
            'content': 'for pieces composed by Wolfgang Amadeus Mozart include the K number after the name of the piece and before the composer\'s name'
        },
        {
            'role': 'user',
            'content': 'Provide the response with one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    recommendations_conversation = [
        {
            'role': 'user',
            'content': 'I\'ve been enjoying playing the classical piano piece {name}'
        },
        {
            'role': 'user',
            'content': 'create a list of 8 similar pieces a student might also enjoy playing at that level'
        },
        {
            'role': 'user',
            'content': 'make sure the recommended pieces include some works by other composers'
        },
        {
            'role': 'user',
            'content': 'for pieces composed by Johann Sebastian Bach include the BWV number after the name of the piece and before the composer\'s name'
        },
        {
            'role': 'user',
            'content': 'for pieces composed by Wolfgang Amadeus Mozart include the K number after the name of the piece and before the composer\'s name'
        },
        {
            'role': 'user',
            'content': 'Provide the response with one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    def clean_line(self, line):
        line = super(PianoPiecesConversation, self).clean_line(line)

        # always remove all () since ChatGPT sometimes puts them in, sometimes does not
        line = line.replace('(', '')
        line = line.replace(')', '')

        # remove other chatter
        line = line.replace(',', '')
        line = line.replace('"', '')
        line = line.replace('\'', '')
        line = line.replace(': ', ':')

        # standardize No, Op
        line = line.replace('No. ', 'No')
        line = line.replace('No.', 'No')
        line = line.replace('No ', 'No')

        line = line.replace('Op. ', 'Op')
        line = line.replace('Op.', 'Op')
        line = line.replace('Op ', 'Op')

        line = line.replace('minor', 'Minor')
        line = line.replace('major', 'Major')

        line = line.replace(' flat ', '-flat')
        line = line.replace(' Flat ', '-flat')
        line = line.replace('-Flat ', '-flat')
        line = line.replace(' sharp ', '-sharp')
        line = line.replace(' Sharp ', '-sharp')
        line = line.replace('-Sharp ', '-sharp')

        # fix oddballs
        line = line.replace('Frédéric', 'Frederic')
        line = line.replace('Für', 'Fur')
        line = line.replace('Gymnopédie', 'Gymnopedie')

        # clean up the stupid (K545) vs (K 545) vs (K.545)
        if 'mozart' in line.lower():
            line = line.replace('K. ', 'K')
            line = line.replace('K.', 'K')
            line = line.replace('K ', 'K')

        if 'bach' in line.lower():
            line = line.replace('BWV. ', 'BWV')
            line = line.replace('BWV.', 'BWV')
            line = line.replace('BWV ', 'BWV')

            line = line.replace('BWVAnh. ', 'BWV')
            line = line.replace('BWVAnh.', 'BWV')
            line = line.replace('BWVAnh ', 'BWV')
            line = line.replace('BWVAnh', 'BWV')

        return line


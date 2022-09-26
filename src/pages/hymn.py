import json


class Hymn:

	@staticmethod
	def get_letter(path):

		with open(path) as file:
			hymn = json.load(file)

		title = hymn['title']

		letter = '\n\n'.join(hymn['letter'])

		out = title + '\n\n' + letter

		return out

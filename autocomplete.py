import sublime, sublime_plugin, apiparser, re

completion_items = apiparser.parse_api_dump()

FUNCTION_CALL_REGEX = re.compile(r"\b([\w\.]+)\s*\(?[\"\'](\w+)\b")

class_detections = [ "GetService", "FindService", "IsA", "Instance.new" ]

class AutoCompleteProvider(sublime_plugin.EventListener):
	"""
	The automatic completions provider.
	"""
	def on_query_completions(self, view, prefix, locations):
		def selected_completions = set()

		for location in locations:
			line = view.line(location)
			function_match = FUNCTION_CALL_REGEX.search(line)

			if function_match is not None and function_match.group(1) in class_detections:
				for class_match in [e.entry_completion for e in completion_items if e.entry_type == "Class" and e.entry_completion.lower().startswith(prefix.lower())]:
					selected_completions.add(class_match)

		return (selected_completions, sublime.INHIBIT_EXPLICIT_COMPLETIONS)
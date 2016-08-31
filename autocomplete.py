import sublime, sublime_plugin
import re
from ROBLOXLua.apiparser import parse_api_dump

completion_items = parse_api_dump()

FUNCTION_CALL_REGEX = re.compile(r"\b([\w\.]+)\s*\(?[\"\'](\w*)")

class_detections = [ "GetService", "FindService", "IsA", "Instance.new" ]

class AutoCompleteProvider(sublime_plugin.EventListener):
	"""
	The automatic completions provider.
	"""
	def on_query_completions(self, view, prefix, locations):
		selected_completions = set()

		for location in locations:
			if "source.rbxlua" not in view.scope_name(location):
				return

			line = view.substr(view.line(location))
			function_match = FUNCTION_CALL_REGEX.search(line)

			if function_match is not None and function_match.group(1) in class_detections:
				class_matches = [ e["entry_completion"] for e in completion_items if e["entry_type"] == "Class" ]
				for class_match in class_matches:
					selected_completions.add(class_match)

		if len(selected_completions) > 0:
			return ([ [e, e] for e in selected_completions ], sublime.INHIBIT_EXPLICIT_COMPLETIONS | sublime.INHIBIT_WORD_COMPLETIONS)
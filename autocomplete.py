import sublime, sublime_plugin
import re
from ROBLOXLua.apiparser import parse_api_dump

completion_items = parse_api_dump()

FUNCTION_CALL_REGEX = re.compile(r"\b([\w\.]+)\s*\(?[\"\']")

service_detections = [ "GetService", "FindService", "getService", "service" ]
creatable_detections = [ "Instance.new" ]
services = set([ e["entry_completion"] for e in completion_items if e["entry_type"] == "Class" and "service" in e["entry_tags"] ])
creatables = set([ e["entry_completion"] for e in completion_items if e["entry_type"] == "Class" and "notCreatable" not in e["entry_tags"] and "abstract" not in e["entry_tags"] and "service" not in e["entry_tags"] and "deprecated" not in e["entry_tags"] ])

class AutoCompleteProvider(sublime_plugin.EventListener):
	"""
	The automatic completions provider.
	"""
	def on_query_completions(self, view, prefix, points):
		selected_completions = set()

		for point in points:
			if "source.rbxlua" not in view.scope_name(point):
				return

			row_col = view.rowcol(point)
			line_region = view.line(point)
			line_text = view.substr(line_region)
			function_match = FUNCTION_CALL_REGEX.search(line_text, 0, row_col[1])

			if function_match is not None and function_match.end(0) >= row_col[1]:
				print(function_match.end(0), row_col[1])
				function_name = function_match.group(1)

				if function_name in service_detections:
					selected_completions.update(services)
				elif function_name in creatable_detections:
					selected_completions.update(creatables)

		if len(selected_completions) > 0:
			return ([ [e] for e in selected_completions ], sublime.INHIBIT_EXPLICIT_COMPLETIONS | sublime.INHIBIT_WORD_COMPLETIONS)
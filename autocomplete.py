import sublime, sublime_plugin
import re
from ROBLOXLua.apiparser import parse_api_dump

completion_items = parse_api_dump()

FUNCTION_CALL_REGEX = re.compile(r"\b(\w+)\s*\(?([\"\'])(\w*)\2?\)?")
ENUM_REGEX = re.compile(r"\bEnum\.(\w*)([\.:]?\w*)")

service_detections = [ "GetService", "FindService", "getService", "service" ]
creatable_detections = [ "Instance.new" ]
class_detections = [ "FindFirstOfClass" ]
classes = set([ e["entry_completion"] for e in completion_items if e["entry_type"] == "Class" ])
services = set([ e["entry_completion"] for e in completion_items if e["entry_type"] == "Class" and "service" in e["entry_tags"] ])
creatables = set([ e["entry_completion"] for e in completion_items if e["entry_type"] == "Class" and "notCreatable" not in e["entry_tags"] and "abstract" not in e["entry_tags"] and "service" not in e["entry_tags"] and "deprecated" not in e["entry_tags"] ])
enum_names = set([ e["entry_completion"] for e in completion_items if e["entry_type"] == "Enum" ])

class AutoCompleteProvider(sublime_plugin.EventListener):
	"""
	The automatic completions provider.
	"""
	def on_query_completions(self, view, prefix, points):
		selected_completions = set()

		for point in points:
			if "source.rbxlua" not in view.scope_name(point):
				return None

			row_col = view.rowcol(point)
			line_region = view.line(point)
			line_text = view.substr(line_region)
			function_match = FUNCTION_CALL_REGEX.search(line_text, 0, row_col[1])
			enum_match = ENUM_REGEX.search(line_text, 0, row_col[1])

			if function_match is not None and function_match.end(0) >= row_col[1]:
				function_name = function_match.group(1)
				value = None

				if function_name in service_detections:
					value = services
				elif function_name in creatable_detections:
					value = creatables
				elif function_name in class_detections:
					value = classes

				if value is not None:
					selected_completions.update([x for x in value if x.startswith(prefix)])
			elif enum_match is not None and enum_match.end(0) >= row_col[1]:
				if enum_match.group(2) is None or enum_match.group(2) == "":
					selected_completions.update(enum_names)
				else:
					if enum_match.group(2)[0] == ".":
						selected_completions.update(set([ e["entry_completion"] for e in completion_items if e["entry_type"] == "EnumItem" and e["enum_parent"] == enum_match.group(1) ]))
					else:
						selected_completions.add("GetEnumItems()")

		if len(selected_completions) > 0:
			return ([ [e] for e in selected_completions ], sublime.INHIBIT_EXPLICIT_COMPLETIONS | sublime.INHIBIT_WORD_COMPLETIONS)
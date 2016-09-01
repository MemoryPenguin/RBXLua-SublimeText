import re
from urllib.request import urlopen
from ROBLOXLua.extra_tags import apply_extra_tags

API_URL = r"http://anaminus.github.io/rbx/raw/api/latest.txt"
API_REGEX = re.compile(r"^\s*(\w+) (\w+)[ \.]?(\w*)[ \.:]*(\w*)(.*)")
TAG_REGEX = re.compile(r"\[(\w+)\]")
API_TAG_FILTERS = [ "hidden", "deprecated", "RobloxScriptSecurity", "RobloxScriptSecurity" ]

def parse_dump_line(line):
	"""
	Parses a line from the API dump.
	"""
	match = API_REGEX.match(line)
	line_type = match.group(1)
	remainder = match.group(5)
	tags = TAG_REGEX.findall(remainder)

	entry = {}
	entry["entry_type"] = line_type
	entry["entry_tags"] = tags

	if line_type == "Class":
		entry["class_name"] = match.group(2)
		entry["entry_completion"] = match.group(2)
	elif line_type == "Property" or line_type == "Function" or line_type == "YieldFunction" or line_type == "Callback":
		entry["entry_completion"] = match.group(4)
	elif line_type == "Event":
		entry["entry_completion"] = match.group(3)
	elif line_type == "Enum":
		entry["entry_completion"] = match.group(2)
		entry["entry_full_completion"] = "Enum.{0}".format(match.group(2))
	elif line_type == "EnumItem":
		entry["entry_completion"] = match.group(3)
		entry["enum_parent"] = match.group(2)
		entry["entry_full_completion"] = "Enum.{0}.{1}".format(match.group(2), match.group(3))

	return apply_extra_tags(entry)

def parse_api_dump():
	"""
	Fetches and parses the API dump from the server.
	"""
	raw_data = urlopen(API_URL)
	entries = []

	for line in raw_data:
		entries.append(parse_dump_line(line.decode()))

	return entries
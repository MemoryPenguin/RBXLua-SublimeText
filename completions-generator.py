import json, re, argparse, urllib2

DEFAULT_SOURCE = r"http://anaminus.github.io/rbx/raw/api/latest.txt"
BARRED_TAGS = [ "[hidden]", "[deprecated]", "[RobloxScriptSecurity]", "[RobloxScriptSecurity]" ]

api_regex = re.compile(r'^\s*(\w+) (\w+)[ \.]?(\w*)[ \.:]*(\w*)(.*)')
parser = argparse.ArgumentParser(description="Generates completions from an API dump.")
parser.add_argument("-s", "--source", help="Where to find the API dump (URL).", default=DEFAULT_SOURCE)
parser.add_argument("-v", "--verbose", help="Prints additional information to the output.", action="store_true")
parser.add_argument("location", help="Where to output the generated completions.")
args = parser.parse_args()

completion_items = set()

def process_api_match(match):
	line_type = match.group(1)
	remainder = match.group(5)
	inserted_item = None

	for tag in BARRED_TAGS:
		if tag in remainder:
			if args.verbose:
				print "Skipping {0}{1} because it has barred tag {2}".format(match.group(2), match.group(3), tag)

			return

	if line_type == "Class":
		inserted_item = match.group(2)
	elif line_type == "Property" or line_type == "Function" or line_type == "YieldFunction" or line_type == "Callback":
		inserted_item = match.group(4)
	elif line_type == "Event":
		inserted_item = match.group(3)
	elif line_type == "EnumItem":
		enum_name = match.group(2)
		item_name = match.group(3)
		inserted_item = "Enum.{0}.{1}".format(enum_name, item_name)
	elif line_type == "Enum":
		enum_name = match.group(2)
		inserted_item = "Enum.{0}".format(enum_name)
	else:
		print "Unknown line type {0}".format(line_type)

	if inserted_item:
		if args.verbose:
			print inserted_item

		completion_items.add(inserted_item)


def get_api_dump():
	raw_data = urllib2.urlopen(args.source)
	
	for line in raw_data:
		match = api_regex.match(line)
		process_api_match(match)

def main():
	get_api_dump()

	with open(args.location, "w") as outfile:
		json.dump({
			"scope": "source.rbxlua",
			"completions": list(completion_items)
		}, outfile)

	print "Wrote {0} completion items to {1}".format(len(completion_items), args.location)

if __name__ == '__main__':
	main()
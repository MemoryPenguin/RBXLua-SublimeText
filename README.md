# RBXLua for Sublime Text

This plugin adds support for [ROBLOX](https://roblox.com) Lua to Sublime Text 3. Currently it supports syntax highlighting, indentation, snippets, and an extremely comprehensive set of completions automatically generated from the API dump.

You will need Sublime Text 3 build 3084 or later to use syntax highlighting, which depends on the new `sublime-syntax` format. The earliest stable build with this support is build 3103.

Once installed, simply select the language using `Ctrl-Shift-P` and searching for `Set Syntax: ROBLOX Lua`, or open a `.lua` or `.rbxs` file. The language definition will by automatically applied to `.lua` and `.rbxs` file extensions. If it isn't applied to `.lua`, you may need to disable the default Lua package by adding its name to the `ignored_packages` array, so it looks like this:

```json
{
	"ignored_packages":
	[
		"Vintage",
		"Lua"
	]
}
```

## Images
*Images were captured using the [Boxy Ocean](https://packagecontrol.io/packages/Boxy%20Theme) theme and syntax highlighting.*
![Demo 1](images/demo-1.gif)

![Demo 2](images/demo-2.png)
# RBXLua for Sublime Text

This plugin adds support for [ROBLOX](https://roblox.com) Lua to Sublime Text 3. Currently it supports syntax highlighting, indentation, snippets, and an extremely comprehensive set of completions automatically generated from the API dump.

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
*Images were captured using [Boxy Ocean](https://packagecontrol.io/packages/Boxy%20Theme)*
![Demo 1](images/demo1.gif)

![Demo 2](images/demo2.png)
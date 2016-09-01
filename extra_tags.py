services = [
	"AdService",
	"AssetService",
	"BadgeService",
	"ChangeHistoryService",
	"Chat",
	"CollectionService",
	"ContentProvider",
	"CoreGui",
	"DataStoreService",
	"Debris",
	"GamePassService",
	"GroupService",
	"GuiService",
	"HapticService",
	"HttpService",
	"InsertService",
	"JointsService",
	"KeyframeSequenceProvider",
	"Lighting",
	"LogService",
	"MarketplaceService",
	"NetworkClient",
	"NetworkServer",
	"PathfindingService",
	"Players",
	"PointsService",
	"ReplicatedFirst",
	"ReplicatedStorage",
	"RunService",
	"ScriptContext",
	"Selection",
	"ServerScriptService",
	"ServerStorage",
	"SoundService",
	"StarterGui",
	"StarterPack",
	"Teams",
	"TeleportService",
	"TestService",
	"UserInputService",
	"Workspace"
]

def apply_extra_tags(entry):
	if entry["entry_type"] == "Class" and entry["class_name"] in services:
		entry["entry_tags"].append("service")

	return entry
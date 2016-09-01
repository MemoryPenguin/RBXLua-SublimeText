class TagDefinition(object):
	"""
	A definition of an extra tag.
	"""
	def __init__(self, name, matcher):
		super(TagDefinition, self).__init__()
		self.tag_name = name
		self.match_check = matcher

	def tag_matches(self, tag):
		return self.match_check(tag)

tag_definitions = []

services = [
	"AdService",
	"AssetService",
	"BadgeService",
	"ChangeHistoryService",
	"CollectionService",
	"ContextActionService",
	"ControllerService",
	"CookiesService",
	"DataStoreService",
	"FlagStandService",
	"FlyweightService",
	"CSGDictionaryService",
	"NonReplicatedCSGDictionaryService",
	"FriendService",
	"GamePassService",
	"GamepadService",
	"GroupService",
	"GuiService",
	"GuidRegistryService",
	"HapticService",
	"HttpRbxApiService",
	"HttpService",
	"InsertService",
	"JointsService",
	"LogService",
	"LoginService",
	"LuaWebService",
	"MarketplaceService",
	"NotificationService",
	"PathfindingService",
	"PersonalServerService",
	"PhysicsService",
	"PointsService",
	"RenderHooksService",
	"RunService",
	"RuntimeScriptService",
	"ScriptService",
	"ServerScriptService",
	"SocialService",
	"SoundService",
	"SpawnerService",
	"TeleportService",
	"TestService",
	"TextService",
	"TimerService",
	"TouchInputService",
	"TweenService",
	"UserInputService",
	"Workspace",
	"ContentProvider",
	"ContentFilter",
	"KeyframeSequenceProvider",
	"Chat",
	"Players",
	"ReplicatedFirst",
	"StarterPlayer",
	"StarterPack",
	"StarterGui",
	"Geometry",
	"Debris",
	"ScriptInformationProvider",
	"Selection",
	"ServerStorage",
	"ReplicatedStorage",
	"MeshContentProvider",
	"SolidModelContentProvider",
	"Lighting",
	"ScriptContext",
	"Teams",
	"VirtualUser",
	"Visit",
	"Stats",
	"GuiRoot",
	"CoreGui",
	"RobloxReplicatedStorage",
	"NetworkServer",
	"NetworkClient",
	"OneQuarterClusterPacketCacheBase",
	"ClusterPacketCache",
	"PhysicsPacketCache",
	"InstancePacketCache"
]

abstract = [
	"BackpackItem",
	"BasePart",
	"BasePlayerGui",
	"BaseScript",
	"BevelMesh",
	"BodyMover",
	"CharacterAppearance",
	"Clothing",
	"Constraint",
	"DataModelMesh",
	"DynamicRotate",
	"FaceInstance",
	"Feature",
	"FormFactorPart",
	"GenericSettings",
	"GuiBase",
	"GuiBase2d",
	"GuiBase3d",
	"GuiButton",
	"GuiItem",
	"GuiLabel",
	"GuiObject",
	"HandleAdornment",
	"HandlesBase",
	"Instance",
	"JointInstance",
	"LayerCollector",
	"Light",
	"LuaSourceContainer",
	"ManualSurfaceJointInstance",
	"NetworkPeer",
	"NetworkReplicator",
	"PVAdornment",
	"PVInstance",
	"Pages",
	"PartAdornment",
	"PartOperation",
	"PostEffect",
	"RbxLibrary",
	"ReflectionMetadataItem",
	"RootInstance",
	"SelectionLasso",
	"ServiceProvider"
]

notCreatable = [
	"PyramidPart",
	"PrismPart",
	"Terrain",
	"Toolbar",
	"Button"
]

tag_definitions.append(TagDefinition("service", lambda entry: entry["entry_type"] == "Class" and entry["class_name"] in services))
tag_definitions.append(TagDefinition("abstract", lambda entry: entry["entry_type"] == "Class" and entry["class_name"] in abstract))
tag_definitions.append(TagDefinition("notCreatable", lambda entry: entry["entry_type"] == "Class" and entry["class_name"] in notCreatable and "notCreatable" not in entry["entry_tags"]))

def apply_extra_tags(entry):
	for tag_def in tag_definitions:
		if tag_def.tag_matches(entry):
			entry["entry_tags"].append(tag_def.tag_name)

	return entry
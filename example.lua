local generated = {}

local function HaveGeneratedAt(x, z)
	-- If we've never generated anything in the row, we can't have generated at that cell.
	if generated[x] == nil then
		return false
	end

	-- Otherwise, check the cell.
	return generated[x][z]
end

local function MarkGeneratedAt(x, z)
	-- Create the array if it doesn't exist.
	if generated[x] == nil then
		generated[x] = {}
	end

	-- Mark the cell as generated, so HaveGeneratedAt returns true later.
	generated[x][z] = true
end

local function GenerateTerrain()
	for x = 1, width do
		for z = 1, height do
			-- If we've never generated a part at this position, then we should make one.
			if not HaveGeneratedAt(x, z) then
				-- ...create the part and position it where it needs to be...

				-- Ensure we don't regenerate the part.
				MarkGeneratedAt(x, z)
			end
		end
	end
end

print(math.atan2(1))

warn("Testing~ %s")

GenerateTerrain "Test"
GenerateTerrain {
	"This is a test too"
}

--[[
Testing testing
]]
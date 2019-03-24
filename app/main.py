# Gilda Six, Private Investigator
# A game by Astrofra
# Created for the PyWeek 27, theme "SIX"

import harfang as hg
import game_globals as gg

hg.LoadPlugins()

plus = hg.GetPlus()
plus.RenderInit(gg.width, gg.height, 4, hg.Windowed)
plus.SetWindowTitle("Gilda Six, Private Investigator")

hg.MountFileDriver(hg.StdFileDriver("./"))

game_scene = plus.NewScene(True, True)
plus.LoadScene(game_scene, "assets/main_scene.scn")

game_scene.UpdateAndCommitWaitAll()

while not plus.IsAppEnded():
	dt = plus.UpdateClock()
	plus.UpdateScene(game_scene, dt)

	plus.Flip()
	plus.EndFrame()

plus.RenderUninit()
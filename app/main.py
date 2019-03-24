# Gilda Six, Private Investigator
# A game by Astrofra
# Created for the PyWeek 27, theme "SIX"

import harfang as hg
import game_globals as gg
from math import sin, cos, pi


def GameCreateCamera():
	gg.camera_angle = hg.Vector3(0.0, pi/2.0, 0.0)
	gg.spawn_point = gg.scene.GetNode("spawn_point")
	gg.camera = plus.AddCamera(gg.scene)
	gg.camera.GetTransform().SetPosition(gg.spawn_point.GetTransform().GetPosition())
	gg.camera.GetTransform().SetRotation(gg.camera_angle)
	gg.scene.SetCurrentCamera(gg.camera)


hg.LoadPlugins()

plus = hg.GetPlus()
plus.RenderInit(gg.width, gg.height, 4, hg.Windowed)
plus.SetWindowTitle("Gilda Six, Private Investigator")

hg.MountFileDriver(hg.StdFileDriver("./"))

gg.scene = plus.NewScene(True, True)
plus.LoadScene(gg.scene, "assets/main_scene.scn")

gg.scene.UpdateAndCommitWaitAll()

GameCreateCamera()

while not plus.IsAppEnded():
	dt = plus.UpdateClock()
	plus.UpdateScene(gg.scene, dt)

	plus.Flip()
	plus.EndFrame()

plus.RenderUninit()
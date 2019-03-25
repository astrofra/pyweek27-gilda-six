# Gilda Six, Private Investigator
# A game by Astrofra
# Created for the PyWeek 27, theme "SIX"

import harfang as hg
import game_globals as gg
from math import sin, cos, pi, radians, degrees


def GameCreateCamera():
	gg.camera_angle = hg.Vector3(0.0, pi/2.0, 0.0)
	gg.spawn_point = gg.scene.GetNode("spawn_point")
	# camera Y controller
	gg.camera_y_controller = plus.AddDummy(gg.scene)
	gg.camera_y_controller.SetName("camera_y_controller")
	gg.camera_y_controller.GetTransform().SetPosition(gg.spawn_point.GetTransform().GetPosition())
	gg.camera_y_controller.GetTransform().SetRotation(gg.camera_angle * hg.Vector3(0.0, 1.0, 0.0))

	# camera
	gg.camera = plus.AddCamera(gg.scene)
	gg.camera.SetName("game_camera")
	gg.camera.GetTransform().SetParent(gg.camera_y_controller)
	gg.camera.GetTransform().SetRotation(gg.camera_angle * hg.Vector3(1.0, 0.0, 0.0))
	gg.scene.SetCurrentCamera(gg.camera)

	gg.camera_target_angle = hg.Vector3(gg.camera_angle)


def GameControlCamera(dt):
	mouse_device = hg.GetInputSystem().GetDevice("mouse")
	if mouse_device.IsButtonDown(hg.Button0):

		gg.mouse = hg.Vector2(mouse_device.GetValue(hg.InputAxisX), mouse_device.GetValue(hg.InputAxisY))
		mouse_speed = gg.prev_mouse - gg.mouse
		gg.prev_mouse = hg.Vector2(gg.mouse)
		# print("Mouse X: %f, Mouse Y: %f" % (mouse_speed.x, mouse_speed.y))

		gg.camera_target_angle.x -= radians(mouse_speed.y * hg.time_to_sec_f(dt) * gg.camera_rot_x_speed)
		gg.camera_target_angle.x = max(min(gg.camera_target_angle.x, gg.camera_rot_x_min_max.y), gg.camera_rot_x_min_max.x)
		gg.camera_target_angle.y += radians(mouse_speed.x * hg.time_to_sec_f(dt) * gg.camera_rot_y_speed)
	else:
		gg.mouse = hg.Vector2(mouse_device.GetValue(hg.InputAxisX), mouse_device.GetValue(hg.InputAxisY))
		gg.prev_mouse = hg.Vector2(gg.mouse)

	cam_dt = gg.camera_target_angle - gg.camera_angle
	if gg.camera_lazyness == 0:
		cam_dt *= hg.time_to_sec_f(dt)
	else:
		cam_dt *= hg.time_to_sec_f(dt) * (1.0 / gg.camera_lazyness)
	gg.camera_angle += cam_dt
	gg.camera.GetTransform().SetRotation(gg.camera_angle * hg.Vector3(1.0, 0.0, 0.0))
	gg.camera_y_controller.GetTransform().SetRotation(gg.camera_angle * hg.Vector3(0.0, 1.0, 0.0))


def GameDrawCross(p):
	w = 0.5
	gg.osd.Line(p.x - w, p.y, p.z, p.x + w, p.y, p.z, hg.Color.Yellow, hg.Color.Yellow)
	gg.osd.Line(p.x, p.y - w, p.z, p.x, p.y + w, p.z, hg.Color.Yellow, hg.Color.Yellow)
	gg.osd.Line(p.x, p.y, p.z - w, p.x, p.y, p.z + w, hg.Color.Yellow, hg.Color.Yellow)

hg.LoadPlugins()

plus = hg.GetPlus()
plus.RenderInit(gg.width, gg.height, 4, hg.Windowed)
plus.SetWindowTitle("Gilda Six, Private Investigator")

hg.MountFileDriver(hg.StdFileDriver("./"))

gg.scene = plus.NewScene(True, True)
plus.LoadScene(gg.scene, "assets/main_scene.scn")

gg.scene.UpdateAndCommitWaitAll()

gg.osd = hg.SimpleGraphicSceneOverlay(False)
gg.scene.AddComponent(gg.osd)

GameCreateCamera()

picker = hg.ScenePicking(plus.GetRenderSystem())

while not plus.IsAppEnded():
	dt = plus.UpdateClock()
	GameControlCamera(dt)
	plus.UpdateScene(gg.scene, dt)

	if picker.Prepare(gg.scene, False, True).get():
		mx, my = plus.GetMousePos()
		my = gg.height - my
		if plus.MouseButtonDown(hg.Button0):
			result, p = picker.PickWorld(gg.scene, mx, my)
			GameDrawCross(p)
			# print(start)

	plus.Flip()
	plus.EndFrame()

plus.RenderUninit()
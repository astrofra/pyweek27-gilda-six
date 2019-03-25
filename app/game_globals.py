import harfang as hg
from math import radians

scale = 0.75
width, height = int(1280 * scale), int(720 * scale)
scene = None
spawn_point = None

osd = None

camera_y_controller = None
camera = None
camera_angle = None
camera_target_angle = None
camera_lazyness = 0.1 # [0:1]

prev_mouse = hg.Vector2(0,0)
mouse = hg.Vector2(0,0)
camera_rot_x_speed = (height / 35.0)
camera_rot_y_speed = (width / 50.0)
camera_rot_x_min_max = hg.Vector2(radians(-10.0), radians(10.0))
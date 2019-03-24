import harfang as hg

scale = 0.75
width, height = int(1280 * scale), int(720 * scale)
scene = None
spawn_point = None
camera = None

camera_angle = None
camera_target_angle = None
camera_lazyness = 0.1 # [0:1]

prev_mouse = hg.Vector2(0,0)
mouse = hg.Vector2(0,0)
camera_rot_y_speed = (width / 50.0)
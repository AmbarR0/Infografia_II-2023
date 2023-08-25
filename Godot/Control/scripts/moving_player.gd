extends Node2D

signal touch()

@export var amplitude = 100
@export var speed = 1.0
var accum_time = 0.0
var next_x_pos
var offset = Vector2(200, 100)


# Called every frame. 'delta' is the elapsed time since the previous frame.
'''func _process(delta):
	accum_time += delta
	next_x_pos = amplitude * sin(speed * accum_time)
	if next_x_pos > 400:
		print("palyer emmitting signal")
		touch.emit()
	position.x += next_x_pos + offset.x
	position.y = offset.y
'''
func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("Right") - Input.get_action_strength("Left")
	input_vector.y = Input.get_action_strength("Down") - Input.get_action_strength("Up")
	input_vector = input_vector.normalized()
	
func _input(event):
	print(event)
	
	if Input.is_action_pressed("Down"):
		position.y -= 5
	if Input.is_action_pressed("Up"):
		position.y += 5
	if Input.is_action_pressed("Left"):
		position.x -= 5
	if Input.is_action_pressed("Right"):
		position.x += 5
	if Input.is_action_pressed("rotateL"):
		rotate(-0.1)
	if Input.is_action_pressed("rotateR"):
		rotate(0.1)

func _on_up_pressed():
		position.y -= 5


func _on_down_pressed():
		position.y += 5



func _on_right_pressed():
		position.x += 5


func _on_left_pressed():
		position.x -= 5


func _on_rotate_left_pressed():
		rotate(-0.1)


func _on_rotate_right_pressed():
		rotate(0.1)

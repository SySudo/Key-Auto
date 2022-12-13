from pynput import mouse, keyboard

print("1.Mouse   2.keyboard")
inputs = input("Type: ")

if inputs == "1":
	mos = mouse.Controller()
	while True:
		mos.click(mouse.Button.left)

elif inputs == "2":
	key = keyboard.Controller()
	while True:
		key.press(keyboard.Key.enter)

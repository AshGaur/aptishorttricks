import os
import random
import sys

from squares import squares
from percents import percents
from cubes import cubes
import colors

first_q = True

ops = ['squares','cubes','percents']
while(True):
	if not first_q:
		print(colors.OKBLUE+"#"*20+colors.ENDC)
	selected_op = random.choice(ops)[0]
	if len(sys.argv)>1:
		selected_op = sys.argv[1]
	if selected_op == "s":
		squares.practice()
	elif selected_op == "c":
		cubes.practice()
	elif selected_op == "p":
		percents.practice()
	else:
		print("Invalid choice")
		break
	first_q = False



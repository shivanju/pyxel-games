#Shapes
shape = (0, 1, 2, 3, 4, 5, 6)
shape_dict = {
	0 : 'I',
	1 : 'O',
	2 : 'J',
	3 : 'L',
	4 : 'T',
	5 : 'S',
	6 : 'Z'
}

#Direction
direction_L = 'L'
direction_R = 'R'
direction_U = 'U'
direction_D = 'D'

#Orientation
orientation = (0, 1, 2, 3)
orientation_dict = {
	0 : 'L',
	1 : 'U',
	2 : 'R',
	3 : 'D'
}
#order of clockwise rotation --> left, up, right, down
#all block will start from position (0, 3)
#config is wrt top left tile of grid (0, 0)
block_dict = {
	#all orientations of block I
	"I_L" : {(1, 0), (1, 1), (1, 2), (1, 3)},
	"I_U" : {(0, 2), (1, 2), (2, 2), (3, 2)},
	"I_R" : {(2, 0), (2, 1), (2, 2), (2, 3)},
	"I_D" : {(0, 1), (1, 1), (2, 1), (3, 1)},

	#all orientations of block O
	"O_L" : {(0, 1), (0, 2), (1, 1), (1, 2)},
	"O_U" : {(0, 1), (0, 2), (1, 1), (1, 2)},
	"O_R" : {(0, 1), (0, 2), (1, 1), (1, 2)},
	"O_D" : {(0, 1), (0, 2), (1, 1), (1, 2)},

	#all orientations of block J
	"J_L" : {(0, 0), (1, 0), (1, 1), (1, 2)},
	"J_U" : {(0, 2), (0, 1), (1, 1), (2, 1)},
	"J_R" : {(2, 2), (1, 0), (1, 1), (1, 2)},
	"J_D" : {(2, 0), (0, 1), (1, 1), (2, 1)},

	#all orientations of block L
	"L_L" : {(0, 2), (1, 0), (1, 1), (1, 2)},
	"L_U" : {(2, 2), (0, 1), (1, 1), (2, 1)},
	"L_R" : {(2, 0), (1, 0), (1, 1), (1, 2)},
	"L_D" : {(0, 0), (0, 1), (1, 1), (2, 1)},

	#all orientations of block S
	"S_L" : {(0, 1), (0, 2), (1, 0), (1, 1)},
	"S_U" : {(0, 1), (1, 1), (1, 2), (2, 2)},
	"S_R" : {(1, 1), (1, 2), (2, 0), (2, 1)},
	"S_D" : {(0, 0), (1, 0), (1, 1), (2, 1)},

	#all orientations of block Z
	"Z_L" : {(0, 0), (0, 1), (1, 1), (1, 2)},
	"Z_U" : {(0, 2), (1, 1), (1, 2), (2, 1)},
	"Z_R" : {(1, 0), (1, 1), (2, 1), (2, 2)},
	"Z_D" : {(0, 1), (1, 0), (1, 1), (2, 0)},

	#all orientations of block T
	"T_L" : {(1, 0), (1, 1), (1, 2), (0, 1)},
	"T_U" : {(0, 1), (1, 1), (2, 1), (1, 2)},
	"T_R" : {(1, 0), (1, 1), (1, 2), (2, 1)},
	"T_D" : {(0, 1), (1, 1), (2, 1), (1, 0)}
}


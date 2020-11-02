# Exemplo de botões com todos os cursores multiplataforma disponíveis

from tkinter import *
cursores_disponiveis = """X_cursor
arrow
based_arrow_down
based_arrow_up
boat
bogosity
bottom_left_corner
bottom_right_corner
bottom_side
bottom_tee
box_spiral
center_ptr
circle
clock
coffee_mug
cross
cross_reverse
crosshair
diamond_cross
dot
dotbox
double_arrow
draft_large
draft_small
draped_box
exchange
fleur
gobbler
gumby
hand1
hand2
heart
icon
iron_cross
left_ptr
left_side
left_tee
leftbutton
ll_angle
lr_angle
man
middlebutton
mouse
none
pencil
pirate
plus
question_arrow
right_ptr
right_side
right_tee
rightbutton
rtl_logo
sailboat
sb_down_arrow
sb_h_double_arrow
sb_left_arrow
sb_right_arrow
sb_up_arrow
sb_v_double_arrow
shuttle
sizing
spider
spraycan
star
target
tcross
top_left_arrow
top_left_corner
top_right_corner
top_side
top_tee
trek
ul_angle
umbrella
ur_angle
watch
xterm"""

CDarray = cursores_disponiveis.splitlines(False)
root = Tk()

framedoBagui = Frame(padx=25, pady=25)
framedoBagui.grid()

catual = []
catual.append(Button(framedoBagui, text="No cursors", padx="20", pady="10"))

iterador = 1
for cursor in CDarray:
    catual.append(Button(framedoBagui,text=cursor, cursor=cursor, padx="20", pady="10"))

iterador = 0

for botao in catual:
    catual[iterador].grid(column=(int(iterador/10)), row=iterador%10)
    iterador = iterador + 1

root.mainloop()
#setup
from tkinter import *
from datetime import datetime
from datetime import date
import math

#window setup
root = Tk()
root.title('Analog Clock')
root.configure(bg='#F1E9D2') #window colour
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#find center point
center_x = int(screen_width/2 - 300)
center_y = int(screen_height/2 - 225)
#set the position of the window to the center of the screen
root.geometry(f'{600}x{450}+{center_x}+{center_y}')
root.resizable(False, False) #stops resize
from datetime import datetime

#setup analog canvas
myCanvas = Canvas(root,width=300,height=300,bg='#F1E9D2')
myCanvas.place(x=10,y=10)

#am OR pm
now = datetime.now()
am_pm_text = "AM" if int(now.hour) < 12 else "PM"
am_pm_label = Label(root, text=am_pm_text, bg='#F1E9D2', font=('Courier New', 18))
am_pm_label.place(x=330, y=5)

#date
today = date.today()
date_text = today.strftime("%d/%m/%Y")
date_label = Label(root, text=date_text, bg='#F1E9D2', font=('Courier New', 16))
date_label.place(x=330, y=30)

#digital time
Canvas2 = Canvas(root,width=200,height=24,bg='#F1E9D2')
Canvas2.place(x=10,y=320)
time_now=datetime.now()
Canvas2.create_text(30,30,fill='black',font='Courier 16',text=time_now)

#moon phase image
CanvasMoon = Canvas(root,width=90,height=90,bg='#F1E9D2')
CanvasMoon.place(x=220,y=320)
date6Jan2000=datetime(2000,1,6)
datenow=datetime.now()
days_since = (datenow - date6Jan2000).days
lunar_day = days_since % 29.53058770576
if 0 < lunar_day <= 1:
    moon_phase = "New Moon"
    CanvasMoon.create_text(45,50,fill='black',font='Courier 96',text="●")
elif 1 < lunar_day <= 6.382647:
    moon_phase = "Waxing Crescent"
    CanvasMoon.create_text(50,55,fill='black',font='Courier 64',text="☽")
elif 6.382647 < lunar_day <= 8.382647:
    moon_phase = "First Quarter"
    CanvasMoon.create_text(45,50,fill='black',font='Courier 96',text="◐")
elif 8.382647 < lunar_day < 13.765295:
    moon_phase = "Waxing Gibbous"
    CanvasMoon.create_text(55,40,fill='black',font='Courier 96',text="◔",angle=135)
elif 13.765294 < lunar_day <= 15.765294:
    moon_phase = "Full Moon"
    CanvasMoon.create_text(45,50,fill='black',font='Courier 96',text="○")
elif 15.765294 < lunar_day <= 21.147941:
    moon_phase = "Waning Gibbous"
    CanvasMoon.create_text(55,40,fill='black',font='Courier 96',text="◔",angle=315)
elif 21.147941 < lunar_day <= 23.147941:
    moon_phase = "Last Quarter"
    CanvasMoon.create_text(45,50,fill='black',font='Courier 96',text="◑")
elif 23.147941 < lunar_day <= 28.530588:
    moon_phase = "Waning Crescent"
    CanvasMoon.create_text(50,55,fill='black',font='Courier 96',text="☾")
else:
    moon_phase = "New Moon"
    CanvasMoon.create_text(45,50,fill='black',font='Courier 96',text="●")

#moon phase label
MoonPhaseCanvas = Canvas(root,width=200,height=24,bg='#F1E9D2')
MoonPhaseCanvas.place(x=10,y=354)
time_now=datetime.now()
MoonPhaseCanvas.create_text(100,14,fill='black',font='Courier 16',text=moon_phase)

#circle for clock
def create_circle(x, y, r, canvas): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1)

def create_analog():   #this actually updates both clocks and the am/pm sign
    myCanvas.delete("all")  #clears the previous
    #create clock
    create_circle(150, 150, 140, myCanvas)
    #add numbers 1 to 12
    for num in range(1, 13):
        num_angle = (30 * num) - 90
        num_rad = num_angle * math.pi / 180
        num_distance = 115
        num_x = 150 + num_distance * math.cos(num_rad)
        num_y = 150 + num_distance * math.sin(num_rad)
        myCanvas.create_text(num_x, num_y, text=str(num), font=('Helvetica', 12, 'bold'), fill='black')
    now = datetime.now()
    hour = int(now.hour)
    minu = int(now.minute)
    seco = int(now.second)
    #update AM or PM
    am_pm_label.config(text="AM" if hour < 12 else "PM")
    #second hand
    angle_in_degree=(6*seco)-90
    angle_in_radians=angle_in_degree*math.pi/180
    line_length=130
    center_x=150
    center_y=150
    end_x=center_x+line_length*math.cos(angle_in_radians)
    end_y=center_y+line_length*math.sin(angle_in_radians)
    myCanvas.create_line(150, 150, end_x, end_y,fill='blue',width=1)
    #minute hand
    angle_in_degree=(6*minu)-90
    angle_in_radians=angle_in_degree*math.pi/180
    line_length=130
    center_x=150
    center_y=150
    end_x=center_x+line_length*math.cos(angle_in_radians)
    end_y=center_y+line_length*math.sin(angle_in_radians)
    myCanvas.create_line(150, 150, end_x, end_y,fill='blue',width=2)
    #hour hand
    angle_in_degree=(30*(hour%12)+(minu/2))-90
    angle_in_radians=angle_in_degree*math.pi/180
    line_length=130
    center_x=150
    center_y=150
    end_x=center_x+line_length*math.cos(angle_in_radians)
    end_y=center_y+line_length*math.sin(angle_in_radians)
    myCanvas.create_line(150, 150, end_x, end_y,fill='red',width=3)
    #digital time
    Canvas2.delete("all")
    time_str = now.strftime("%H:%M:%S.%f")[:-2]
    Canvas2.create_text(100,12,fill="black",font="Courier 16",text=time_str)
    root.after(1, create_analog) # 1 millisecond delay
#run
create_analog()
root.mainloop()

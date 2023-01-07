import turtle
import pandas
import openpyxl
import math
#E0E0E0 grey
modulus_of_elasticity = 210 * 1000
pi = 3.142857
#things_used = input("enter the things you will use with a space between each word")
#x = things_used.split(' ')
#-------------------------------------------------------------------------------------------------------------
excel1 = 'inputs.xlsx'
inputt = pandas.read_excel(excel1, engine="openpyxl")
a=inputt['used items']
plate1 = float(inputt['thickness of first plate (mm)'][0])
plate2 = float(inputt['thickness of second plate (mm)'][0])
nominal_dia_of_bolt = float(inputt['diameter of bolt (mm)'][0])
f_max=float((inputt['maximum force on bolt (N)'][0]))
f_res=float((inputt['residual force in joint(N)'][0]))
pitch=float((inputt['pitch of bolt (mm)'][0]))
safety_factor=float((inputt['safety factor'][0]))
x=list(a)
# ---------------------------------------------------------------------------------------------------------------
D_washer=[0,0,10,12,14,18,22,28,30,34,40,40,45,45,52,58,62,68,75,80,85,92]
l_under = [6, 7, 5, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 22, 25, 26, 28, 30, 32, 35, 38, 40, 42, 48, 50]
l_above = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 48, 50, 55, 60, 65, 70, 75,80,85,90,95,100,105,110,115,120]
outer_dia = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 42, 45, 48]
s1 = [0, 0, 0.8, 0.8, 1.5, 2, 2.5, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8]
b = [6, 8, 10, 12, 15, 18, 22, 25, 28, 32, 36, 38, 42, 45, 48, 55, 58, 62, 70, 75, 80, 85]
a = [2.4, 3.6, 4.8, 5.8, 7, 9.5, 11.5, 14, 16, 18, 20, 23, 25, 27, 30, 33, 36, 40, 42, 45, 48, 52]
v = [3, 4, 5, 6, 7, 9, 12, 14, 16, 19, 21, 23, 25, 277, 31, 34, 37, 41, 44, 47, 50, 53]
core_d = [1.44, 2.31, 3.03, 3.89, 4.61, 6.26, 7.92, 9.57, 12.6, 13.2, 14.5, 16.5, 18.5, 19.8, 22.8, 25.1, 28.1, 30.4,
          33.4, 35.8, 38.8, 41.1]
s = [4.5, 6, 8, 9, 11, 14, 17, 22, 22, 27, 32, 32, 36, 36, 41, 46, 50, 55, 60, 65, 70, 75]
grades=['4.6','4.8','5.8','8.8','9.8','10.9','12.9']
# -----------------------------------------------------------------------------------------------------------------
D_washer_=dict(zip(outer_dia,D_washer))
s_ = dict(zip(outer_dia, s))
core_d_ = dict(zip(outer_dia, core_d))
S1 = dict(zip(outer_dia, s1))
B = dict(zip(outer_dia, b))
a_ = dict(zip(outer_dia, a))
v_ = dict(zip(outer_dia, v))
# ----------------------------------------------------------------
#plate1 = int(input("enter thickness of plate 1"))
#plate2 = int(input("enter thickness of plate 2"))
#nominal_dia_of_bolt = int(input("enter bolt diameter"))
#f_max=int(input("enter the maximum load on the bolt"))
#f_res=int(input("enter the residual force in the joint"))
#pitch=float(input("enter the pitch of the bolt"))
#safety_factor=int(input("enter safety factor"))
#-----------------------------------------------------------------------------
dm_bolt=((nominal_dia_of_bolt+core_d_[nominal_dia_of_bolt])/2)
tan_alpha=float((pitch/(pi*dm_bolt)))
print(tan_alpha)
# ----------------------------------------------------------------------------
if (('washer' in x) and ("gasket" not in x)):
    lenght_of_bolt = plate1 + plate2 + S1[nominal_dia_of_bolt] + v_[nominal_dia_of_bolt]
    # print(f"{lenght_of_bolt}")
    # print(1)
# ---------------------------------------------------------------------------------
if ('gasket' in x) and ('washer' in x):
    thick_gasket = float((inputt['gasket thickness (mm)'][0]))
    lenght_of_bolt = plate1 + plate2 + S1[nominal_dia_of_bolt] + v_[nominal_dia_of_bolt] + thick_gasket
# ---------------------------------------------------------------------------------
if nominal_dia_of_bolt > 6:
    lens = l_above
else:
    lens = l_under
counter = 0
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
while (1):
    if lenght_of_bolt in lens:
        print(f"lenght of bolt is {lenght_of_bolt}")
    else:
        lenght_of_bolt = lenght_of_bolt + 1
        counter = counter + 1
    if lenght_of_bolt in lens:
        break
print(f'\nthe lenght of the bolt is {lenght_of_bolt}')
# ----------------------------------------------------------------------------------------------------------------------------
print("now we calculate the bolt stifness")
v_new = v_[nominal_dia_of_bolt] + counter
bolt_stifness = 1 / (((lenght_of_bolt - B[nominal_dia_of_bolt]) / (
            modulus_of_elasticity * ((pi / 4) * nominal_dia_of_bolt ** 2))) + ((B[nominal_dia_of_bolt] - v_new) / (
            modulus_of_elasticity * ((pi / 4) * core_d_[nominal_dia_of_bolt] ** 2))))
#bolt_stifness=703000
print(f'the bolt stifness is {bolt_stifness}')
# -------------------------------------------------------------------------------------------------------------------------------
if (('washer' in x) and ("gasket" not in x)):
    if (s_[nominal_dia_of_bolt] + 2 * S1[nominal_dia_of_bolt]) < (s_[nominal_dia_of_bolt] + 2 * plate1):
        new_dia = s_[nominal_dia_of_bolt] + 2 * S1[nominal_dia_of_bolt]
        if (new_dia + 2 * plate2) < (s_[nominal_dia_of_bolt] + 2 * plate1):
            new_dia1 = new_dia + 2 * plate2
            condd=True
        else:
            new_dia1 = s_[nominal_dia_of_bolt] + 2 * plate1
            condd=False
# -------------------------------------------------------------------------------------------------------------------------------
if (('washer' in x) and ("gasket" not in x)):
    print("now joint stifness")
    dm_1 = (s_[nominal_dia_of_bolt] + new_dia1) / 2
    dm_2 = (new_dia + new_dia1) / 2
    dm_3 = (new_dia + s_[nominal_dia_of_bolt]) / 2
    area1 = (pi / 4) * ((dm_1 ** 2) - (a_[nominal_dia_of_bolt] ** 2))
    area2 = (pi / 4) * ((dm_2 ** 2) - (a_[nominal_dia_of_bolt] ** 2))
    area3 = (pi / 4) * ((dm_3 ** 2) - (a_[nominal_dia_of_bolt] ** 2))
    j_s1 = (modulus_of_elasticity * area1 / plate1)
    j_s2 = (modulus_of_elasticity * area2 / plate2)
    j_s3 = (modulus_of_elasticity * area3 / S1[nominal_dia_of_bolt])
    joint_stifness = 1 / ((1 / j_s1) + (1 / j_s2) + (1 / j_s3))
    print(f"the joint stifness is {joint_stifness}")

# ---------------------------------------------------------------------------------------------------------
if ('gasket' in x) and ('washer' in x):
    if (s_[nominal_dia_of_bolt] + 2 * S1[nominal_dia_of_bolt]) < (s_[nominal_dia_of_bolt] + 2 * plate1):
        new_dia = s_[nominal_dia_of_bolt] + 2 * S1[nominal_dia_of_bolt]
        cond = True
    else:
        new_dia3 = s_[nominal_dia_of_bolt] + 2 * plate1
        cond = False
    if ((cond == True) and (new_dia + 2 * plate2 < s_[nominal_dia_of_bolt] + 2 * plate1)):
        new_dia2 = new_dia + 2 * plate2
        new_dia3 = new_dia2
        pla = True
    elif ((cond == True) and (new_dia + 2 * plate2 > s_[nominal_dia_of_bolt] + 2 * plate1)):
        new_dia3 = s_[nominal_dia_of_bolt] + 2 * plate1
        new_dia2 = new_dia3
        pla = False
    if ((cond == False)):
        # new_dia3=s_[nominal_dia_of_bolt]+2*plate1
        new_dia2 = new_dia3
    dm1 = ((new_dia3) + s_[nominal_dia_of_bolt]) / 2
    dm2 = new_dia2
    dm3 = (new_dia2 + new_dia) / 2
    dm4 = (new_dia + s_[nominal_dia_of_bolt]) / 2
    area1 = (pi / 4) * ((dm1 ** 2) - (a_[nominal_dia_of_bolt] ** 2))
    area2 = (pi / 4) * ((dm2 ** 2) - (a_[nominal_dia_of_bolt] ** 2))
    area3 = (pi / 4) * ((dm3 ** 2) - (a_[nominal_dia_of_bolt] ** 2))
    area4 = (pi / 4) * ((dm4 ** 2) - (a_[nominal_dia_of_bolt] ** 2))
    j_s1 = (modulus_of_elasticity * area1 / plate1)
    j_s2 = (modulus_of_elasticity * area2 / thick_gasket)
    j_s3 = (modulus_of_elasticity * area3 / plate2)
    j_s4 = (modulus_of_elasticity * area4 / S1[nominal_dia_of_bolt])
    joint_stifness = 1 / ((1 / j_s1) + (1 / j_s4) + (1 / j_s3) + (1 / j_s2))
    print(f"the joint stifness is {joint_stifness}")

# ----------------------------------------------------------------------------------------------------------------------------------
f_initial=((bolt_stifness*f_res)+(f_max*joint_stifness))/(joint_stifness+bolt_stifness)
torque_one=f_initial*(dm_bolt/2)*((tan_alpha+0.230)/(1-(tan_alpha*0.230)))
print(torque_one)
segma_assembly=f_initial/((pi/4)*((core_d_[nominal_dia_of_bolt])**2))
print(segma_assembly)
shear_ass=(16*torque_one)/(pi*((core_d_[nominal_dia_of_bolt])**3))
print(shear_ass)
segma_working=f_max/((pi/4)*((core_d_[nominal_dia_of_bolt])**2))
print(segma_working)
assembly_stress=(((segma_assembly/2)**2)+((shear_ass)**2))**0.5
working_stress=((segma_working/2)**2)**0.5
#--------------------------------------------------------------------------------------------------------------------------------------
if assembly_stress>working_stress:
    ss=assembly_stress
    for grade in grades:
        e=grade.split('.')
        yieldd=(int(e[0]))*(int(e[1]))*10
        if yieldd<assembly_stress*2*safety_factor:
            continue
        else:
            print(f"segma yield should be grater than {2*safety_factor*assembly_stress}")
            gradee=grade
            break
else:
    ss=working_stress
    for grade in grades:
        e=grade.split('.')
        yieldd=(int(e[0]))*(int(e[1]))*10
        if yieldd<working_stress*2*safety_factor:
            continue
        else:
            gradee=grade
            print(f"segma yield should be grater than  {2*safety_factor*working_stress}")
            break
print(f"the grade selected is")
print(gradee)
#--------------------------------------------------------------------------------------------------------------------
#output={'bolt_stifness':[bolt_stifness],'joint_stifness':[joint_stifness],'f_initial':[f_initial],'maximum force':[f_max],'bolt lenght':[lenght_of_bolt],'maximum shear stress':[ss],'min yield strength':[(ss*2*safety_factor)],'the selected grade':[gradee]}
wb=openpyxl.load_workbook("F:\\pycharm projects\\project5\\inputs.xlsx")
sh=wb['Sheet1']

# sh['A7'].value = 'bolt_stiffness (N/mm)'
# sh['B7'].value = 'joint_stiffness (N/mm)'
# sh['C7'].value = 'f_initial (N)'
# sh['D7'].value = 'maximum force (N)'
# sh['E7'].value = 'bolt length (mm)'
# sh['F7'].value = 'max shear stress'
# sh['G7'].value = 'min yield stress(N)'
# sh['H7'].value = 'the selected grade'
#---------
sh['A8'].value = bolt_stifness
sh['B8'].value = joint_stifness
sh['C8'].value = f_initial
sh['D8'].value = f_max
sh['E8'].value = lenght_of_bolt
sh['F8'].value = ss
sh['G8'].value = (ss*2*safety_factor)
sh['H8'].value = gradee
wb.save('out4.xlsx')
#data=pandas.DataFrame.from_dict(output)

#open('out3.xlsx')
#data.to_excel('out3.xlsx')

#-------------------------------------------------------------------------------
if 'gasket'not in x :
    tut2 = turtle.Turtle()
    tut5=turtle.Turtle()
    tut4=turtle.Turtle()
    tut2.hideturtle()
    tut5.hideturtle()
    tut4.hideturtle()
    tut2.speed(3)
    tut5.speed(3)
    tut4.speed(3)
    wn = turtle.Screen()
    tut2.goto(D_washer_[nominal_dia_of_bolt]*2,4*0)
    tut5.goto(D_washer_[nominal_dia_of_bolt]*2,4*0)
    tut2.goto(D_washer_[nominal_dia_of_bolt]*2,4*S1[nominal_dia_of_bolt])
    tut5.goto(D_washer_[nominal_dia_of_bolt]*2,S1[nominal_dia_of_bolt]*4 )
    tut5.goto((270), S1[nominal_dia_of_bolt] * 4)
    tut5.goto(270, (plate2+S1[nominal_dia_of_bolt])* 4)
    tut5.goto(-270, (plate2 + S1[nominal_dia_of_bolt]) * 4)
    tut5.goto(-270, 4*S1[nominal_dia_of_bolt])
    tut5.goto(0,S1[nominal_dia_of_bolt]*4)
    tut4.penup()
    tut4.goto(270,(S1[nominal_dia_of_bolt]+plate2)*4)
    tut4.pendown()
    tut4.goto(270,(S1[nominal_dia_of_bolt]+plate1+plate2)*4)
    tut4.goto(-270,(S1[nominal_dia_of_bolt]+plate1+plate2)*4)
    tut4.goto(-270,(S1[nominal_dia_of_bolt]+plate2)*4)
    #tut4.pencolor('white')
    #tut4.penup()
    #tut4.goto(-a_[nominal_dia_of_bolt]*2,(S1[nominal_dia_of_bolt]+plate2)*4)
    #tut4.pendown()
    #tut4.forward(a_[nominal_dia_of_bolt]*4)
    tut2.goto(-1*D_washer_[nominal_dia_of_bolt]*2,4*S1[nominal_dia_of_bolt])
    tut2.goto(-1*D_washer_[nominal_dia_of_bolt]*2,0)
    tut2.goto(a_[nominal_dia_of_bolt]*2,0)
    tut2.goto(-a_[nominal_dia_of_bolt]*2,0)
    tut2.pencolor('black')
    tut2.goto(a_[nominal_dia_of_bolt]*-2,(4*(plate1+plate2+S1[nominal_dia_of_bolt])))
    tut2.forward(a_[nominal_dia_of_bolt]*4)
    tut2.goto(a_[nominal_dia_of_bolt] * 2,0)
    #------------------
    tut2.penup()
    tut4.penup()
    tut5.penup()
    tut12=turtle.Turtle()
    tut8=turtle.Turtle()
    tut8.hideturtle()
    tut12.hideturtle()
    tut12.penup()
    tut8.penup()
    tut8.speed(1)
    tut2.speed(1)
    tut2.goto(s_[nominal_dia_of_bolt]*0.5*4,0)
    tut8.goto(-s_[nominal_dia_of_bolt]*0.5*4,0)
    tut2.pendown()

    tut2.goto(new_dia*2,4*S1[nominal_dia_of_bolt])
    tut2.shape('circle')
    tut2.shapesize(0.2,0.2,0.2)
    tut2.showturtle()
    tut2.stamp()
    tut8.shape('circle')
    tut8.shapesize(0.2,0.2,0.2)
    tut8.showturtle()
    tut8.pendown()
    tut8.goto(-new_dia*2,4*S1[nominal_dia_of_bolt])
    tut8.stamp()
    #---------------------------------------
    if  (condd==False):
        tut5.goto(-s_[nominal_dia_of_bolt]*2,(4*(plate1+plate2+S1[nominal_dia_of_bolt])))
        tut12.goto(s_[nominal_dia_of_bolt]*2,(4*(plate1+plate2+S1[nominal_dia_of_bolt])))
        tut5.speed(1)
        tut5.pendown()

        tut12.speed(1)
        tut12.shape('circle')
        tut5.shape('circle')

        tut5.shapesize(0.2,0.2,0.2)
        tut5.stamp()
        tut12.shapesize(0.2,0.2,0.2)
        tut12.pendown()
        tut12.stamp()
        tut5.goto((-new_dia1*2),(S1[nominal_dia_of_bolt]+plate2)*4)
        tut5.stamp()
        tut12.goto((new_dia1 * 2), (S1[nominal_dia_of_bolt] + plate2) * 4)
        tut12.stamp()
        tut5.goto(-new_dia*2,4*S1[nominal_dia_of_bolt])
        tut5.stamp()
        tut12.goto(new_dia*2,4*S1[nominal_dia_of_bolt])
        tut12.stamp()
    else:

        tut2.goto(new_dia1*2,4*(S1[nominal_dia_of_bolt]+plate2))
        tut2.stamp()
        tut8.goto(new_dia1*-2,4*(S1[nominal_dia_of_bolt]+plate2))
        tut8.stamp()
        tut2.goto(s_[nominal_dia_of_bolt]*0.5*4,(4*(plate1+plate2+S1[nominal_dia_of_bolt])))
        tut8.goto(s_[nominal_dia_of_bolt]*-0.5*4,(4*(plate1+plate2+S1[nominal_dia_of_bolt])))
        #---------------
    tut1=turtle.Turtle()
    tut3=turtle.Turtle()
    tut6=turtle.Turtle()
    tut7=turtle.Turtle()
    tut7.pencolor('red')
    tut1.shapesize(0.5)
    tut3.shapesize(0.5)
    tut6.shapesize(0.5)
    tut7.shapesize(0.5)
    tut1.speed(10)
    tut3.speed(10)
    tut6.speed(10)
    tut7.speed(10)
    tut1.penup()
    tut3.penup()
    tut6.penup()
    tut7.penup()
    tut1.shapetransform()
    tut3.shapetransform()
    tut6.shapetransform()
    tut7.shapetransform()
    tut1.goto(270,(S1[nominal_dia_of_bolt])*4)
    tut3.goto(270,(S1[nominal_dia_of_bolt]+plate2)*4)
    tut7.goto(270, (S1[nominal_dia_of_bolt]+plate2) * 4)
    tut6.goto(270, (S1[nominal_dia_of_bolt]+plate1+plate2) * 4)
    tut7.tilt(270)
    tut3.tilt(90)
    tut7.pendown()
    tut12.pencolor('red')
    tut7.forward(30)
    tut6.pendown()
    tut6.pencolor('red')
    tut6.forward(40)
    tut6.tilt(270)
    tut7.stamp()
    tut6.stamp()
    tut1.pendown()
    tut1.pencolor('red')
    tut1.tilt(90)
    tut1.forward(30)
    tut1.stamp()
    tut3.pencolor('red')
    tut3.pendown()


    tut3.forward(40)
    tut3.stamp()
    tut3.left(90)
    tut3.forward(plate1*2)
    tut3.write(f"{plate1} mm",align='center')
    tut6.hideturtle()
    tut6.right(90)
    tut6.forward(plate1*2-20)
    tut3.hideturtle()
    #-----------------------------
    tut1.tilt(270)
    tut1.left(90)
    tut1.forward(2*plate2)
    tut1.write(f"{plate2} mm",align="center")
    tut7.tilt(270)
    tut7.right(90)

    tut7.forward(2*plate2-20)
    tut7.hideturtle()
    tut1.hideturtle()
    #----------------------------------
    tut1.penup()
    tut3.penup()
    tut1.goto(2*a_[nominal_dia_of_bolt],2*plate2)
    tut3.goto(-2 * a_[nominal_dia_of_bolt], 2 * plate2)
    tut1.left(90)
    tut1.stamp()
    tut3.tilt(270)
    tut3.right(90)
    tut3.stamp()
    #--------------------

    #-------------------
    tut1.pendown()
    tut1.forward(a_[nominal_dia_of_bolt]*2)
    tut1.write(f'{a_[nominal_dia_of_bolt]} mm',align='center')
    tut3.pendown()
    tut3.forward(a_[nominal_dia_of_bolt]*2-10)
    #--------------------------------------
    tut1.penup()
    tut3.penup()
    tut1.goto(new_dia1*2,(plate2+S1[nominal_dia_of_bolt])*4)
    tut3.goto(new_dia1 * -2, (plate2 + S1[nominal_dia_of_bolt]) * 4)
    tut1.pendown()
    tut3.pendown()
    tut1.goto(new_dia1 * 2,-50)
    tut3.goto(new_dia1 * -2,-50)
    tut1.stamp()
    tut3.stamp()

    tut1.forward(2*new_dia1)
    tut1.write(f'{new_dia1} mm',align='center')
    tut3.forward(2*new_dia1)
    #-----------------
    tut1.penup()
    tut3.penup()
    tut1.goto(new_dia * 2, (S1[nominal_dia_of_bolt]) * 4)
    tut3.goto(new_dia * -2, (S1[nominal_dia_of_bolt]) * 4)
    tut1.pendown()
    tut3.pendown()
    tut1.goto(new_dia* 2, -30)
    tut3.goto(new_dia* -2, -30)
    tut1.stamp()
    tut3.stamp()

    tut1.forward(2 * new_dia)
    tut1.write(f'{new_dia}mm', align='center')
    tut3.forward(2 * new_dia)
    #-------------------
    tut1.penup()
    tut3.penup()
    tut1.goto(s_[nominal_dia_of_bolt] * 2, (plate2 +plate1+ S1[nominal_dia_of_bolt]) * 4)
    tut3.goto(s_[nominal_dia_of_bolt]  * -2, (plate2 + plate1+S1[nominal_dia_of_bolt]) * 4)
    tut1.pendown()
    tut3.pendown()
    tut1.goto(s_[nominal_dia_of_bolt]  * 2, (plate2 +plate1+ S1[nominal_dia_of_bolt]+4) * 4)
    tut3.goto(s_[nominal_dia_of_bolt]  * -2, (plate2 +plate1+ S1[nominal_dia_of_bolt]+4) * 4)
    tut1.stamp()
    tut3.stamp()

    tut1.forward(2 * s_[nominal_dia_of_bolt] )
    tut1.write(f'{s_[nominal_dia_of_bolt] } mm', align='center')
    tut3.forward(2 * s_[nominal_dia_of_bolt] )
    #-------------------------
    tut1.penup()
    tut2.pensize(5)
    tut1.goto(0,-230)
    tut1.write(f"the grade of the bolt is {gradee}",align='center',font=('Arial', 15, 'normal'))
    #tut1.goto(0, -130)
    #tut1.write(f'the bolt stifness = {bolt_stifness} (N/mm)',align='center',font=('Arial', 15, 'normal'))
    #tut1.goto(0, -110)
    #tut1.write(f'the joint stifness = {joint_stifness} (N/mm)',align='center',font=('Arial', 15, 'normal'))
    #ut1.goto(0,-90)
    #tut1.write(f'the pre load = {f_initial} (N)',align='center',font=('Arial', 15, 'normal'))
    #tut1.goto(0,-150)
    #tut1.write(f'f_ maximum ={f_max} (N)',align='center',font=('Arial', 15, 'normal'))
    #tut1.goto(0,-170)
    #tut1.write(f'length of bolt ={lenght_of_bolt} (mm)',align='center',font=('Arial', 15, 'normal'))
    #tut1.goto(0,-190)
    #tut1.write(f'maximum shear stress ={ss}(MPA)',align='center',font=('Arial', 15, 'normal'))
    tut1.goto(0,-210)
    tut1.write(f'the minimum yield strength ={(ss * 2 * safety_factor)} (MPA)',align='center',font=('Arial', 15, 'normal'))


    wn.exitonclick()
#-------------------------------------------------------------------------------------------------------------------------------
if 'gasket' in x :
    wn = turtle.Screen()
    tut9=turtle.Turtle()
    tut8=turtle.Turtle()
    tut11=turtle.Turtle()
    tut12=turtle.Turtle()
    tut11.shapesize(0.2,0.2,0.2)
    tut12.shapesize(0.2,0.2,0.2)
    tut9.shapesize(0.2,0.2,0.2)
    tut8.shapesize(0.2,0.2,0.2)
    tut9.shape('circle')
    tut8.shape('circle')
    tut11.shape('circle')
    tut12.shape('circle')

    #------------------------------
    tut9.goto(D_washer_[nominal_dia_of_bolt] * 2, 4 * 0)
    tut9.goto(D_washer_[nominal_dia_of_bolt] * 2, 4 * S1[nominal_dia_of_bolt])
    tut9.goto(-1*D_washer_[nominal_dia_of_bolt] * 2, 4 * S1[nominal_dia_of_bolt])
    tut9.goto(-1 * D_washer_[nominal_dia_of_bolt]*2 , 0)
    tut9.goto(0,0)
    #--------------------------------------
    tut11.penup()
    tut11.goto(-1*D_washer_[nominal_dia_of_bolt] * 2, 4 * S1[nominal_dia_of_bolt])
    tut11.pendown()
    tut11.goto(-270, 4 * S1[nominal_dia_of_bolt])
    tut11.goto(-270,4*(plate2+S1[nominal_dia_of_bolt]))
    tut11.goto(270,4*(plate2+S1[nominal_dia_of_bolt]))
    tut11.goto(270,4*S1[nominal_dia_of_bolt])
    tut11.goto(D_washer_[nominal_dia_of_bolt]*2,4*S1[nominal_dia_of_bolt])
    tut11.hideturtle()
    #---------------------------
    tut9.penup()
    if pla==True:
        f = 2 * (s_[nominal_dia_of_bolt] + 5 + 2 * plate1)
        tut9.goto(f,4*(plate2+S1[nominal_dia_of_bolt]))

    else:
        f=2* (s_[nominal_dia_of_bolt] + 5 + 2 * plate1)
        tut9.goto(f, 4 * (plate2 + S1[nominal_dia_of_bolt]))

    tut9.pendown()
    tut9.goto(f,4*(plate2+S1[nominal_dia_of_bolt]+thick_gasket))
    tut9.goto(-1*f,4*(plate2+S1[nominal_dia_of_bolt]+thick_gasket))
    tut9.goto(-1*f,4*(plate2+S1[nominal_dia_of_bolt]))
    #---------------------------gasket drawing
    tut9.goto(-1*f,4*(plate2+S1[nominal_dia_of_bolt]+thick_gasket))
    tut9.goto(-270,4*(plate2+S1[nominal_dia_of_bolt]+thick_gasket))
    tut9.goto(-270,4*(plate2+plate1+S1[nominal_dia_of_bolt]+thick_gasket))
    tut9.goto(270,4*(plate2+plate1+S1[nominal_dia_of_bolt]+thick_gasket))
    tut9.goto(270,4*(plate2+S1[nominal_dia_of_bolt]+thick_gasket))
    tut9.goto(f, 4 * (plate2 + S1[nominal_dia_of_bolt] + thick_gasket))
    tut9.hideturtle()
    #------------------------------------------
    tut8.speed(1)
    tut8.goto(a_[nominal_dia_of_bolt] * 2, 0)
    tut8.goto(a_[nominal_dia_of_bolt]*2,4*(plate2+plate1+S1[nominal_dia_of_bolt]+thick_gasket))
    tut8.goto(-1*a_[nominal_dia_of_bolt]*2,4*(plate2+plate1+S1[nominal_dia_of_bolt]+thick_gasket))
    tut8.goto(-1 * a_[nominal_dia_of_bolt] * 2, 0)
    #--------------------------------
    tut12.speed(1)
    tut12.goto(s_[nominal_dia_of_bolt] * 2, 0)
    tut8.goto(s_[nominal_dia_of_bolt] * -2, 0)
    tut12.goto(new_dia*2,S1[nominal_dia_of_bolt]*4)
    tut12.stamp()
    tut8.goto(new_dia*-2,S1[nominal_dia_of_bolt]*4)
    tut8.stamp()
    #------------
    if (pla==False):
        tut12.penup()
        tut12.goto(s_[nominal_dia_of_bolt] * 2,4*(plate1+plate2+thick_gasket+S1[nominal_dia_of_bolt]))
        tut12.stamp()
        tut8.penup()
        tut8.goto(-1*s_[nominal_dia_of_bolt] * 2,4*(plate1+plate2+thick_gasket+S1[nominal_dia_of_bolt]))
        tut8.stamp()
        tut12.pendown()
        tut8.pendown()
        tut12.goto(new_dia3*2,4*(plate2+thick_gasket+S1[nominal_dia_of_bolt]))
        tut12.stamp()
        tut8.goto(-1*new_dia3*2,4*(plate2+thick_gasket+S1[nominal_dia_of_bolt]))
        tut8.stamp()
        tut12.goto(1*new_dia3*2,4*(plate2+S1[nominal_dia_of_bolt]))
        tut12.stamp()
        tut8.goto(-1 * new_dia3 * 2, 4 * (plate2+S1[nominal_dia_of_bolt]))
        tut8.stamp()
        tut8.goto(new_dia * -2, S1[nominal_dia_of_bolt] * 4)
        tut8.stamp()
        tut12.goto(new_dia * 2, S1[nominal_dia_of_bolt] * 4)
        tut12.stamp()
    else :
        tut12.goto(new_dia2*2,4*(plate2+S1[nominal_dia_of_bolt]))
        tut12.stamp()
        tut8.goto(-1*new_dia2 * 2, 4 * (plate2 + S1[nominal_dia_of_bolt]))
        tut8.stamp()
        tut12.goto(new_dia2 * 2, 4 * (plate2 +thick_gasket+ S1[nominal_dia_of_bolt]))
        tut12.stamp()
        tut8.goto(-1*new_dia2 * 2, 4 * (plate2 +thick_gasket+ S1[nominal_dia_of_bolt]))
        tut8.stamp()
        tut12.goto(s_[nominal_dia_of_bolt] * 2, 4 * (plate2 +plate1+thick_gasket+ S1[nominal_dia_of_bolt]))
        tut12.stamp()
        tut8.goto(-1*s_[nominal_dia_of_bolt] * 2, 4 * (plate2 +plate1+thick_gasket+ S1[nominal_dia_of_bolt]))
        tut8.stamp()
    #-------------------------------------
    tut1 = turtle.Turtle()
    tut3 = turtle.Turtle()
    tut6 = turtle.Turtle()
    tut7 = turtle.Turtle()
    tut7.pencolor('red')
    tut1.shapesize(0.5)
    tut3.shapesize(0.5)
    tut6.shapesize(0.5)
    tut7.shapesize(0.5)
    tut1.speed(10)
    tut3.speed(10)
    tut6.speed(10)
    tut7.speed(10)
    tut1.penup()
    tut3.penup()
    tut6.penup()
    tut7.penup()
    tut1.shapetransform()
    tut3.shapetransform()
    tut6.shapetransform()
    tut7.shapetransform()
    tut1.goto(270, (S1[nominal_dia_of_bolt]) * 4)
    tut3.goto(270, (S1[nominal_dia_of_bolt] + plate2+thick_gasket) * 4)
    tut7.goto(270, (S1[nominal_dia_of_bolt] + plate2) * 4)
    tut6.goto(270, (S1[nominal_dia_of_bolt] + plate1 + plate2+thick_gasket) * 4)
    tut7.tilt(270)
    tut3.tilt(90)
    tut7.pendown()
    tut12.pencolor('red')
    tut7.forward(30)
    tut6.pendown()
    tut6.pencolor('red')
    tut6.forward(40)
    tut6.tilt(270)
    tut7.stamp()
    tut6.stamp()
    tut1.pendown()
    tut1.pencolor('red')
    tut1.tilt(90)
    tut1.forward(30)
    tut1.stamp()
    tut3.pencolor('red')
    tut3.pendown()

    tut3.forward(40)
    tut3.stamp()
    tut3.left(90)
    tut3.forward(plate1 * 2)
    tut3.write(f"{plate1} mm", align='center')
    tut6.hideturtle()
    tut6.right(90)
    tut6.forward(plate1 * 2 - 20)
    tut3.hideturtle()
    # -----------------------------
    tut1.tilt(270)
    tut1.left(90)
    tut1.forward(2 * plate2)
    tut1.write(f"{plate2} mm", align="center")
    tut7.tilt(270)
    tut7.right(90)

    tut7.forward(2 * plate2 - 20)
    tut7.hideturtle()
    tut1.hideturtle()
    # ----------------------------------
    tut1.penup()
    tut3.penup()
    tut1.goto(2 * a_[nominal_dia_of_bolt], 2 * plate2)
    tut3.goto(-2 * a_[nominal_dia_of_bolt], 2 * plate2)
    tut1.left(90)
    tut1.stamp()
    tut3.tilt(270)
    tut3.right(90)
    tut3.stamp()
    # --------------------

    # -------------------
    tut1.pendown()
    tut1.forward(a_[nominal_dia_of_bolt] * 2)
    tut1.write(f'{a_[nominal_dia_of_bolt]} mm', align='center')
    tut3.pendown()
    tut3.forward(a_[nominal_dia_of_bolt] * 2 - 10)
    # --------------------------------------
    tut1.penup()
    tut3.penup()
    tut1.goto(new_dia2 * 2, (plate2 + S1[nominal_dia_of_bolt]) * 4)
    tut3.goto(new_dia2 * -2, (plate2 + S1[nominal_dia_of_bolt]) * 4)
    tut1.pendown()
    tut3.pendown()
    tut1.goto(new_dia2 * 2, -50)
    tut3.goto(new_dia2 * -2, -50)
    tut1.stamp()
    tut3.stamp()

    tut1.forward(2 * new_dia2)
    tut1.write(f'{new_dia2} mm', align='center')
    tut3.forward(2 * new_dia2)
    # -----------------
    tut1.penup()
    tut3.penup()
    tut1.goto(new_dia * 2, (S1[nominal_dia_of_bolt]) * 4)
    tut3.goto(new_dia * -2, (S1[nominal_dia_of_bolt]) * 4)
    tut1.pendown()
    tut3.pendown()
    tut1.goto(new_dia * 2, -30)
    tut3.goto(new_dia * -2, -30)
    tut1.stamp()
    tut3.stamp()

    tut1.forward(2 * new_dia)
    tut1.write(f'{new_dia}mm', align='center')
    tut3.forward(2 * new_dia)
    # -------------------
    tut1.penup()
    tut3.penup()
    tut1.goto(s_[nominal_dia_of_bolt] * 2, (plate2 + plate1 +thick_gasket+ S1[nominal_dia_of_bolt]) * 4)
    tut3.goto(s_[nominal_dia_of_bolt] * -2, (plate2 + plate1+thick_gasket + S1[nominal_dia_of_bolt]) * 4)
    tut1.pendown()
    tut3.pendown()
    tut1.goto(s_[nominal_dia_of_bolt] * 2, (plate2 + plate1 + thick_gasket+S1[nominal_dia_of_bolt] + 4) * 4)
    tut3.goto(s_[nominal_dia_of_bolt] * -2, (plate2 + plate1 +thick_gasket+ S1[nominal_dia_of_bolt] + 4) * 4)
    tut1.stamp()
    tut3.stamp()

    tut1.forward(2 * s_[nominal_dia_of_bolt])
    tut1.write(f'{s_[nominal_dia_of_bolt]} mm', align='center')
    tut3.forward(2 * s_[nominal_dia_of_bolt])
    # -------------------------
    tut1.penup()

    tut1.goto(0, -230)
    tut1.write(f"the grade of the bolt is {gradee}", align='center', font=('Arial', 15, 'normal'))
    # tut1.goto(0, -130)
    # tut1.write(f'the bolt stifness = {bolt_stifness} (N/mm)',align='center',font=('Arial', 15, 'normal'))
    # tut1.goto(0, -110)
    # tut1.write(f'the joint stifness = {joint_stifness} (N/mm)',align='center',font=('Arial', 15, 'normal'))
    # ut1.goto(0,-90)
    # tut1.write(f'the pre load = {f_initial} (N)',align='center',font=('Arial', 15, 'normal'))
    # tut1.goto(0,-150)
    # tut1.write(f'f_ maximum ={f_max} (N)',align='center',font=('Arial', 15, 'normal'))
    # tut1.goto(0,-170)
    # tut1.write(f'length of bolt ={lenght_of_bolt} (mm)',align='center',font=('Arial', 15, 'normal'))
    # tut1.goto(0,-190)
    # tut1.write(f'maximum shear stress ={ss}(MPA)',align='center',font=('Arial', 15, 'normal'))
    tut1.goto(0, -210)
    tut1.write(f'the minimum yield strength ={(ss * 2 * safety_factor)} (MPA)', align='center',
               font=('Arial', 15, 'normal'))


    #--------------------------------------------------
    wn.exitonclick()


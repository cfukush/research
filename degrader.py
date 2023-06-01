
#---------------------------------------#
#This program displays the actuator's   #
#     position and the number of pulses.#
#                                       #
#    Made by cfukush 2023.Feb.25        #
#---------------------------------------#


xmin = 0
xmax = 250
ymin = 1.0
ymax = 16.0
dpulse = 0.00750016
pulse0_ini = 3109
pulse1_ini = 3269
posi0_ini = 23.318
posi1_ini = 24.518
beam_range = 40
halfbeam_range = beam_range/2

y_aida = ymax - ymin
dydx = y_aida/xmax

deg_change_thick = ymin + ymax
degmin_beamrange = beam_range*((ymax-ymin)/xmax) + ymin + ymin
degmax_beamrange = ymax + ymax -beam_range*((ymax-ymin)/xmax)   

print("Enter the thickness of degrader.")
thick = float(input())
if (thick >= degmin_beamrange) and (thick <= deg_change_thick):
    dthick = thick - (ymin + ymin)
    x_value = dthick / dydx + posi0_ini - halfbeam_range
    pulse = x_value / dpulse
    pulse_min = (posi1_ini + halfbeam_range)/dpulse
    print("Axis number 0")
    print("position: ", '{:.3f}'.format(-x_value), "mm")
    print("pulse   : ", '{:.3f}'.format(-pulse))
    print("Axis number 1")
    print("position: ", '{:.3f}'.format(-posi1_ini + halfbeam_range), "mm")
    print("pulse   : ", '{:.3f}'.format(-pulse_min))


elif (thick >deg_change_thick) and (thick <= degmax_beamrange):
    dthick = (thick - deg_change_thick) #+ 4.4 - (ymin + ymin)
    x_value = dthick / dydx + posi1_ini + halfbeam_range
    x_value_max = ((deg_change_thick - (ymin + ymin))/dydx + posi0_ini - halfbeam_range)
    pulse_max = ((deg_change_thick - (ymin + ymin))/dydx + posi0_ini - halfbeam_range) / dpulse
    pulse = x_value / dpulse 
    print("Axis number 0")
    print("position: ", '{:.3f}'.format(-x_value_max), "mm")
    print("pulse   : ", '{:.3f}'.format(-pulse_max))
    print("Axis number 1")
    print("position: ", '{:.3f}'.format(-x_value), "mm")
    print("pulse   : ", '{:.3f}'.format(-pulse))
else:
    print("\aWARNING! out of range.(", degmin_beamrange,"mm <= thickness <= ",degmax_beamrange, "mm)")

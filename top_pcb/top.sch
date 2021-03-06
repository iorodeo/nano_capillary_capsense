EESchema Schematic File Version 2  date Wed 25 May 2011 01:33:27 PM PDT
LIBS:power,./top,device,transistors,conn,linear,regul,74xx,cmos4000,adc-dac,memory,xilinx,special,microcontrollers,dsp,microchip,analog_switches,motorola,texas,intel,audio,interface,digital-audio,philips,display,cypress,siliconi,opto,atmel,contrib,valves,./top.cache
EELAYER 24  0
EELAYER END
$Descr A4 11700 8267
Sheet 1 1
Title ""
Date "20 may 2011"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	3200 1300 3200 3100
Wire Wire Line
	4450 1650 4450 1850
Connection ~ 1950 2750
Wire Wire Line
	1850 2850 1950 2850
Connection ~ 1950 2450
Wire Wire Line
	1950 2550 1850 2550
Connection ~ 1950 2000
Wire Wire Line
	1950 2350 1850 2350
Connection ~ 1950 1800
Wire Wire Line
	1950 1900 1850 1900
Connection ~ 1950 1500
Wire Wire Line
	1950 1600 1850 1600
Connection ~ 3200 2550
Wire Wire Line
	3200 2750 3300 2750
Connection ~ 3200 2350
Wire Wire Line
	3200 2450 3300 2450
Connection ~ 3200 1900
Wire Wire Line
	3200 2000 3300 2000
Connection ~ 3200 1600
Wire Wire Line
	3200 1800 3300 1800
Wire Wire Line
	3300 1500 1850 1500
Wire Wire Line
	2600 1900 2600 1700
Wire Wire Line
	2600 1700 3300 1700
Wire Wire Line
	3200 1600 3300 1600
Connection ~ 3200 1500
Wire Wire Line
	3200 1900 3300 1900
Connection ~ 3200 1800
Wire Wire Line
	3200 2350 3300 2350
Connection ~ 3200 2000
Wire Wire Line
	3200 2550 3300 2550
Connection ~ 3200 2450
Wire Wire Line
	3200 2850 3300 2850
Connection ~ 3200 2750
Wire Wire Line
	1950 1800 1850 1800
Connection ~ 1950 1600
Wire Wire Line
	1950 2000 1850 2000
Connection ~ 1950 1900
Wire Wire Line
	1950 2450 1850 2450
Connection ~ 1950 2350
Wire Wire Line
	1950 2750 1850 2750
Connection ~ 1950 2550
Connection ~ 3200 2850
Wire Wire Line
	1950 2850 1950 1300
$Comp
L CONN_1 P6
U 1 1 4DD5B3DF
P 3200 1150
F 0 "P6" H 3280 1150 40  0000 L CNN
F 1 "CONN_1" H 3200 1205 30  0001 C CNN
	1    3200 1150
	0    -1   -1   0   
$EndComp
Text Label 4450 1850 0    60   ~ 0
GND
$Comp
L GND #PWR01
U 1 1 4DD571BC
P 4450 1850
F 0 "#PWR01" H 4450 1850 30  0001 C CNN
F 1 "GND" H 4450 1780 30  0001 C CNN
	1    4450 1850
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG02
U 1 1 4DD571AF
P 4450 1650
F 0 "#FLG02" H 4450 1920 30  0001 C CNN
F 1 "PWR_FLAG" H 4450 1880 30  0000 C CNN
	1    4450 1650
	1    0    0    -1  
$EndComp
Text Notes 1700 3450 0    60   ~ 0
CAPILLARY SENSOR TOP PLATE
Text Label 2750 1700 0    60   ~ 0
EXC
Text Label 3200 3100 0    60   ~ 0
GND
$Comp
L GND #PWR03
U 1 1 4DD5710B
P 3200 3100
F 0 "#PWR03" H 3200 3100 30  0001 C CNN
F 1 "GND" H 3200 3030 30  0001 C CNN
	1    3200 3100
	1    0    0    -1  
$EndComp
NoConn ~ 3300 2650
NoConn ~ 1850 2650
NoConn ~ 1850 1700
$Comp
L CAP_PLATE S1
U 1 1 4DD57032
P 2600 3100
F 0 "S1" H 1750 3300 60  0000 C CNN
F 1 "CAP_PLATE" H 2150 2900 60  0000 C CNN
	1    2600 3100
	0    1    1    0   
$EndComp
$Comp
L CONN_1 P3
U 1 1 4DD56FD2
P 1950 1150
F 0 "P3" H 2030 1150 40  0000 L CNN
F 1 "CONN_1" H 1950 1205 30  0001 C CNN
	1    1950 1150
	0    -1   -1   0   
$EndComp
$Comp
L CONN_6 P2
U 1 1 4DD56FCB
P 1500 2600
F 0 "P2" V 1450 2600 60  0000 C CNN
F 1 "CONN_6" V 1550 2600 60  0000 C CNN
	1    1500 2600
	-1   0    0    -1  
$EndComp
$Comp
L CONN_6 P1
U 1 1 4DD56FC8
P 1500 1750
F 0 "P1" V 1450 1750 60  0000 C CNN
F 1 "CONN_6" V 1550 1750 60  0000 C CNN
	1    1500 1750
	-1   0    0    -1  
$EndComp
$Comp
L CONN_6 P5
U 1 1 4DD56FC7
P 3650 2600
F 0 "P5" V 3600 2600 60  0000 C CNN
F 1 "CONN_6" V 3700 2600 60  0000 C CNN
	1    3650 2600
	1    0    0    -1  
$EndComp
$Comp
L CONN_6 P4
U 1 1 4DD56FC4
P 3650 1750
F 0 "P4" V 3600 1750 60  0000 C CNN
F 1 "CONN_6" V 3700 1750 60  0000 C CNN
	1    3650 1750
	1    0    0    -1  
$EndComp
$EndSCHEMATC

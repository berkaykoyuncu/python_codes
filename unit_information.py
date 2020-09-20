# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:49:37 2020

@author: USER
"""


print('WELCOME TO THE -UNIT OF PHYSICAL PROPERTY- by Berkay ')

print('')
print('')

    
print('Which physical property unit would you like to learn?')
print('')
print('Options: density / flow rate / gravitational acceleration / force / temperature / volume / pressure')
answer = input()
print('')
print('')
print('')
print('')
print('')
    
if answer == 'density':
    print ('SI: kg/m3     English Unit: slugs/ft3 or lb/ft3')

if answer == 'force':
    print ('SI: Newton (N) and Dyne (D)      English Unit: pound-force (lbf)')

if answer == 'weight':
    print ('SI: g, kg     English Unit: slugs, pound(lb)')

if answer == 'pressure':
    print ('SI: Pascal (Pa) = N/m2, bar     English Unit: pound per square inch (psi)')

if answer == 'gravitational acceleration':
    print ('SI: m/s2 [Earth Value = 9.80665 m/s2]     English Unit: ft/s2 [Earth Value = 32.17405 ft/s2]')

if answer == 'temperature':
    print ('Kelvin (K), Celsius (C), Fahrenheit (F)')

if answer == 'flow rate':
    print ('SI: cubic meter per second (cms)     English Unit: cubic feet per second (cfs)')

if answer == 'volume':
    print ('SI: cubic meter (m3), litre (L)     English Unit: cubic feet (ft3), ounce (oz), gallon (gal)')
    
        
#    return ('Do you have another question? [Y/N]:')

#def Replay():
#    print ('Do you have another question? [Y/N] ')
#    reply = input()
#    if reply == 'Y':
#        units()
#    elif reply == 'N':
#        exit()
#    else:
#        print('I apologies, I did not catch that. Please repeat.')
#        Replay()



#reply = input()
#    if reply == 'Y':
#        Magic8Ball()
#    elif reply == 'N':
#        exit()
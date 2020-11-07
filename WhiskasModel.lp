\* Whiskas_cat_food_problem *\
Minimize
OBJ: 0.008 beef + 0.013 chicken + 0.001 gel + 0.01 mutton + 0.002 rice
 + 0.005 wheat
Subject To
_C1: beef + chicken + gel + mutton + rice + wheat = 100
_C2: 0.2 beef + 0.1 chicken + 0.15 mutton + 0.04 wheat >= 12
_C3: 0.1 beef + 0.08 chicken + 0.11 mutton + 0.01 rice + 0.01 wheat >= 8
_C4: 0.005 beef + 0.001 chicken + 0.003 mutton + 0.1 rice + 0.15 wheat <= 2
_C5: 0.005 beef + 0.002 chicken + 0.007 mutton + 0.002 rice + 0.008 wheat
 <= 0.4
Bounds
0 <= beef
0 <= chicken
0 <= gel
0 <= mutton
0 <= rice
0 <= wheat
Generals
beef
chicken
gel
mutton
rice
wheat
End

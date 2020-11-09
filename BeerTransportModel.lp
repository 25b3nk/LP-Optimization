\* Beer_transportation_problem *\
Minimize
OBJ: 2 A1 + 4 A2 + 5 A3 + 2 A4 + A5 + 3 B1 + B2 + 3 B3 + 2 B4 + 3 B5
Subject To
_C1: A1 + A2 + A3 + A4 + A5 <= 1000
_C2: B1 + B2 + B3 + B4 + B5 <= 4000
_C3: A1 + B1 >= 500
_C4: A2 + B2 >= 900
_C5: A3 + B3 >= 1800
_C6: A4 + B4 >= 200
_C7: A5 + B5 >= 700
Bounds
0 <= A1
0 <= A2
0 <= A3
0 <= A4
0 <= A5
0 <= B1
0 <= B2
0 <= B3
0 <= B4
0 <= B5
Generals
A1
A2
A3
A4
A5
B1
B2
B3
B4
B5
End

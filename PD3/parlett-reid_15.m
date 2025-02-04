#!/usr/bin/env -S octave -qf

fprintf('Pregunta N°15\n')
A15 = [
    0.0909 0.1111 0.1429 0.2000 0.3333 1.0000;
    0.1111 0.1429 0.2000 0.3333 1.0000 -1.0000;
    0.1429 0.2000 0.3333 1.0000 -1.0000 -0.3333;
    0.2000 0.3333 1.0000 -1.0000 -0.3333 -0.2000;
    0.3333 1.0000 -1.0000 -0.3333 -0.2000 -0.1429;
    1.0000 -1.0000 -0.3333 -0.2000 -0.1429 -0.1111
    ];
[L15, T15, P15] = ParlettReid(A15);
left_15 = P15 * A15 * P15'
right_15 = L15 * T15 * L15'
norm(left_15 - right_15);
P15
L15
T15
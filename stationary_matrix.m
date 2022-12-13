Transition_A = [ 0.85, 0.1, 0.05; 0.25, 0.65, 0.1; 0.25, 0.4, 0.35 ];
Start_S0 = [ 0.7, 0.2, 0.1 ];
k = 13;

for i = 0:(k-1)
    Final_A = Transition_A;
    for j = 1:i
        Final_A = Final_A * Transition_A;
    end
    S_k = Start_S0 * Final_A;
    fprintf(1, 'S_%d: [%s]\n\n', i+1, join(string(S_k), '   '));
end
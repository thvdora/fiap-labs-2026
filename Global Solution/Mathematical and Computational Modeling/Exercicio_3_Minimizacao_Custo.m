% Intervalo do numero de mutiroes por semestre
m = 0:0.1:12;

% Funcao de custo
C = 3 * m.^2 - 36 * m + 150;

% Calculo do custo minimo usando fminbnd
funcao = @(m) 3 * m.^2 - 36 * m + 150;

[mutiroes_minimos, custo_minimo] = fminbnd(funcao, 0, 12);

% Exibicao dos resultados
fprintf('RESULTADOS DO CUSTO MINIMO\n');
fprintf('Numero de mutiroes por semestre: %.2f\n', mutiroes_minimos);
fprintf('Custo minimo: %.2f\n', custo_minimo);

% Criacao do grafico
figure;

plot(m, C, 'b', 'LineWidth', 2);
hold on;

% Destaque do ponto minimo
plot(mutiroes_minimos, custo_minimo, 'ro', ...
     'MarkerSize', 4, 'MarkerFaceColor', 'r');

% Configuracoes do grafico
title('Custo de manutencao por numero de mutiroes no semestre');
xlabel('Numero de mutiroes por semestre');
ylabel('Custo de manutencao');
legend('Funcao C(m)', 'Custo minimo', 'location', 'northeast');
grid on;
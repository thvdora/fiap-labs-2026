% Intervalo de tempo (0 a 52 semanas)
t = 0:0.1:52;

% Funcao das ocorrencias abertas
O = 400 * (1 - exp(-0.1 * t));

% Derivada da funcao
Od = 40 * exp(-0.1 * t);

% Criacao da figura com dois graficos
figure;

% Grafico 1 - Ocorrencias abertas
subplot(2,1,1);

plot(t, O, 'b', 'LineWidth', 2);
hold on;

% Teto de ocorrencias
plot([0 52], [400 400], 'r--', 'LineWidth', 1.5);

xlim([0 52]);
title('Ocorrencias abertas - Vila Aurora');
xlabel('Tempo (semanas)');
ylabel('Ocorrencias abertas');
legend('O(t)', 'Teto de 400 ocorrencias');
grid on;

% Grafico 2 - Derivada das ocorrencias
subplot(2,1,2);

plot(t, Od, 'g', 'LineWidth', 2);

xlim([0 52]);
title('Velocidade de crescimento das ocorrencias');
xlabel('Tempo (semanas)');
ylabel('Variacao por semana');
legend('Derivada de O(t)');
grid on;

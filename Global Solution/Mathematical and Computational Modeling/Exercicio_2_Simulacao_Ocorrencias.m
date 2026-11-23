% Intervalo de 0 a 30 semanas
semanas = 0:30;

% Vetor para armazenar as ocorrencias
abertas = zeros(1, 31);

% Simulacao semanal
for i = 2:31
    abertas(i) = abertas(i-1) * 0.9 + 40;
end

% Modelo continuo
O = 400 * (1 - exp(-0.1 * semanas));

% Comparacao na semana 30
simulacao = abertas(31);
continuo = 400 * (1 - exp(-0.1 * 30));

% Exibicao dos resultados
fprintf('RESULTADOS DA SEMANA 30\n');
fprintf('Simulacao semanal: %.2f ocorrencias\n', simulacao);
fprintf('Modelo continuo: %.2f ocorrencias\n', continuo);
fprintf('Diferenca: %.2f ocorrencias\n', simulacao - continuo);

% Criacao do grafico
figure;

plot(semanas, O, 'b', 'LineWidth', 2);
hold on;

plot(semanas, abertas, 'r-', 'LineWidth', 1.5);

% Configuracoes do grafico
xlim([0 30]);
title('Comparacao das ocorrencias abertas');
xlabel('Tempo (semanas)');
ylabel('Ocorrencias abertas');
legend('Modelo continuo O(t)', 'Simulacao semanal', 'location', 'southeast');
grid on;
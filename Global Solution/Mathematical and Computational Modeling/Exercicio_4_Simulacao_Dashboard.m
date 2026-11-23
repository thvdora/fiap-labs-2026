% Valor inicial de ocorrencias
L = 12;

% Vetores para armazenar os resultados
semanas = 1:24;
valores = zeros(1, 24);

% Simulacao durante 24 semanas
fprintf('SIMULACAO DE OCORRENCIAS\n\n');
fprintf('Semana\tL\tStatus\n');

for semana = 1:24

% Aumento semanal de ocorrencias
L = L + 4;

% Classificacao conforme os limites definidos
if L < 30
status = 'Normal';
elseif L < 50
status = 'Atencao';
else
status = 'Critico';
end

% Armazenamento do valor antes do mutirao
valores(semana) = L;

% Exibicao dos resultados
fprintf('%d\t%d\t%s\n', semana, L, status);

% Mutirao: reinicia as ocorrencias para 12
% somente depois de registrar a semana critica
if L >= 50
L = 12;
end

end

% Criacao do grafico
figure;

plot(semanas, valores, 'b-', 'LineWidth', 2);

% Configuracoes do grafico
title('Simulacao de ocorrencias ao longo de 24 semanas');
xlabel('Semanas');
ylabel('Quantidade de ocorrencias');

xlim([1 24]);
grid on;
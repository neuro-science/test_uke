% % % fid = fopen('/Users/wang/git/hub/honesty_science/data_honesty.txt', 'r');
% % % % [x1, x2] = fscanf(fid, '%d %d %d\n');
% % % x1 = fscanf(fid, '%d %d %d', [3 Inf]);
% % % % ct = 0;
% % % % while 1
% % % % 	tline = fgetl(fid);
% % % % 	if ~ischar(tline)
% % % % 		break;
% % % % 	else
% % % % 		ct = ct + 1;
% % % % 		y(ct) = str2double(tline);
% % % % 	end
% % % % 	disp(tline)
% % % % end
% % % fclose(fid);
% % % 
% % % % x = csvread('/Users/wang/git/hub/honesty_science/data_honesty.csv', 0, 0);
% % % % x = load('/Users/wang/git/hub/honesty_science/data_honesty.txt');
clear all;close all;clc;
fpath = '/Users/wang/git/hub/honesty_science/';
%% 1. data 
x = load(fullfile(fpath, 'data_honesty.txt'));
d = zeros(numel(unique(x(:, 1))), 4, 2);	%[country, n/m, n/d]
for ic = size(x, 1) : -1 : 1
	d(x(ic, 1), x(ic, 2)+1, 1) = d(x(ic, 1), x(ic, 2)+1, 1) + 1;
	d(x(ic, 1), x(ic, 2)+1, 2) = d(x(ic, 1), x(ic, 2)+1, 2) + x(ic, 3);
end
y = d(:, 1:2, 2) ./ d(:, 1:2, 1);
y1 = sum(d(:, 1:2, 2), 2) ./ sum(d(:, 1:2, 1), 2);
z = (y(:, 2) - y(:, 1)) ./ y1(:, 1);
clear x y y1 d ic;
%% 2. IDs
fid = fopen(fullfile(fpath, 'ids.txt'), 'r');
% [x1, x2] = fscanf(fid, '%d %d %d\n');
x = textscan(fid, '%d %s %s\n', [Inf, 1]);
fclose(fid);
for k = numel(x{1}) : -1 : 1
	y{k} = [num2str(x{1}(k), '%02d'), ' ', x{2}{k}, ' ', x{3}{k}];
end
y = unique(y');	
for k = 1 : numel(y)
	y{k} = y{k}(3:end);
end
[x1, x2] = sort(z);
barh(z(x2));
title('Honesty Index By Countries');
set(gca, 'ytick', 1:40, 'yticklabel', y(x2), 'xtick', [-0.4 0 0.4 0.8 1.2], 'fontsize', 16);
export_fig([fpath, 'Honesty.eps']);



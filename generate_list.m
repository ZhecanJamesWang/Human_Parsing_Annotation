clc
clear all;

fileFolder=fullfile('.\data\images');
dirOutput=dir(fullfile(fileFolder));
fileNames={dirOutput.name}';
fid = fopen('C:\Users\Jian\Desktop\js-segment-annotator\list.txt','a+');
for i = 3:length(fileNames)
    name = strcat('"data\images\', fileNames{i, 1}, '",');
    
    fprintf(fid,'\r\n%s', name);   
end
fclose(fid);
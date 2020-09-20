clear; close all; warning off all;
groundtruth = ('F:\New folder (6)\data uji\versi jpg\grtr\STARE');
%groundtruth = ('F:\New folder (6)\data uji\versi jpg\grtr\DRIVE');
%hasilolah = ('F:\New folder (6)\data uji\versi jpg\sauvola jp\STARE');
%hasilolah = ('F:\New folder (6)\data uji\versi jpg\sauvola jp\DRIVE');
hasilolah = ('F:\New folder (6)\data uji\versi jpg\dynam jp\STARE');
%hasilolah = ('F:\New folder (6)\data uji\versi jpg\dynam jp\DRIVE');

fileGT = fullfile(groundtruth, '*.jpg');
filehasilolah = fullfile(hasilolah, '*.jpg'); 
%a=[1,1,1,1];
%b=[1,1,1,1];
myFiles = dir(filehasilolah); % folder testimage
myGTFiles = dir(fileGT); % folder grondtruth

for q = 1 : length(myFiles) 
    rowsl = ceil(sqrt(length(myFiles)));
    fullFileName = fullfile(hasilolah, myFiles(q).name);
    fullFileNameGT = fullfile(groundtruth, myGTFiles(q).name);

    A=imread(fullFileName);
    B=imread(fullFileNameGT);
    
    ground = double(A);
    olah = double(B);

    [M N] = size(ground);
    error = ground - olah;
    MSE = sum(sum(error.^2))./ (M * N);

    if(MSE > 0)
        PSNR = 10*log10(max(max(ground)).^2./MSE);
    else
        PSNR = 99;
    end 
    list_psnr(q,1)=MSE;
    list_psnr(q,2)=PSNR;
    data{q,1}=myFiles(q).name;
    data{q,2}=MSE;
    data{q,3}=PSNR;
end


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
akurasi = 0;
for i = 1 : length(myFiles)
    rowsl = ceil(sqrt(length(myFiles)));
    fullFileName = fullfile(hasilolah, myFiles(i).name);
    fullFileNameGT = fullfile(groundtruth, myGTFiles(i).name);

    a=imread(fullFileName);
    b=imread(fullFileNameGT);

    X = im2bw(a);
    Y = im2bw(b);
    x = size(X,1);
    y = size(Y,1);

    gabungan = X & Y;
    irisan = X | Y;
    jaccardIdx = sum(gabungan(:))/sum(irisan(:));
    persentjaccidx= 100.*jaccardIdx;
    jaccardDist = 1 - jaccardIdx;
    persentjaccdist= 100.*jaccardDist;

    listjaccard(i,1)=persentjaccidx;
    listjaccard(i,2)=persentjaccdist;
    data{i,1}=myFiles(i).name;
    data{i,2}=persentjaccidx;
    data{i,3}=persentjaccdist;
    
    if any(persentjaccdist > 65)
        benar = 1;
    else 
        benar = 0;
    end
        akurasi = akurasi + benar
end
acc = akurasi / length(myFiles)



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

for q = 1 : length(myFiles) 
    rowsl = ceil(sqrt(length(myFiles)));
    fullFileName = fullfile(hasilolah, myFiles(q).name);
    fullFileNameGT = fullfile(groundtruth, myGTFiles(q).name);

    aaa=imread(fullFileName);
    bbb=imread(fullFileNameGT);
    
X=im2bw(aaa);
Y=im2bw(bbb);

[a,b]=size(X);
[c,d]=size(Y);
Xi=Y-X;

Xi(Xi==-1)=1;

im=imcomplement(Xi);

D = bwdist(im);

sum = 0;
    for t = 1 : a,
        for v =1 :b
            sum = sum +  D(t,v);
        end
end
hasil1=sum/100000;
hasil= 1 - hasil1;
akurasi = hasil *100;

    list_euclid(q,1)=hasil1;
    list_euclid(q,2)=hasil;
    list_euclid(q,3)=akurasi;
    data{q,1}=myFiles(q).name;
    data{q,2}=hasil1;
    data{q,3}=hasil;
    data{q,4}=akurasi;

end

clear; close all; warning off all;
%A=imread('F:\New folder (6)\data uji\versi jpg\grtr\STARE\im0004.ah.jpg');
%B=imread('F:\New folder (6)\data uji\versi jpg\sauvola jp\STARE\im0004.jpg'); 
A=[1,0,0,0;1,1,1,1;0,1,1,1;];
B=[1,0,0,0;0,1,0,0;0,0,1,1;];
origImg = double(A);
distImg = double(B);

[M N] = size(origImg);
error = origImg - distImg;
MSE = sum(sum(error.^2)) / (M * N);

if(MSE > 0)
    PSNR = 10*log10(max(max(origImg)).^2/MSE);
else
    PSNR = 99;
end 

clear; close all; warning off all;
%A=imread('F:\New folder (6)\data uji\versi jpg\grtr\STARE\im0004.ah.jpg');
%B=imread('F:\New folder (6)\data uji\versi jpg\sauvola jp\STARE\im0004.jpg'); 
%A=imread('C:\Users\Reimu\Downloads\PSNR-example-base.jpg');
%B=imread('C:\Users\Reimu\Downloads\PSNR-example-base.jpg');
A=[1,0,0,0;1,1,1,1;0,1,1,1;];
B=[1,0,0,0;0,1,0,0;0,0,1,1;];
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

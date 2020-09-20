data = imread('F:\New folder (6)\data uji\versi jpg\grtr\im0002.ah.jpg');
data2= imread('F:\New folder (6)\data uji\versi jpg\dynam jp\im0002.jpg');
I = im2bw(data);
J = im2bw(data2);
[n,p] = size(I)
D = zeros(n,size(J,1));

for i = 1:size(J,1)
    D(:,i) = (I(:,1) - J(i,1)).^2;
    for j = 2:p
        D(:,i) = sqrt(D(:,i) + (I(:,j) - J(i,j)).^2);
    end
end
out=mean(D(:,i));
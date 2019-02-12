%HW1 Q4d
%Manoj Ravi
%Average Search time

T1=lsh('lsh',10,24,size(patches,1),patches,'range',255);

for i = 100:100:1000
tic; [nnlsh,numcand]=lshlookup(patches(:,i),patches,T1,'k',4,'distfun','lpnorm','distargs',{1});toc
endfor

%Elapsed time is 0.013582 seconds.
%Elapsed time is 0.010015 seconds.
%Elapsed time is 0.043262 seconds.
%Elapsed time is 0.00689387 seconds.
%Elapsed time is 0.0080142 seconds.
%Elapsed time is 0.00678992 seconds.
%Elapsed time is 0.0796578 seconds.
%Elapsed time is 0.00759411 seconds.
%Elapsed time is 0.0185502 seconds.
%Elapsed time is 0.037035 seconds.

%Average elapsed time : 0.023139 sec


for i = 100:100:1000
tic;d=sum(abs(bsxfun(@minus,patches(:,i),patches)));[ignore,ind]=sort(d);toc;
endfor

%Elapsed time is 0.229627 seconds.
%Elapsed time is 0.229598 seconds.
%Elapsed time is 0.233313 seconds.
%Elapsed time is 0.238337 seconds.
%Elapsed time is 0.238495 seconds.
%Elapsed time is 0.230438 seconds.
%Elapsed time is 0.223018 seconds.
%Elapsed time is 0.222204 seconds.
%Elapsed time is 0.23333 seconds.
%Elapsed time is 0.234385 seconds.

%Average elapsed time : 0.23123 sec

%lpnorm(patches(:,50),patches(:,51)
        

%Q4d Error Value Calculation
        
load patches;
        
for i = 100:100:1000
        
    
tic;d=sum(abs(bsxfun(@minus,patches(:,i),patches)));[ignore,ind]=sort(d);toc;
elinear(i/100)=lpnorm(patches(:,ind(2)),patches(:,i))+lpnorm(patches(:,ind(3)),patches(:,i))+lpnorm(patches(:,ind(4)),patches(:,i))
endfor

error_array_ind = 0


% Vary L
%We calculate error value based on similarity and not on 1-similarity. Hence, we infer the inverse results from the plots
        %obtained for L and K
        
for L=10:2:20

error_value=0
nnlsh = 0
        
for i = 100:100:1000
while size(nnlsh,2)!=4
T1=lsh('lsh',L,24,size(patches,1),patches,'range',255);
tic; [nnlsh,numcand]=lshlookup(patches(:,i),patches,T1,'k',4,'distfun','lpnorm','distargs',{1});toc
end

        
elsh(i/100)=lpnorm(patches(:,nnlsh(2)),patches(:,i))+lpnorm(patches(:,nnlsh(3)),patches(:,i))+lpnorm(patches(:,nnlsh(4)),patches(:,i))
endfor


for j = 1:10
error_value =error_value + (elsh(j)/elinear(j))
endfor
error_value =error_value/10
error_array_ind = error_array_ind+1
error_array(error_array_ind)=error_value


endfor
        
% Vary k

        for k=16:2:24
        
        error_value=0
        nnlsh = 0
        
        for i = 100:100:1000
        while size(nnlsh,2)!=4
        T1=lsh('lsh',10,k,size(patches,1),patches,'range',255);
        tic; [nnlsh,numcand]=lshlookup(patches(:,i),patches,T1,'k',4,'distfun','lpnorm','distargs',{1});toc
        end
        
        
        elsh(i/100)=lpnorm(patches(:,nnlsh(2)),patches(:,i))+lpnorm(patches(:,nnlsh(3)),patches(:,i))+lpnorm(patches(:,nnlsh(4)),patches(:,i))
        endfor
        
        
        for j = 1:10
        error_value =error_value + (elsh(j)/elinear(j))
        endfor
        error_value =error_value/10
        error_array_ind = error_array_ind+1
        error_array(error_array_ind)=error_value
        
        
        endfor

        
        

        
        
%100th patch and 10 nearest neighbours
        
load patches;
        
%100th patch
figure(1);imagesc(reshape(patches(:,100),20,20));colormap gray;axis image
        
T1=lsh('lsh',10,24,size(patches,1),patches,'range',255);
tic; [nnlsh,numcand]=lshlookup(patches(:,100),patches,T1,'k',11,'distfun','lpnorm','distargs',{1});toc
        
%10 nearest neighbours per lsh

figure(2);clf;
for k=1:10, subplot(2,5,k);imagesc(reshape(patches(:,nnlsh(k+1)),20,20)); colormap gray;axis image; end

        
tic;d=sum(abs(bsxfun(@minus,patches(:,100),patches)));[ignore,ind]=sort(d);toc;
        
%10 nearest neighbours per linear Search
figure(3);clf;
for k=1:10, subplot(2,5,k);imagesc(reshape(patches(:,ind(k+1)),20,20));colormap gray;axis image; end




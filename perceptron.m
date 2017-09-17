input=[0 0;0 1;1 0;1 1];
num_itr=4;
desired_out=[0;1;1;1];
bias=-1;
coeff=0.7;
weight=-1*2.*rand(3,1);
iterations=10000;
for i=1:iterations
 out=zeros(4,1);
 for j=1:num_itr
   y=bias*weight(1,1)+input(j,1)*weight(2,1)+input(j,2)*weight(3,1);
   out(j)=1/(1+exp(-y));
   delta=desired_out(j)-out(j);
   weight(1,1)=weight(1,1)+coeff*delta*bias;
   weight(2,1)=weight(2,1)+coeff*delta*input(j,1);
   weight(3,1)=weight(3,1)+coeff*delta*input(j,2);
 end
end
disp("predicted output")
disp(out);
disp("calculated weights")
disp(weight);



t=0:0.2:2*pi;
plot(t,sin(t),"b")
hold on;
plot(t,cos(t),"r--")
xlabel('time');
ylabel('Function value');
title('sin and cos functions');
legend('sin','cos');
xlim([0,2*pi]);
ylim([-1.4,1.4]);

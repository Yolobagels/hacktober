#include <stdio.h>
int main () {
float C=0.00058;
int f=150;
float V=3.5;
float p,p1,p2;
for (f=150;f<=300;f+=10){
  if (f==150){
    p = C*V*V*f;
    p1 = p;
    printf("V(volts) = %.5f     f(Mhz) = %d     P(watts) = %.5f\n",V,f,p);
  }
  else{
    V*=1.1;
    p = C*V*V*f;
    p2 = 100*p/p1 - 100;
    p1 = p;
    printf("V(volts) = %.5f     f(Mhz) = %d     P(watts) = %.5f     %% increase in P = %.5f\n",V,f,p,p2);
  }
}
}

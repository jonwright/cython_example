

#include <stdio.h>
#include "my_c_code.h"

#define N 10

int main(){
    double vecs[N][3];
    double mods[N];
    int i,j;
    for(i=0;i<N;i++){ 
        vecs[i][0]=i;
        vecs[i][1]=i+1;
        vecs[i][2]=i+2;
    }

    vnorm( vecs, mods, N );

    for(i=0; i<N; i++){
        for(j=0; j<3; j++){
            printf("vecs[%d][%d] = %f ",i,j,vecs[i][j]);
        }
        printf("|vec|=%f\n",mods[i]);
    }
    return 0;
}



#include <sys/time.h>

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "my_c_code.h"

#define N 1024*1024*4*4

int main(){
    vec    *vecs;
    double *mods , delta;
    int i,j;
    clock_t begin, end;

    struct timeval start, finish;

    vecs = malloc( N * sizeof( vec ) );
    if(vecs == NULL){
      printf("Malloc failed\n");
      exit(1);
    }
    mods = malloc( N * sizeof( double ));
    if(mods == NULL){
      printf("Malloc failed\n");
      exit(1);
    }

    j=0;
    for(i=0;i<N;i++){ 
        vecs[i][0]=j++;
        vecs[i][1]=j++;
        vecs[i][2]=j++;
    }
    vnorm( vecs, mods, N ); /* warm up */

    begin = clock();
    gettimeofday(&start, NULL);
    
    vnorm( vecs, mods, N );
    
    gettimeofday(&finish, NULL);
    end = clock();
    delta = (finish.tv_sec - start.tv_sec) +
	    (finish.tv_usec- start.tv_usec)/1e6;
    
    for(i=0; i<10; i++){
        for(j=0; j<3; j++){
            printf("vecs[%d][%d] = %f ",i,j,vecs[i][j]);
        }
        printf("|vec|=%f\n",mods[i]);
    }
    printf("Runtime for vnorm was %f %f /s, %f kB %f MB/s\n",
	   (double)(end-begin)/CLOCKS_PER_SEC,
	   delta,
	   (double)(sizeof(double)*N*4/1024),
	   (double)(sizeof(double)*N*4/1024/1024/delta)
	   );
    begin = clock();
    for(i=0;i<1000;i++)
      vnorm( vecs, mods, 1 );
    end = clock();
    printf("us per call for one value %f /us/\n",1000*(double)(end-begin)/CLOCKS_PER_SEC);
    free(vecs);
    free(mods);
    return 0;
}


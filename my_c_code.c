
#include <math.h>

#include "my_c_code.h"


void vnorm(double vecs[][3], double mods[],  int n){
  int i;
#pragma omp parallel for schedule(static)
  for(i=0; i<n; i++){
      mods[i] = sqrt( vecs[i][0]*vecs[i][0] + 
                      vecs[i][1]*vecs[i][1] + 
                      vecs[i][2]*vecs[i][2] );
  }
}








#include <iostream>
#include <armadillo>

using namespace std;
using namespace arma;

sp_mat _build_mat(int N, float J)
{
 sp_mat M(pow);

 M(1,2)=12;

 M.print("M=");
 cout << sizeof(table) <<"\n"
      << 2*sizeof(int) <<"\n";
 
 if(sizeof(table)>=2*sizeof(int)){
   table[0]=sizeof(table)-2*sizeof(int);
   table[1]=2;
 }
 return 1;
}

void _find_spectrum(sp_mat M, int Nb_values, float* values){
  vec eigval = eigs_sym(M,Nb_values,"sa"); // armadillo vec type
  vector<float> eigs = conv_to< vector<float> >::from(eigval); //std vector type
  if (sizeof(values)>= Nb_values*sizeof(float)){
    copy(eigs.begin(), eigs.end(), values);
  }
}

void compute_pack_spectrum(int N, int samples, int Nb_values, float* values){
  float *vals = new float[Nb_values];
  float J=0;
  int i=0;
  sp_mat M;
  for(i=0;i<samples;i++){
    J = float(i)/(float(samples-1));
    //M=_build_mat(N,J);
    _find_spectrum(M,Nb_values, vals);
    if (sizeof(values)>= Nb_values*samples*sizeof(float)){
      copy(vals,vals+Nb_values,values+i*Nb_values); // We need double-checks
    }

  }
}

extern "C" {
  // int buildMat(int* table){ return build_mat(table); }
  // int ftest(int b){ return b; }
  void computePackSpectrum(int N, int samples, int Nb_values, float* values){
    return compute_pack_spectrum(N,samples,Nb_values, values); }
}

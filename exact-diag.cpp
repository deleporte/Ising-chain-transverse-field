#include <iostream>
#include <armadillo>
#include <cmath>

using namespace std;
using namespace arma;

int number(int base, vector<int> state){
  int result=0;
  while(state.size()!=0){
    result *= base;
    result += state.back();
    state.pop_back();
  }
  return result;
}

vector<int> digits(int base, int i){
  int j=i;
  vector<int> state;
  while(j>0){
    state.push_back(j-base*int(j/base));
    j /= base;
  }
  return state;
}

sp_mat _build_mat(int N, float J)
{
  vector<float> data; // initialized to empty arrays
  vector<int> state, varstate, row_ind, col_ind;
  float value;
  int i,j;
  umat locations(2,pow(2,N)*(N+1));
  for(i=0; i<pow(2,N); i++){
    state= digits(2,i);
    while(state.size()<N){
      state.push_back(0);
      value=0;
      for(j=0; j<N; j++){
	value -= J*(2*state[j]-1)*(2*state[(j+1)%N]-1);
	copy(state.begin(), state.end(), varstate.begin());
	varstate[j]=1-varstate[j];
	col_ind.push_back(i);
	row_ind.push_back(number(2,varstate));
	data.push_back(1.-J);
      }
      data.push_back(value);
      col_ind.push_back(i);
      row_ind.push_back(i);
    }
  }
  locations.insert_cols(0,conv_to<ucolvec>::from(row_ind));
  locations.insert_cols(1,conv_to<ucolvec>::from(col_ind));
  return sp_mat(locations, conv_to<colvec>::from(data));
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
    M=_build_mat(N,J);
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

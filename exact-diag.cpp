#include <iostream>
//#define ARMA_64BIT_WORD
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
  vector<double> data; // initialized to empty arrays
  vector<int> state, varstate, row_ind, col_ind;
  data.reserve(N*pow(2,N));
  row_ind.reserve(N*pow(2,N));
  col_ind.reserve(N*pow(2,N));
  state.reserve(N);
  varstate.reserve(N);
  double value;
  int i,j;
  umat locations;//(2,pow(2,N)*(N+1));
  for(i=0; i<pow(2,N); i++){
    state= digits(2,i);
    while(state.size()<N){
      state.push_back(0);
    }
    value=0;
    for(j=0; j<N; j++){
      value -= J*(2*state[j]-1)*(2*state[(j+1)%N]-1);
      varstate=state;
      varstate[j]=1-varstate[j];
      col_ind.push_back(i);
      row_ind.push_back(number(2,varstate));
      data.push_back(1.-J);
    }
    data.push_back(value);
    col_ind.push_back(i);
    row_ind.push_back(i);
  }
  locations.insert_rows(0,conv_to<urowvec>::from(row_ind));
  locations.insert_rows(1,conv_to<urowvec>::from(col_ind));
  return sp_mat(locations, conv_to<colvec>::from(data),pow(2,N),pow(2,N));
}

void _find_spectrum(sp_mat M, int Nb_values, double* values){
  vector<double> eigs;
  eigs.reserve(Nb_values);
  vec eigval = eigs_sym(M,Nb_values,"sa"); // armadillo vec type
  eigs = conv_to< vector<double> >::from(eigval); //std vector type
  //if (sizeof(values)>= Nb_values*sizeof(double)){
    copy(eigs.begin(), eigs.end(), values);
    //}
}

void compute_pack_spectrum(int N, int samples, int Nb_values, double* values){
  double *vals = new double[Nb_values];
  float J=0;
  int i=0;
  sp_mat M;
  for(i=0;i<samples;i++){
    J = float(i)/(float(samples-1));
    M=_build_mat(N,J);
    _find_spectrum(M,Nb_values, vals);
    //if (sizeof(values)>= Nb_values*samples*sizeof(double)){
      copy(vals,vals+Nb_values,values+i*Nb_values); // We need double-checks
      //}
  }
  for(i=0; i<samples*Nb_values; i++){
    cout << values[i] << endl;
  }
}

//use following for debugging
// int main(){
//   sp_mat M;
//   vector<int> state;
//   double eigvals[3];
//   cout << "Testing the library." << endl;
//   cout << "The (inverse) digits of 6 in base 2 are: "
//        << digits(2,6)[0]
//        << digits(2,6)[1]
//        << digits(2,6)[2] << endl;
//   state.push_back(0);
//   state.push_back(1);
//   state.push_back(1);
//   cout << "Reciprocally, (the inverse of) 110 is: " << number(2,state) << endl;
//   M=_build_mat(2,0.9);
//   M.print("The matrix for N=2,J=0.9 is :");
//   _find_spectrum(M,3,eigvals);
//   cout << "Its 3 first values are: "
//        << eigvals[0] << "\n"
//        << eigvals[1] << "\n"
//        << eigvals[2] << endl;
//   return 0;
// }

extern "C" {
  void computePackSpectrum(int N, int samples, int Nb_values, double* values){
    return compute_pack_spectrum(N,samples,Nb_values, values); }

  void computeSpectrum(int N, float J, int Nb_values, double* values){
    return _find_spectrum(_build_mat(N,J),Nb_values, values); }
}

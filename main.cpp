#include<iostream>


bool isSolved(int Uface[2][2] , int Dface[2][2], int Lface[2] , int Rface[2] , int Fface[2] , int Bface[2]){
	// check for Uface
	for(int i=0;i<2;i++){
		for(int j=0;j<2;j++){
			if(Uface[i][j]!=Uface[0][0]){
				return false;
			}
		}
	}
	// check for Dface
	for(int i=0;i<2;i++){
		for(int j=0;j<2;j++){
			if(Dface[i][j]!=Dface[0][0]){
				return false;
			}
		}
	}
	// check for Lface
	if(Lface[0]!=Lface[1]){
		return false;
	}
	// check for Rface
	if(Rface[0]!=Rface[1]){
		return false;
	}
	// check for Fface
	if(Fface[0]!=Fface[1]){
		return false;
	}
	// check for Bface
	if(Bface[0]!=Bface[1]){
		return false;
	}

	return true;

}

void Solve2x2x1(){

}

int main(){

	int U[2][2] = { {1,1},{1,1} };
	int D[2][2] = { {2,2},{2,2} };
	int L[2] = {3,3};
	int R[2] = {4,4};
	int F[2] = {5,5};
	int B[2] = {6,6};

	if(isSolved(U,D,L,R,F,B)){
		std::cout<<"YES it is solved !"<<std::endl;
	}
	else{
		std::cout<<"No it is Not solved !"<<std::endl;
	}

	return 0;
}

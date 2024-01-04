#include <iostream>
#include <fstream>
#include <string>

bool isSolved(int Uface[2][2], int Dface[2][2], int Lface[2], int Rface[2], int Fface[2], int Bface[2])
{
	// check for Uface
	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			if (Uface[i][j] != Uface[0][0])
			{
				return false;
			}
		}
	}
	// check for Dface
	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			if (Dface[i][j] != Dface[0][0])
			{
				return false;
			}
		}
	}
	// check for Lface
	if (Lface[0] != Lface[1])
	{
		return false;
	}
	// check for Rface
	if (Rface[0] != Rface[1])
	{
		return false;
	}
	// check for Fface
	if (Fface[0] != Fface[1])
	{
		return false;
	}
	// check for Bface
	if (Bface[0] != Bface[1])
	{
		return false;
	}

	return true;
}

void Solve2x2x1(int Uface[2][2], int Dface[2][2], int Lface[2], int Rface[2], int Fface[2], int Bface[2])
{
	std::string mystring;

	std::ifstream myfile1("combinations_length_2.txt");

	while (getline(myfile1, mystring))
	{
		// std::cout << mystring<<" ";
		// for(int i=0;i<sizeof(mystring)/sizeof(mystring[0]);i++){
			std::cout<<mystring<<" ";
		// }
		std::cout<<std::endl;

	}

	std::cout << std::endl;
}
//NOTE : 
// A = U
// B = D
// C = R
// D = L

int main()
{

	int U[2][2] = {{1, 2}, {1, 1}};
	int D[2][2] = {{2, 2}, {2, 2}};
	int L[2] = {3, 3};
	int R[2] = {4, 4};
	int F[2] = {5, 5};
	int B[2] = {6, 6};

	if (isSolved(U, D, L, R, F, B))
	{
		std::cout << "YES it is solved !" << std::endl;
	}
	else
	{
		std::cout << "No it is Not solved !" << std::endl;

		// solve
		Solve2x2x1(U, D, L, R, F, B);
	}

	return 0;
}

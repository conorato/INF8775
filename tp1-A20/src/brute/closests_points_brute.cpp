// A brute force program in C++ to find the smallest distance from a
// given set of points.
// Brute force algo source: https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/

#include <iostream>
#include <float.h>
#include <stdlib.h>
#include <math.h>
using namespace std;


// A structure to represent a Point in 2D plane
struct Point
{
	int x, y;
};

// A utility function to find the distance between two points
float dist(Point p1, Point p2)
{
	return sqrt( (p1.x - p2.x)*(p1.x - p2.x) +
				(p1.y - p2.y)*(p1.y - p2.y)
			);
}

// The main function that finds the smallest distance
// A Brute Force method to return the smallest distance between two points
// in P[] of size n
float closest(Point P[], int n)
{
	float min = FLT_MAX;
	for (int i = 0; i < n; ++i)
		for (int j = i+1; j < n; ++j)
			if (dist(P[i], P[j]) < min)
				min = dist(P[i], P[j]);
	return min;
}

Point * readFile(string filename)
{
  string line;
  ifstream myfile = ifstream(filename);
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      cout << line << '\n';
    }
    myfile.close();
  }
}

int main(int argc, char *argv[])
{
  if (argc == 1)
  {
    Point P[] = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
    int n = sizeof(P) / sizeof(P[0]);
    cout << "The smallest distance is " << closest(P, n) << endl;
  }
  else
  {
    cout << "You must put into args only the input file path" << endl;
  }
	return 0;
}

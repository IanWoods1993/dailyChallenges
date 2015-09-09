#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
class Point
{
public:
	Point(int incomingX, int incomingY);
	void setX(double x);
	void setY(double y);
	double getX();
	double getY();
private:
	double x;
	double y;
};
double calculatePath(Point p0, Point p1, Point p2, Point p3);
vector<Point> getPoints();
int main(void)
{
	vector<Point> pointVec;
	pointVec = getPoints();
	if
	(calculatePath(pointVec[0], pointVec[2], pointVec[3], pointVec[1]) < calculatePath(pointVec[2], pointVec[0], pointVec[1], pointVec[3]))// 0 is A, 1 is B, etc.
	{
		cout << "It is more efficient for driver 1 to travel the A, C, D, B path" << endl;
	}
	else
	{
		cout << "It is more efficient for driver 2 to travel the C, A, B, D path" << endl;
	}
	return(0);
}

vector<Point> getPoints()
{
	vector<Point> pointVec;
	double tempX, tempY;
	char letter = 'A';
	for(int i = 0; i < 4; i++)
	{
		cout << "Enter x value for point " << letter <<": ";
		cin >> tempX;
		cout << "Enter y value for point " << letter <<": ";
		cin >> tempY;
		Point *newPoint = new Point(tempX, tempY);
		pointVec.push_back(*newPoint);
		letter++;
	}
	return(pointVec);
}
Point::Point(int incomingX, int incomingY)
{
	this->x = incomingX;
	this->y = incomingY;
}

void Point::setX(double incomingX)
{
	this->x = incomingX;
}

void Point::setY(double incomingY)
{
	this->y = incomingY;
}

double Point::getX()
{
	return(this->x);
}

double Point::getY()
{
	return(this->y);
}

double calculatePath(Point p0, Point p1, Point p2, Point p3)
{
	vector<Point> temp;
	temp.push_back(p0); temp.push_back(p1); temp.push_back(p2), temp.push_back(p3);
	double pathLength = 0;
	double xDistSquared = 0;
	double yDistSquared = 0;
	for(int i = 1; i < 4; i++)
	{
		xDistSquared = pow(temp[i].getX() - temp[i-1].getX(),2);
		yDistSquared = pow(temp[i].getY() - temp[i-1].getY(),2);
		pathLength += sqrt(xDistSquared + yDistSquared);
	}
	return(pathLength);
}

/* Note - I understand latitude and longitude traditionally
necessitates a spherical coordinate system, but given that for
a reasonable distance the difference between spherical and
traditional Cartesian coordinates is quite small, I decided to
use Cartesian coordinates for simplicity */

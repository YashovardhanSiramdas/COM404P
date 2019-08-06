/******************************************
*
*    Circle drawing using DDA Algorithm
*
*	code.cheraus.com
******************************************/

#include<iostream.h>
#include<conio.h>
#include<dos.h>
#include<math.h>
#include<graphics.h>

//function prototype for DDA circle function
void dda_circle(int xc,int yc,int r);

int main()
{

   int xc,yc,r,gd,gm;

   clrscr();

   //taking circle parameters from the user
   cout<<"\nEnter the Center point (xc,yc) :";
   cin>>xc>>yc;

   cout<<"\nEnter the Radius :";
   cin>>r;

   
   detectgraph(&gd,&gm);
   initgraph(&gd,&gm,"C:\\turboc3\\bgi");

   setcolor(10);

   //drawing the co-ordinate axes
   line(0,240,640,240);
   line(320,0,320,480);

   setcolor(5);

   //converting the screen co-ordinates to more user friendly co-ordinates
   // with respect to the centre of the screen.
   xc = 320 + xc;
   yc = 240 - yc;

   //function call for DDA circle.
   dda_circle(xc,yc,r);

   getch();
   return 0;

}

/*
Function Definition for DDA circle

Function: dda_circle() Draws the circle with given parameters using DDA algorithm.
Input: Takes three input
       1) x co-ordinate for centre
	   2) y co-ordinate for centre
	   3) radius of the circle
	   
Return : This function does not return anything.

*/

void dda_circle(int xc,int yc,int r)
{

   float xc1,xc2,yc1,yc2,eps,sx,sy;

  int val,i;

  xc1=r;

  yc1=0;

  sx=xc1;

  sy=yc1;

  i=0;

  do{

      val=pow(2,i);

      i++;

      }while(val<r);

  eps = 1/pow(2,i-1);

  do{

      xc2 = xc1 + yc1*eps;
      yc2 = yc1 - eps*xc2;

      putpixel(xc+xc2,yc-yc2,3);

      xc1=xc2;

      yc1=yc2;

     }while((yc1-sy)<eps || (sx-xc1)>eps);

}

          
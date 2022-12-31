#include<windows.h>
#include <conio.h>
#include<stdlib.h>
#include <stdio.h>
#include<time.h>
int lei[11][11];
int jilu[11][11];
int xx = 0,yy = 0;
void saolei(int lei[11][11],int jilu[11][11],int xx,int yy);
void biaoji(int lei[11][11],int jilu[11][11],int xx,int yy);
void gotoxy(int x, int y);
char c;
int main()
{
	clock_t start,end;
	srand((unsigned)time(NULL));
	for (int a = 0; a <11; a++) //初始化雷列表和记录扫过的列表 
	{
		for(int b = 0; b< 11;b++)
		{
			lei[a][b] = 0;
			jilu[a][b] = 0;
		}
	}
	for (int a = 0; a < 10; a++) //生成雷 
	{
		int x,y;
		x = rand()%9+1;
		y = rand()%9+1;
		if(lei[x][y]!=9)
		{
			lei[x][y] = 9;
			jilu[x][y] = 9;
		}
		else
			a--;
	}
	for (int a = 1; a <10; a++) //生成其他数字 
	{
		for(int b = 1; b< 10;b++)
		{
			if(lei[a][b] == 0)
			{
				for(int x = a-1;x <= a+1;x++)
				{
					for(int y = b-1;y <= b+1;y++)
					{
						if (lei[x][y] == 9)
						{
							lei[a][b]++;
						}
					}
				}
			}
		}
	}
	for (int a = 1; a <10; a++) //输入地图 
	{
		for(int b = 1; b< 10;b++)
		{
			printf("■");
		}
		printf("\n");
	}
	gotoxy(20,2); 
	printf("按空格开始计时；按空格扫雷，F标记雷"); 
	gotoxy(xx,yy);
	while(1) //判断开始 
	{
		c = _getch();
		start = clock();
		break;
	}
	while(1) //判断按键 
	{
		c = _getch();
		if(c == 'w')
		{
			if(yy > 0)
				yy--;
			gotoxy(xx,yy);
		}
		if(c == 's')
		{
			if(yy < 8 )
				yy++;
			gotoxy(xx,yy);
		}
		if(c == 'a')
		{
			if(xx > 0)
				xx--;
			gotoxy(xx,yy);
		}
		if(c == 'd')
		{
			if(xx < 8)
				xx++;
			gotoxy(xx,yy);
		}
		if(c == ' ')
			saolei(lei,jilu,xx,yy);
		if(c == 'f')
			biaoji(lei,jilu,xx,yy);
		int num  = 0;
		for (int a = 1; a <10; a++)
		{
			for(int b = 1; b< 10;b++)
			{
				if (jilu[a][b] == 9)
					num++;
			}
		}
		if (num == 81) //判断胜利 
		{	
			end = clock();
			gotoxy(20,0);
			printf("time=%f s\n",(double)(end-start)/CLK_TCK);
			gotoxy(20,1);
			printf("你赢了");
			Sleep(INFINITE); 
		}
	}
	return 0;
}
void saolei(int lei[11][11],int jilu[11][11],int xx,int yy)
{
	if(lei[xx+1][yy+1] == 9)
	{
		gotoxy(xx,yy);
		if(jilu[xx+1][yy+1] == 9)
		{
			printf("★");
			gotoxy(20,0);
			printf("游戏结束");
			Sleep(INFINITE); 
		}
	}
	else if (lei[xx+1][yy+1] == 0)
	{
		gotoxy(xx,yy);
		printf("%d ",lei[xx+1][yy+1]);
		jilu[xx+1][yy+1] = 9;
		if(xx>0)
		{
			if(jilu[xx][yy+1]!=9)
				saolei(lei,jilu,xx-1,yy); //2
			if(yy>0)
			{
				if(jilu[xx][yy]!=9)
				saolei(lei,jilu,xx-1,yy-1); //1
			}
			if(yy<8)
			{
				if(jilu[xx][yy+2]!=9)
					saolei(lei,jilu,xx-1,yy+1); //3
			}
			
		}
		if(yy>0)
		{
			if(jilu[xx+1][yy]!=9)
				saolei(lei,jilu,xx,yy-1); //4
			if(xx<8&&jilu[xx+2][yy]!=9)
				saolei(lei,jilu,xx+1,yy-1); //7
		}
		if(yy<8)
		{
			if(jilu[xx+1][yy+2]!=9)
				saolei(lei,jilu,xx,yy+1); //6
		}
		if(xx<8)
		{
			if(jilu[xx+2][yy+1]!=9)
				saolei(lei,jilu,xx+1,yy); //8
			if(yy<8&&jilu[xx+2][yy+2]!=9)
				saolei(lei,jilu,xx+1,yy+1); //9
		}
	}
	else
	{
		gotoxy(xx,yy);
		printf("%d ",lei[xx+1][yy+1]);
		jilu[xx+1][yy+1] = 9;
	}
	gotoxy(xx,yy);
} 
void biaoji(int lei[11][11],int jilu[11][11],int xx,int yy)
{
	gotoxy(xx,yy);
	printf("* ");
	gotoxy(xx,yy);
}
void gotoxy(int x, int y)//位置函数
{
	COORD pos;
	pos.X = 2 * x;
	pos.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

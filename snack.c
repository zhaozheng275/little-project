#include <stdio.h>
#include<windows.h>
#include <conio.h>
#include<stdlib.h>
int snake[10][2];
int apple[2];
int len = 2;
int score = 0;
char ch;
void wall_info();
void snake_apple();
void movesnake();
void gotoxy(int x, int y);
void if_wall();
void color(int a);
void eat_apple();
int main()
{
	wall_info();
	snake_apple();
	do
	{
		movesnake();
		eat_apple();
		if_wall();
	} while (1);
}
void gotoxy(int x, int y)//位置函数
{
	COORD pos;
	pos.X = 2 * x;
	pos.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}
void color(int a)//颜色函数
{
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), a);
}
void wall_info()
{
	
	int wall[23][23];
	for (int a = 0; a < 23; a++)
	{
		for (int b = 0; b < 23; b++)
			wall[a][b] = 0;
	}
	for (int a = 1; a < 22; a++)
	{
		for (int b = 1; b < 22; b++)
			wall[a][b] = 1;
	}
	for (int a = 0; a < 23; a++)
	{
		for (int b = 0; b < 23; b++)
		{
			if (wall[a][b] == 1)
			{
				color(11);
				printf("■");
			}
			else if (wall[a][b] == 0)
			{
				color(11);
				printf("□");
			}
		}
		printf("\n");
	}
	gotoxy(24,5); 
	printf("按w、s、a、d");
	gotoxy(24, 6);
	printf("按任意键暂停");
	gotoxy(24, 8);
	printf("得分：%d", score);
}
void snake_apple()
{
	int x, y;
	x = 1 + rand() % 21;
	y = 1 + rand() % 21;
	apple[0] = x;
	apple[1] = y;
	color(12);
	gotoxy(apple[0], apple[1]);
	printf("●");
	snake[0][0] = 1 + rand() % 21;
	snake[0][1] = 1 + rand() % 21;
	gotoxy(snake[0][0], snake[0][1]);
	color(14);
	printf("¤");
	for (int i = 1; i <= len; i++)
	{
		snake[i][0] = snake[0][0];
		snake[i][1] = snake[0][1] - i;
		gotoxy(snake[i][0], snake[i][1]);
		printf("★");
	}
}
void movesnake()
{

	int snake_tail[10][2];
	int i;
	for (i = 0; i <= len; i++)
	{
		snake_tail[i][0] = snake[i][0];
		snake_tail[i][1] = snake[i][1];
	}
	if (_kbhit())
		ch = _getch();
	switch (ch)
	{
	case 'w':snake[0][1]--; break;
	case 's':snake[0][1]++; break;
	case 'a':snake[0][0]--; break;
	case 'd':snake[0][0]++; break;
	default: break;
	}
	if (ch == 'w' || ch == 'a' || ch == 's' || ch == 'd')
	{
		gotoxy(snake[0][0], snake[0][1]);
		color(14);
		printf("¤");
		gotoxy(snake_tail[0][0], snake_tail[0][1]);
		color(14);
		printf("★");


		for (i = 1; i <= len; i++)
		{
			snake[i][0] = snake_tail[i - 1][0];
			snake[i][1] = snake_tail[i - 1][1];
		}
		for (i = 1; i <= len; i++)
		{
			gotoxy(snake[i][0], snake[i][1]);
			color(14);
			printf("★");
		}
		i = i - 1;
		if (snake_tail[i][0] != 0 && snake_tail[i][1] != 0)
		{
			gotoxy(snake_tail[i][0], snake_tail[i][1]);
			color(11);
			printf("■");
		}
		gotoxy(23, 23);
	}
	Sleep(200 - 0.5 * score);
}
void eat_apple()
{
	if (snake[0][0] == apple[0] && snake[0][1] == apple[1])
	{

		score = score + 1;
		if (len < 9)
			len = len + 1;
		apple[0] = 1 + rand() % 21;
		apple[1] = 1 + rand() % 21;
		color(12);
		gotoxy(apple[0], apple[1]);
		printf("●");
		gotoxy(24, 8);
		color(14);
		printf("得分：%d", score);
	}
}
void if_wall()
{
	if (snake[0][1] == 0 || snake[0][1] == 22 || snake[0][0] == 0 || snake[0][0] == 22)
	{
		gotoxy(10, 10);
		color(10);
		printf("游戏失败");
		Sleep(INFINITE);
	}
}

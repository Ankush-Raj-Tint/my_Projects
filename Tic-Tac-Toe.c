// 1.create an array to represent the board,
//a.can be of type char and should be 3x3 array.
//b. should not contain 0.
//c. each element represents coordinates on the board that each user can select.

//2. some functions that you should probably create,
//a. checkForWin- checks to see of the player has won or it is a draw.
//b. drawBoard- redraws the board for each player's turn.
//c. markBoard- sets the char array for selection and marks the invalid selection.

#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
// declaring array as a global variable because it need to be accessed by other functions.
// though its not a good practice, but until now we haven't studied about pointers and call by reference value.
char square[10]={'o','1','2','3','4','5','6','7','8','9'};// 0 is used to facilitate the purpose of indexing of array.
int player, choice;// player 1 or player 2. choice will be which box to enter.


int checkForWin();// checks the winner or whether its a draw.
void displayBoard();// its just going to redraw board after each player's turn.
void markBoard(char mark);// going to display board with the player's marked response.so we can reuse it.

int main()
{
    int gameStatus;
    char mark;
    player = 1;// its player 1 to start the game.
    do
    {
        displayBoard();
        player = (player % 2) ? 1 : 2;
        printf("player %d, enter a number:",player);//  ,player refers to the turn(1 or 2)
        scanf("%d", &choice);

        mark = (player == 1)?'X':'O';

        markBoard(mark);
        gameStatus = checkForWin();
        player++;


    }while (gameStatus == -1);
    return 0;
}
/*
its returning game status.
a. 1 for game is over with result.
b. -1 for game is in progress.
c. 0 for game is over with no result or a draw.
*/

int checkForWin()
{
    int returnValue = -1;

    if (square[1] == square[2] && square[2] == square[3])
    {
        returnValue = 1;
    }
    else if (square[4]==square[5] && square[5]==square[6])
        returnValue =  1;

    else if (square[7]==square[8] && square[8]==square[9])
        returnValue = 1;

    else if (square[1]==square[4] && square[4]==square[7])
        returnValue = 1;

    else if (square[2]==square[5] && square[5]==square[8])
        returnValue = 1;

    else if (square[3]==square[6] && square[6]==square[9])
        returnValue = 1;

    else if (square[1]==square[5] && square[5]==square[9])
        returnValue = 1;

    else if (square[3]==square[5] && square[5]==square[7])
        returnValue = 1;

    else if (square[1]!='1' && square[2]!='2' && square[3]!='3' && square[4]!='4' && square[5]!='5' && square[6]!='6' && square[7]!='7' && square[8]!='8' && square[9]!='9')
        returnValue = 0;// because if it is a draw then the all the squares will be filled obviously.

    else
        returnValue = -1;

    return returnValue;
}

void displayBoard()
{
    system("cls");

    printf("\n\n tic tac toe \n\n");
    printf("player 1(X) - player 2(O) \n\n\n");

    printf("   %c  | %c  | %c \n",square[1],square[2],square[3]);
    printf("   ___|____|___ \n");// had to shift the vertical bar leftwards because there was not any data contained in it(compensating).

    printf("   %c  | %c  | %c \n",square[4],square[5],square[6]);
    printf("   ___|____|___ \n");

    printf("   %c  | %c  | %c \n",square[7],square[8],square[9]);
    return;// use this format of return when the function is returning void.

}
/*****************
here we set the the board with the correct character, x or o in the correct spot
 in the array(board).
*/
void markBoard(char mark)
{
    if (choice == 1 && square[1] == '1')
        square[1]= mark;

    else if (choice == 2 && square[2] == '2')
        square[2] = mark;

    else if (choice == 3 && square[3] == '3')
        square[3] = mark;

    else if (choice == 4 && square[4] == '4')
        square[4] = mark;

    else if (choice == 5 && square[5] == '5')
        square[5] = mark;

    else if (choice == 6 && square[6] == '6')
        square[6] = mark;

    else if (choice == 7 && square[7] == '7')
        square[7] = mark;

    else if (choice == 8 && square[8] == '8')
        square[8] = mark;

    else if (choice == 9 && square[9] == '9')
        square[9] = mark;

    else
    {
        printf("invalid move");

        player--;
        getch(); // it pauses the program for the user to press enter to go on.
    }


}


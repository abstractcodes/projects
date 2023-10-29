// This is a simple to do list without using GUI model.
// file input and output functionality is used for this code.
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int enter_number = 1;
    // taking user input for the dates.
    printf("Enter a number to put in a file: ");
    // checking the user input is correct or not.
    scanf("%d", &enter_number);
    printf("%d",enter_number);

    // opening the input_dates file if it exists to write in it or else a new files is created to write in it.
    FILE* file = fopen("list.txt","w");
    fprintf(file,"%d",enter_number);
    fclose(file);
    return 0;
   
}
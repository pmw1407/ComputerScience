#include <stdio.h>
#include <string.h>
#define TRUE 1
#define FALSE 0

void next_tag(char *str){
    char temp[8] = "START";
    strcpy(str, temp);
}

int main(int argc, char * argv[]){
    int valid = FALSE;
    char str1[8];
    char str2[8];

    next_tag(str1);
    gets(str2);
    if(strncmp(str1, str2, 8) == 0){
        valid = TRUE;
    }

    printf("buffer1: str1(%s), str2(%s), valid(%d)\n", str1, str2, valid);
}

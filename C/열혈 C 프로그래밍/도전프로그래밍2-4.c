#include <stdio.h>
#include <string.h>

void Palindrome(char * array, int len){
    int count = 0;
    for (int i = 0 ; i < len/2 ; i++){
        if (array[i] == array[len-1 - i]){
            count ++;
        }
    }
    if (count == len/2){
        printf("palindrome");
    }
    else{
        printf("not palindrome");
    }
}

int main(){
    char arr[100];
    printf("word : ");
    scanf("%s",arr);
    int len = strlen(arr);
    Palindrome(arr, len);
}

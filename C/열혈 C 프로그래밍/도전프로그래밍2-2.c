#include <stdio.h>

int main(void){
    int num;
    int array[100];
    int i = 0;
    printf("Enter a decimal integer : ");
    scanf("%d",&num);
    
    while(num >= 1){
        array[i] = num % 2;
        num = num / 2;
        i++;
    }

    for (i; i > 0 ; i--){
        printf("%d",array[i-1]);
    }
    return 0;
}

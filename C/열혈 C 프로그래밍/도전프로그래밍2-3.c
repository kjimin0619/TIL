#include <stdio.h>

int main(void)
{
    int num = 0;
    int arr[10];
    int Odd = 0;
    int Even = 9;

    for (int i = 0; i < 10 ; i++){
        printf("enter : ");
        scanf("%d", &num);
        if (num % 2 != 0) 
            arr[Odd++] = num;           
        else
            arr[Even--] = num;
    }
    printf("<print all> \n");
    for (int k = 0; k < 10 ; k++){
        printf("%d  ",arr[k]);
    }
    return 0;
}

#include <stdio.h>

// Odd number
void findODD(int * array, int len){
    printf("odd number is.. ");
    for (int i = 0; i < len ; i++){
        if (array[i] % 2 != 0){
            printf("%d, ",array[i]);
        }
    }
    printf("\n");
}

// Even number
void findEVEN(int * array, int len){
    printf("even number is.. ");
    for (int i = 0; i < len ; i++){
        if (array[i] % 2 == 0){
                printf("%d, ",array[i]);
            }
    }
    printf("\n");
}

int main(void){
    int arr[10];
    printf("enter 10 number \n");
    for (int i = 0; i < sizeof(arr)/sizeof(int) ; i++){
        printf("number[%d] : ",i+1);
        scanf("%d",&arr[i]);
    }

    findODD(arr,sizeof(arr)/sizeof(int));
    findEVEN(arr,sizeof(arr)/sizeof(int));
    return 0;
}

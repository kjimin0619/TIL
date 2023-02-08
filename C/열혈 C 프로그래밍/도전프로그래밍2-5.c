#include <stdio.h>
#include <string.h>
// buble sort
void Ascendingorder(int * str, int len){
    int i , j;
    int temp;
    for (i = 0 ; i < len-1 ; i++){ // 대소 비교 시작할 인덱스
        for (j = 0 ; j < len-i-1 ; j++){ // 본격적인 대소 비교 시작
            if (str[j] > str[j+1]){
                temp = str[j];
                str[j] = str[j+1];
                str[j+1] = temp;
            }
        }
    }
}

void descendingorder(int str[], int len){
    int i , j;
    int temp;
    for (i = 0 ; i < len-1 ; i++){ // 대소 비교 시작할 인덱스
        for (j = 0 ; j < len-i-1 ; j++){ // 본격적인 대소 비교 시작
            if (str[j] < str[j+1]){
                temp = str[j];
                str[j] = str[j+1];
                str[j+1] = temp;
            }
        }
    }
}

int main(){
    // 배열의 길이 사용자 입력
    int len;
    printf("length : ");
    scanf("%d",&len);

    // 수 사용자 입력
    int arr[len];
    for (int i = 0; i < len ; i++){
        printf("enter : ");
        scanf("%d", &arr[i]);
    }

    // ascending
    Ascendingorder(arr,len);
    printf("ascending order\n");
    for (int i = 0 ; i < len ; i++){
        printf("%d", arr[i]);
    }
    printf("\n");

    // descending
    descendingorder(arr,len);
    printf("descending order\n");
    for (int i = 0 ; i < len ; i++){
        printf("%d", arr[i]);
    }
    printf("\n");
}

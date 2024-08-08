#include<stdio.h>
void BubbleSort(int x[], int n){
    int temp;
    for (int i = 0; i < n-1 ; i++){
        for (int j = 0; j < n-1-i; j++){
            if (x[j]>x[j+1]){
                temp = x[j];
                x[j] = x[j+1];
                x[j+1] = temp;
            }
        }
    }
}

void Display(int x[], int n){
    for (int i = 0; i < n; i++){
        printf("%d\t",x[i]);
    }
}

int main(){
	int n,a[10],i;
    printf("Enter Number Of Elements You Want To Store In Array : ");
    scanf("%d",&n);
    printf("\n");
    for( i = 0 ; i < n ; i++ ){
        printf("Enter Element %d : ",i+1);
        scanf("%d",&a[i]);
    }
    printf("\nBefore Sorting :  ");
    Display(a,n);
    printf("\nAfter Sorting  :  ");
    BubbleSort(a,n);
    Display(a,n);
    return 0;
}
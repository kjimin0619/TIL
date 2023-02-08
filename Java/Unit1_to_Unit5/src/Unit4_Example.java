public class Unit4_Example {
    public static void main(String[] args){
        // 1. 조건문의 참과 거짓 : everywhere

        // 2. 3배수의 합
        int i = 1;
        int sum = 0;
        while (i <= 1000){
            if (i%3 == 0){
                sum = sum +  i;
            }
            i++;
        }
        System.out.println("#2. 3의 배수의 합 : "+sum);

        // 3. 별 출력하기
        for (int j = 1 ; j <= 5 ; j++){
            int k = 1;
            while(k <= j) {
                System.out.print("*");
                k++;
            }
            System.out.println(" ");
        }

        // 4. 1~100까지 출력
        for (int n = 0 ; n < 100 ; n++){
            System.out.println(n+1);
        }

        // 5. 평균점수 구하기
        int[] marks = {70, 60, 55, 75, 95, 90, 80, 80, 85, 100};
        int sums = 0;
        for (int mark : marks){
            sums = sums + mark;
        }
        System.out.println("#5. 평균점수 구하기 : "+ (float)sums/marks.length);

    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Scanner;

import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.PrintWriter;

import java.util.Comparator;

public class Examples_1to8 {
    // 피보나치
    static int fib(int n){
        if (n == 0){
            return 0;
        }
        else if (n == 1){
            return 1;
        } else {
            return fib(n - 2) + fib(n - 1);
        }
    }

    static void gugudan(int d){
        for (int k = 1 ; k < 10 ; k ++){
            System.out.printf("%d ", d*k);
        }

    }
    public static void main(String args[]) throws IOException{
        // 1. 문자열 바꾸기
        String s = "a:b:c:d";

        String s1 = s.replace(':', '#');
        String s2[] = s.split(":");
        String s2_1 = String.join("#", s2);
        
        System.out.println(s1);
        System.out.println(s2_1);


        // 2. 맵에서 값 추출
        HashMap<String, Integer> a = new HashMap<>();
        a.put("A", 90);
        a.put("B", 80);
        System.out.println(a.getOrDefault("C", 70));


        // 3. 50점 이상 점수의 총합 구하기
        int[] A = {20, 55, 67, 82, 45, 33, 90, 87, 100, 25};
        int sum = 0;
        for (int score : A){
            if (score >= 50) {
                sum += score;
            }
        }

        System.out.println(sum);

        // 4. 피보나치 수열
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> nums = new ArrayList<>(Arrays.asList(0,1));
        

        for (int i = 0 ; i <= n ; i++){
            if (i >= 2) {
                int k = nums.get(i-1) + nums.get(i-2);
                nums.add(k);
                System.out.println(k);
            }
        }

        // 피보나치 메서드 활용
        for (int i = 0 ; i < n+1 ; i ++){
            System.out.println(fib(i));
        }

        // 5. 한 줄 구구단
        System.out.print("구구단을 출력할 숫자를 입력하세요(2~9): ");
        Scanner sc5 = new Scanner(System.in);
        int dan = sc5.nextInt();
        gugudan(dan);
        System.out.println();

        // 6. 입력 숫자의 총합 구하기
        Scanner sc6 = new Scanner(System.in);
        String s6 = sc6.nextLine();
        String nums6[] = s6.split(",");

        int sum6 = 0;

        for (String num : nums6){
            num = num.trim(); // 숫자 문자 공백 제거
            int int_num = Integer.parseInt(num); // 정수 변환
            sum6 += int_num;
        }
        System.out.printf("총합 : %d\n", sum6);
        

        // 7. abc.txt파일을 읽어 역순으로 result.txt에 저장하기
        
        BufferedReader br7 = new BufferedReader(new FileReader("abc.txt"));
        ArrayList<String> words = new ArrayList<>();
        // 읽기
        while (true){
            String word = br7.readLine();
            if (word == null) break;
            words.add(word);
        }
        br7.close();

        // 역순 정렬
        words.sort(Comparator.reverseOrder());

        // 쓰기
        PrintWriter pw7 = new PrintWriter("result.txt");
        for (String word : words) {
            pw7.write(word+"\n");
        }
        pw7.close();
        


        // 8. 파일을 읽어 평균 값 저장하기
        BufferedReader br8 = new BufferedReader(new FileReader("sample.txt"));
        int count = 0 ; 
        int sum8 = 0;

        while (true) {
            String line8 = br8.readLine();
            if (line8 == null) break;
            int num8 = Integer.parseInt(line8);
            count++;
            sum8 += num8;
        }
        br8.close();

        double avg = sum8 / count;

        // 총합과 평균 쓰기
        PrintWriter pw8 = new PrintWriter("result2.txt");
        pw8.write(String.format("=== sum : %d, average : %.3f===", sum, avg));
        pw8.close();
    }
}
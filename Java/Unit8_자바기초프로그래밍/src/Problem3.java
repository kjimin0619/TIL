// 양의 정수를 입력받아 자릿수 출력하는 프로그램 작성
import java.util.Scanner;

public class Problem3 {
    static int getDigitCount(int n){
        int count = 0;
        while (true){
            if (n == 0){
                break;
            }
            n = n / 10;
            count++;
        }
        return count;
    }
    // 더 간단한게 자릿수 세는 법 : 문자열로 전환 후 길에 반환
    static int getDigitCount2(int n){
        String s = n+"";
        return s.length();
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        System.out.println(getDigitCount2(input));
    }
}

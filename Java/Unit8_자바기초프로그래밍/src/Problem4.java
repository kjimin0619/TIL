// 공백을 제외한 글자수 세기
import java.util.Scanner;

public class Problem4 {
    static int getCharCount(String s){
        int count = 0;
        for (int i = 0 ; i < s.length() ; i++){
            if (s.charAt(i) != ' ') {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args){
        System.out.print("문자열을 입력하세요 : ");
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine(); // 줄 단위 사용자 입력

        System.out.println("공백을 제외한 문자열의 길이 : " +getCharCount(s));
    }
}

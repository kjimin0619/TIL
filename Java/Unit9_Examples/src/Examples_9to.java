import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.HashMap;
import java.util.Random;

class calculator {
    int[] data = new int[5];

    public calculator(int[] data) {
        this.data = data;
    }

    public int sum() {
        return Arrays.stream(data).sum();
    }

    public float avg() {
        return sum()/data.length;
    }
}

class OddException extends Exception{
}

public class Examples_9to {
    static void execute(int n) throws OddException {
        System.out.printf("입력숫자 : %d\n", n);
        if (n % 2 == 1) {
            throw new OddException();
        }
        System.out.println("짝수입니다");
    }
    static String Dashinsert(String s){
        int[] numbers = Arrays.stream(s.split(""))
                .mapToInt(Integer::parseInt)
                .toArray();
        ArrayList<String> results = new ArrayList<>();

        for (int i = 0 ; i<numbers.length ; i++){
            results.add(numbers[i]+"");
            if (i < numbers.length - 1) { // 다음 수가 있다면
                boolean isOdd = numbers[i] % 2 != 0; // 홀수면 1
                boolean isNextOdd = numbers[i+1] % 2 != 0;
    
                // 홀수 연속
                if (isOdd && isNextOdd) {
                    results.add("-");
                }
    
                // 짝수 연속
                if (!(isOdd || isNextOdd)) {
                    results.add("*");
    
                }
            }
        }
        return String.join("",results);
    }

    static String strCount(String data){
        int count = 0;
        String standard = "";

        String result = "";

        for (String s : data.split("")){
            if (!s.equals(standard)){
                standard = s;

                // 이전 문자 처리
                if (count > 0) {
                    result += ""+count;
                }

                // 새로운 문자 처리
                result += s;
                count = 1;

            } else {
                count++;
            }
        }
        if (count > 0){
            result += count;
        }
        return result;
    }

    static boolean duplicateNums(String s){
        ArrayList<String> result = new ArrayList<>();
        for (String c : s.split("")){
            if (result.contains(c)) return false;
            else {
                result.add(c);
            }
        }
        return result.size() == 10;
    }

    static String caesar(String word, int n){
        String A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        ArrayList<String> re = new ArrayList<>();

        for (String c : word.split("")){
            int pos = A.indexOf(c);
            int newPos = pos + n;
            newPos = newPos % 26; // 26자리가 넘어가는 경우
            re.add(A.substring(newPos, newPos+1));
        }
        return String.join("", re);

    }

    static String mosRead(String mos) {
        HashMap<String, String> info = new HashMap<>() {{
            put(".-", "A");
            put("-...", "B");
            put("-.-.", "C");
            put("-..", "D");
            put(".", "E");
            put("..-.", "F");
            put("--.", "G");
            put("....", "H");
            put("..", "I");
            put(".---", "J");
            put("-.-", "K");
            put(".-..", "L");
            put("--", "M");
            put("-.", "N");
            put("---", "O");
            put(".--.", "P");
            put("--.-", "Q");
            put(".-.", "R");
            put("...", "S");
            put("-", "T");
            put("..-", "U");
            put("...-", "V");
            put(".--", "W");
            put("-..-", "X");
            put("-.--", "Y");
            put("--..", "Z");
        }};

        String result = "";
        // space 2개 기준 구분
        for (String word : mos.split("  ")){
            // space 1개 기준 구분
            for (String c : word.split(" ")){
                result = result + info.get(c);
            }
            result = result + " "; // 단어 사이 공백
     
        }
        return result;
    }

    public static void main(String args[]){
        // 9. calculator 클래스 작성하기
        int[] data1 = {1,2,3,4,5};
        calculator ca = new calculator(data1);
        System.out.printf("평균 : %.2f\n", ca.avg());
        System.out.printf("합계 : %d\n\n", ca.sum());
        
        // 10. 오류에 상관없이 모두 수행하기
        Random r = new Random();
            for (int i = 0 ; i < 10 ; i++){
                try {
                    execute(r.nextInt(20));
                } catch (OddException e) {
                    e.printStackTrace();
                }   
            }
        
        // 11. dashinsert
        // System.out.println("11. DashInsert");
        // Scanner sc11 = new Scanner(System.in);
        // String in11 = sc11.nextLine();
        String result = Dashinsert("5588");
        System.out.println(result);

        // 12. 문자열 압축
        String in12 = "aaabbcccccca";
        System.out.println(strCount(in12));

        // 13. duplicate Numbers
        System.out.println(duplicateNums("0123456789"));
        System.out.println(duplicateNums("01234567893"));
        
        // 14. 모스 부호 해독
        System.out.println(mosRead(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"));

        // 15. 시저암호
        // ABCDEFGHIJKLMNOPQRSTOW
        System.out.println(caesar("CAT", 5));
        System.out.println(caesar("XYZ", 3));

    
    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator; 
import java.util.HashMap;
import java.util.HashSet;


public class Unit3_Datatype {
    enum CoffeeType {
        AMERICANO,
        ICE_AMERICANO,
        CAFE_LATTE
    } // 상수 집합 정의

    static public void main(String args[]){
        System.out.println("3. data type");
        /*
         * <정수>
         * int, long(더 넓은 범위)
         * long 자료형 사용시, 숫자뒤(접미사)에 L을 붙인다
         * <실수>
         * float, double(자바 디폴트)
         * float 사용시, 숫자뒤 F 붙이기
         * <8진수, 16진수> : int 자료형 사용
         * 8진수 : 0으로 시작 ex. 023(십진수 19)
         * 16진수 : 0x로 시작 ex. 0xC(십진수 12)
         * <문자> 
         * char : 한 개의 문자 값에 대한 자료형. '' 사용
         * ---------- 여기까지 원시자료형(new 키워드로 값 생성 불가)
         * 원시 자료형 Wrapper 클래스 : Wrapper 클래스를 사용하면 값 대신 객체를 주고 받을 수 있어 객체 중심 프로그래밍 가능
         * 또한 멀티스레딩 환경에서 동기화 지원
         * Integer, Long, Double, Float, Boolean, Char
         * 
         * <문자열>
         * 리터럴 표기 : Strig a = "blabla"
         * 객체 표기 : String a = new String("blabla")
         * string 자료형은 한번 값이 생성되면 그 값을 변경할 수 없음.
         * String Buffer는 String 자료형보다 무겁지만 객체는 한 번만 생성하면 됨.
         * 문자열 작업이 많을 때 : StringBuffer
         * 문자열 작업이 많고 동기화를 고려할 때 : StringBuilder
         * 문자열 작업이 많지는 않을 때 : String 
         * 
         * <Map> == 파이썬 딕셔너리
         * Associative array, Hash라고도 불림
         * key, value를 한쌍으로 갖는 자료형
         */ 

    
        long countOfStar = 1234565777777L;
        System.out.println(countOfStar);

         // 증감 연산 : i++(참조 후 증가), ++i(참조 전 증가)
        int i = 0;
        i++;
        System.out.println(i); // 1
        System.out.println(i++); // 1
        System.out.println(i); // 2
        System.out.println(++i); // 3

         // 부울 연산
        boolean isTall;
        int base = 180;
        int height = 190;

        isTall = height > base; // true
        if (isTall){
            System.out.println("tall!");
        }

        // 문자열 내장 메서드
        String a = "Hello Java";
        String b = "Hello";

        // 두 문자열이 같나?(객체 비교는 ==, 문자열 값 비교는 equals)
        System.out.println(a.equals(b)); // false

        // 특정 문자열이 시작되는 위치 리턴
        System.out.println(a.indexOf('e')); // 1 

        // 특정 문자열 포함 여부 리턴
        System.out.println(a.contains("Java")); // true

        // 특정 위치 문자열 리턴
        System.out.println(a.charAt(6)); // 'J' 
        
        // 특정 문자열 다른 문자열로 변경       
        System.out.println(a.replaceAll("Java","World"));  // Hello World

        // 문자열 특정 부분 뽑아내기
        System.out.println(a.substring(0,4)); // Hell
        
        // 대문자 변경(소문자는 toLowerCase)
        System.out.println(a.toUpperCase()); // HELLO JAVA

        // 구분자로 나누기
        String c = "a:b:c:d";
        String[] result = c.split(":");
        ArrayList<String> test = new ArrayList<>(Arrays.asList(result));
        System.out.println(test);
        System.out.println(result[0] + result[1] + result[2] + result[3]);


        // 문자열 포매팅 : %s 자동 포맷팅
        // String.format : 포매팅된 문자열 리턴
        // System.out.printf : 문자열 출력 메서드
        System.out.println(String.format("I eat %s apples", 3.2578));
        System.out.println(String.format("print : %10.4f", 3.145156));
        System.out.printf("print : %10.4f", 1.2666678);
        System.out.println(" ");

        // StringBuffer
        StringBuffer sb = new StringBuffer();
        sb.append("hello");
        sb.append("  ");
        sb.append("jump");

        sb.insert(0, "hmm,,"); // 문자열 삽입
        
        String re  = sb.toString();
        System.out.println(re);

        System.out.println(sb.substring(0,6));

        // 배열 : 길이 고정
        String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
        for (int j = 0 ; j < weeks.length ; j++){
            System.out.println(weeks[j]);
        }
        String joinTest = String.join("::", weeks);
        System.out.println(joinTest);

        // 리스트 : 크기 고정 X ; 동적으로 자료형의 갯수가 변하는 상황
        // generics 표기
        ArrayList<String> pitches = new ArrayList<>();
        pitches.add("138");
        pitches.add("129");
        pitches.add("139400");

        System.out.println(pitches.get(1)); // get
        System.out.println(pitches.size()); // 갯수
        System.out.println(pitches.contains("129")); // 포함 여부
        System.out.println(pitches.remove("139400"));

        System.out.println(pitches); // [138, 129]
        pitches.add("486");

        // String.join
        String result3 = String.join("!!", pitches);
        System.out.println(result3); // 138!!129!!486

        // 정렬 * 내림차순 정렬 : reverseOrder()
        pitches.sort(Comparator.naturalOrder());
        System.out.println(pitches);

        // map (순서 없음)
        // HashMap
        HashMap<String, String> hashMapTest = new HashMap<>();
        hashMapTest.put("people", "사람");
        hashMapTest.put("baseball","야구");
        System.out.println(hashMapTest.get("people")); // 사람
        System.out.println(hashMapTest.getOrDefault("java", "자바"));
       
        System.out.println(hashMapTest.containsKey("java")); // false
        System.out.println(hashMapTest.remove("people")); // 사람 출력 & 키,값 쌍 삭제
        System.out.println(hashMapTest.size()); // 1
        
        hashMapTest.put("jimin", "지민");
        System.out.println(hashMapTest.keySet()); // [jimin, baseball] 출력
        
        ArrayList<String> keyList = new ArrayList<>(hashMapTest.keySet());
        System.out.println(keyList);

        // Set
        // 중복 금지, 순서 없음(인덱싱 불가)
        HashSet<String> set = new HashSet<>(Arrays.asList("H","e","l","l","o"));
        System.out.println(set);

        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1,2,3,4,5));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4,5,6,7,8,9));
       
        // 교집합
        HashSet<Integer> intersection = new HashSet<>(s1);
        intersection.retainAll(s2); // 교집합 수행
        System.out.println(intersection); // [4,5]
        
        // 합집합
        HashSet<Integer> union = new HashSet<>(s1);
        union.addAll(s2);
        System.out.println(union);

        // 차집합
        HashSet<Integer> substract = new HashSet<>(s1);
        substract.removeAll(s2);
        System.out.println(substract);

        // 집합 자료형 관련 메서드
        set.add("Jump");
        set.add("To");
        set.addAll(Arrays.asList("Hello","Hi","This"));
        
        set.remove("To");
        System.out.println(set);

        // 형변환
        // string to int/double
        String n1 = "1234";
        int ni = Integer.parseInt(n1);

        String n2 = "123.456";
        double nf = Double.parseDouble(n2);
        
        System.out.println(ni); // 1234
        System.out.println(nf);

        // int to string
        int nn = 1234;
        String ver1 = "" + nn;
        String ver2 = String.valueOf(nn);
        String ver3 = Integer.toString(nn);

        System.out.println(ver1);
        System.out.println(ver2);
        System.out.println(ver3);

        // final : 값 변경 불가능한 변수 제작
        final int finalTest = 123;
        // finalTest = 456 // error 발생
        


    }
}

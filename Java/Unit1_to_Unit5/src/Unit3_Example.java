import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;


public class Unit3_Example {
    enum CoffeeType{
        AMERICANO,
        ICE_AMERICANO,
        CAFE_LATTE
    }

    static String printCoffeePrice(CoffeeType type){
        HashMap<CoffeeType, Integer> priceMap = new HashMap<>();

        priceMap.put(CoffeeType.AMERICANO, 3000);
        priceMap.put(CoffeeType.CAFE_LATTE, 4000);
        priceMap.put(CoffeeType.ICE_AMERICANO, 5000);

        int price = priceMap.get(type);
        
        return price + "원";
    }

    static public void main(String[] args){
        // 1. 평균 점수 구하기
        int korean = 80;
        int english = 75;
        int math = 55;
        double average = (korean + english + math) / 3;
        System.out.println("#1 평균점수 : " + average);
    
        // 2. 홀짝 판별
        int num = 13;
        if (num % 2 == 0) {
            System.out.println("#2 홀짝 판별 : 짝수");
        }
        else {
            System.out.println("#2 홀짝 판별 : 홀수");
        }

        // 3. 주민등록번호 나누기
        String number = "881120-1068234";
        String[] splitResult = number.split("-");
        String birth = splitResult[0];
        String ownNum = splitResult[1];
        System.out.println("#3 주민번호 분할 : " + birth + "\n" + ownNum);

        // 4. 주민등록번호 인덱싱
        char pin = number.charAt(7);
        System.out.println("#4 주민번호 인덱싱 : " + pin);

        // 5. 문자열 바꾸기
        String a = "a:b:c:d";
        System.out.println("#5 문자열 바꾸기 : " + a.replaceAll(":","#"));

        // 6. 리스트 역순 정렬
        ArrayList<Integer> myList = new ArrayList<>(Arrays.asList(1,3,5,4,2));
        myList.sort(Comparator.reverseOrder()); 
        System.out.println("#6 리스트 역순 정렬 : " + myList);

        // 7. 리스트를 문자열로 만들기
        ArrayList<String> myList7 = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
        String answer7 = String.join(" ", myList7);
        System.out.println("#7 리스트를 문자열로 변환 : " + answer7);

        // 8. map 에서 값 추출
        HashMap<String, Integer> myMap = new HashMap<>();
        myMap.put("a", 90);
        myMap.put("b", 80);
        myMap.put("c", 70);
        System.out.println("#8. 맵에서 값 추출하기 : " + myMap.remove("b") + "  | 남은 map : " + myMap);

        // 9. 중복 숫자 제거하기
        ArrayList<Integer> myList9 = new ArrayList<>(Arrays.asList(1,1,1,2,2,3,3,3,4,4,5,5));
        HashSet<Integer> result9 = new HashSet<>(myList9); // List to Set
        System.out.println("#9. 중복 숫자 제거 : " + result9);

        // 10. 매직넘버 제거
        System.out.println("#10. 매직넘버 제거 : " + printCoffeePrice(CoffeeType.AMERICANO)); 
        






    }
}

import java.util.function.BiFunction; // 더 더 축약해주는 인터페이스
import java.util.function.BinaryOperator; // 입출력 데이터타입 동일

// 함수형 인터페이스 사용 : 2개 이상 메서드 구현 불가
@FunctionalInterface
interface Calculator {
    int sum(int a, int b);
}

public class FunctionalPG {
    public static void main(String[] args){
        Calculator mc = (a,b) -> a+b ;
        int result = mc.sum(3,4);
        System.out.println(result);

        // 더 축약하는 버전
        // 두 수를 더하여 결과 리턴하는 함수 (a,b) -> a+b 는
        // Integer.sum(int a, int b) 와 동일
        Calculator mc2 = Integer::sum;
        int result2 = mc2.sum(3,4);
        System.out.println(result2);

        // 더 더 축약하는 버전(곱셈으로 변경) ; BiFuncrion 인터페이스 사용
        // BiFunction<입력, 입력, 출력>
        BiFunction<Integer, Integer, Integer> bmc = (a,b) -> a*b;
        int bmcResult = bmc.apply(3,4);
        System.out.println(bmcResult);
        
        // 더 더 더 축약하는 버전 ; 입출력 항목이 동일한 경우 BinaryOperator
        BinaryOperator<Integer> bomc = (a, b) -> a*b;
        int bomcResult = bomc.apply(3,4);
        System.out.println(bomcResult);
    }
}
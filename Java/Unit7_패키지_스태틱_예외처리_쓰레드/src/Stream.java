import java.util.Arrays;
import java.util.Comparator;

class Stream {
    public static void main(String[] args){
        /*
         * 스트림 : 흐름
         */

         // 정수 배열에서 짝수만 뽑아 중복을 제거하고 역순으로 정렬
         int[] data = {5,6,4,2,3,1,1,2,2,4,8};
         int[] result = Arrays.stream(data) // intStream 생성
            .boxed() // IntStream을 Integer의 Stream으로 변경
            .filter((a) -> a % 2 == 0) // 짝수만 필터링
            .distinct() // 중복 제거
            .sorted(Comparator.reverseOrder()) // 역순 정렬
            .mapToInt(Integer::intValue) // Integer의 Stream을 IntStream으로 변경
            .toArray() // int[] 배열 리턴
            ;
            
        for (int r : result) {
            System.out.print(r+" ");
        }

    }
}
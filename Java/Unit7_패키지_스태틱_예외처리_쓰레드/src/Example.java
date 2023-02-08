import java.util.ArrayList;
import java.util.Arrays;

class HeavyWork implements Runnable{
    String name;

    HeavyWork(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        work();
    }
    public void work(){
        try {
            Thread.sleep(100); // 0.1초 대기
        } catch(Exception e){

        }

        System.out.printf("%s done \n", this.name);
    }
}

public class Example {
    public static void main (String[] args){
        // 1. 패키지 오류 수정 : import house.HousePark으로 변경

        // 2. 예외 처리 : 인덱스 에러 +3, finally +4 == 7

        // 3. 스레드 적용 : 
        long start = System.currentTimeMillis();    
        ArrayList<Thread> thrds = new ArrayList<>();

        for (int i = 1 ; i < 5 ; i++){
            Thread t = new Thread(new HeavyWork("w" + i));
            t.start();
            thrds.add(t);
        }

        for (Thread t : thrds){
            try {
                t.join(); // 스레드 종료까지 대기
            } catch(Exception e){}
        }

        long end = System.currentTimeMillis();
        System.out.printf("elapsed time : %s ms\n", end - start);

        // 4. 홀수에만 2를 곱하여 리턴
        int[] data = {1,2,3,4,5};
        int[] result = Arrays.stream(data) // intStream 생성
        .filter((a) -> a % 2 != 0) // 홀수 필터링
        .map((a) -> a * 2)
        .toArray() // int[] 배열로 리턴
        ;

        // 5. 음수 제거
        int[] numbers = {1, -2, 3, -5, 8, -3};
        int[] result2 = Arrays.stream(numbers)
        .filter((a) -> a >= 0)
        .toArray();
    }
}
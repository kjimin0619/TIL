package house;

class Counter {
    // static 키워드 : 공유 변수 제작. 메모리 할당을 한 번만 하게 됨. 
    // final 키워드 : 변경 불가능한 변수 제작
    static int count = 0;
    // 생성자
    Counter() {
        count++;
        System.out.println(count);
    }

    // static 메서드
    public static int getCount() {
        return count;
    }
}

public class Sample {
    // 접근 제어자 : private -> default(패키지 내 접근 가능) -> protected -> public
    public static void main(String[] args){
        HousePark hp = new HousePark();
        System.out.println(hp.info);

        // static
        Counter c1 = new Counter(); // 1
        Counter c2 = new Counter(); // 2

        System.out.println(Counter.getCount()); // 2

    }

   
    
}



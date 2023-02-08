interface Mineral {  
    int GetAdd();
}
class Gold implements Mineral {
    public int GetAdd() {
        return 100;
    }
    
}
class Silver implements Mineral {
    public int GetAdd() {
        return 90;
    }
}
class MineralCalculator {
    int value = 0;

    public void add (Mineral mineral){
        this.value += mineral.GetAdd();
    }

    public int getValue() {
        return this.value;
    }
}

public class Unit5_Example2 {
    public static void main(String[] args){
        MineralCalculator mcal = new MineralCalculator();
        mcal.add(new Gold());
        mcal.add(new Silver());

        System.out.println(mcal.getValue());
    }
}

// 6 : 초기값 지정 안 해줌. Integer value = 0; 으로 초기화 필요
/* 8. : 4번 오류. 자식 클래스 자료형의 변수가 부모 클래스 자료형을 호출할 순 없음
 * 9. : 2 5번 오류. 자료형이 제공하는 메서드만 사용 가능
 */
import java.util.ArrayList;
import java.util.Arrays;

class Calculator {
    int value;

    Calculator() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    int getValue() {
        return this.value;
    }

    boolean isOdd(int n){
        return n%2==1;
    }

    int avg(ArrayList<Integer> a){
        int sum = 0;
        for (int num : a) {
            sum = sum + num;
        }
        return sum/a.size();
    }

    int avg(int[] a){
        int sum = 0;
        for (int num : a) {
            sum = sum + num;
        }
        return sum/a.length;
    }

}

class UpgradeCalculator extends Calculator {
    void minus(int a){
        this.value -= a ; 
    }
}

class MaxLimitCalculator extends Calculator {
    void add(int val){
        this.value += val;
        if (this.value > 100){
            this.value = 100;
        }
    }
}

public class Unit5_Example {
    public static void main(String args[]){
        // upgradeCalculator
        UpgradeCalculator cal = new UpgradeCalculator();
        cal.add(10);
        cal.minus(3);
        System.out.println(cal.getValue());  // 10에서 7을 뺀 3을 출력
        
        // MaxLinitCalculator
        MaxLimitCalculator cal2 = new MaxLimitCalculator();
        cal2.add(50);
        cal2.add(60);
        System.out.println(cal2.getValue());
    
        System.out.println(cal.isOdd(3));

        // average 
        int[] data = {1, 3, 5, 7, 9};
        Calculator cal3 = new Calculator();
        int result = cal3.avg(data);
        System.out.println(result);

        ArrayList<Integer> data2 = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9));
        Calculator cal4 = new Calculator();
        int result2 = cal4.avg(data2);
        System.out.println(result2);

    }
}

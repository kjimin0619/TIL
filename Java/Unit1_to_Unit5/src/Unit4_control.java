import java.util.ArrayList;

public class Unit4_control {
    static public void main(String args[]) {
        boolean money = true;
        if (money) {
            System.out.println("taxi");
        }

        ArrayList<String> pocket = new ArrayList<>();
        pocket.add("paper");
        pocket.add("handphone");

        if (pocket.contains("paper")) {
            System.out.println("paper");
        } else {
            System.out.println("no paper");
        }

        int month = 8;
        String monStr = " ";
        switch(month){
            case 1: monStr = "January";
                    break;
            case 2: monStr = "February";
                    break;
            case 8: monStr = "August";
                    break;
        }
        System.out.println(monStr);

        int treeHit = 0;
        while (treeHit < 10){
            treeHit++;
            System.out.println("tree : "+treeHit);
            if (treeHit == 10){
                System.out.println("나무 넘어감");
            }
        }

        // continue
        // print odd number in 1 ~ 10
        int a = 0;
        while (a < 10){
            a++;
            if (a%2 ==0){
                continue;
            }
            System.out.println(a);
        }

        // for
        String[] numbers = {"one", "two", "three"};
        for (int i = 0 ; i < numbers.length ; i++) {
            System.out.println(numbers[i]);
        }

        // for each ---> for (type var : iterate). iterate : 루프를 돌릴 객체
        for (String number : numbers) {
            System.out.print(number+" ");
        }

    }
}
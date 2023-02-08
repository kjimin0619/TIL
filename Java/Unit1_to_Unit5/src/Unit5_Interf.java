interface Predator {
    // 인터페이스는 인터페이스의 메서드를 반드시 구현
    // 메서드 구현의 "강제성"을 갖는 것 == 인터페이스
    String getFood();

    // default method
    default void printFood() {
        System.out.printf("my food is %s\n",getFood());
    }

    // 인터페이스 상수
    int LEG_COUNT = 4;

    static int speed(){
        return LEG_COUNT*30;
    }
}

interface Barkable{
    void bark();
}

// 인터페이스는 다중 상속 가능
interface BarkablePredator extends Predator, Barkable {

}

class Animal {
    String name = "no name";

    // method
    public void setName(String name){
        this.name = name;
    }
}


class Tiger extends Animal implements BarkablePredator {
    public String getFood() {
        return "apple";
    }

    public void bark(){
        System.out.println("어흥");
    }
}

class Lion extends Animal implements BarkablePredator {
    public String getFood(){
        return "banana";
    }
    public void bark(){
        System.out.println("으르렁");
    }
}

class ZooKeeper {
    void feed(Predator predator){
        System.out.println("feed!" + predator.getFood());
    }
}

class Bouncer {
    void barkAnimal(Barkable animal) {
        animal.bark();
    }
}

public class Unit5_Interf {
    public static void main(String args[]){
        ZooKeeper keeper = new ZooKeeper();
        Lion lion = new Lion();
        Tiger tiger = new Tiger();

        lion.printFood();
        keeper.feed(lion);
        keeper.feed(tiger);

        Bouncer b = new Bouncer();
        b.barkAnimal(tiger);

        System.out.println(Predator.speed());

        // polymorphism 다형성
        Tiger tiger2 = new Tiger();
        Animal animal2 = new Tiger();
        Predator predator2 = new Tiger();
        Barkable barkable2 = new Tiger();

    }
}

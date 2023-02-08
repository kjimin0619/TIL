class Animal {
    String name = "no name";

    // method
    public void setName(String name){
        this.name = name;
    }

    public void getName(){
        System.out.println(this.name);
    }
}

// is-a 관계 : 상속 가능
class Cow extends Animal {
    void makeMilk(){
        System.out.println("make milk!");
    }

    void sleep(){
        System.out.println(this.name + " sleep zz");
    }
}   

class HouseCow extends Cow {
    // constructor (생성자)
    // 클래스명과 이름이 동일하고, 리턴자료형을 정의하는 않는 메서드
    // 객체 생성될 때 호출
    HouseCow(String name){
        this.setName(name);
    }

    // 생성자 오버로딩
    HouseCow(int a){
        if (a == 1){
            this.setName("one");
        }else {
            this.setName("not one");
        }
    }

    // method overriding
    void makeMilk() {
        System.out.println("we cannot make milk..");
    }

    // method overloading
    void makeMilk(int a) {
        System.out.println("we make milk "+a+"ml!");
    }
}

class Updater {
    void update_cv(int count){ 
        count++; // call by value
    }

    void update_cr(Counter count){
        count.count++; // call by reference
    }
}

class Counter {
    int count = 0;
}

public class Sample {
    public static void main(String[] args){
        Animal cat = new Animal(); // cat은 인스턴스
        Animal dog = new Animal();
        dog.setName("Kung");
        cat.setName("Mew");

        cat.getName();
        dog.getName();

        Cow myCow = new Cow();
        myCow.makeMilk();
        myCow.setName("happy");
        myCow.sleep();


        HouseCow hCow = new HouseCow("coco");
        hCow.makeMilk(); // overriding
        hCow.makeMilk(100); // overloading

        HouseCow hCow2 = new HouseCow(3);
    
        System.out.println(hCow.name);
        System.out.println(hCow2.name);

        System.out.println();
        // call by value vs call by reference
        Counter myCounter = new Counter();
        Updater myUpdater = new Updater();
        System.out.println("before update:"+myCounter.count);
        
        myUpdater.update_cv(myCounter.count);
        System.out.println("after call by value update:"+myCounter.count);
        
        myUpdater.update_cr(myCounter);
        System.out.println("after call by reference update:"+myCounter.count);
    }
}

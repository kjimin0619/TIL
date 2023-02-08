class Singleton {
    private static Singleton one;
    // 생성자 private
    private Singleton() {
    }

    public static Singleton getInstace() {
        if (one==null){
            one = new Singleton();
        }
        return one;
    }
}



public class SingletonPattern {
    public static void main(String[] args) {
        Singleton singleton1 = Singleton.getInstace();
        Singleton singleton2 = Singleton.getInstace();
        System.out.println(singleton1 == singleton2); // true
    }
    
}

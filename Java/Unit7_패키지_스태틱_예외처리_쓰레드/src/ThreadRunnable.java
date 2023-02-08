import java.util.ArrayList;


public class ThreadRunnable implements Runnable {
    int seq;
    public ThreadRunnable(int a){
        this.seq = a;
    }

    public void run(){
        System.out.println(this.seq + " thread start.");
        try {
            Thread.sleep(1000);
        } catch(Exception e) {}

        System.out.println(this.seq + " thread end.");
    }

    public static void main(String[] args){
        ArrayList<Thread> trds = new ArrayList<>();

        for (int i = 0 ; i < 10 ; i ++){
            Thread t = new Thread(new ThreadRunnable(i));
            t.start();
            trds.add(t);
        }

        for (int i = 0 ; i < trds.size() ; i ++){
            Thread t = trds.get(i);
            try {
                t.join();
            } catch(Exception e){}
        }

        System.out.println("== main end ==");
    }
}

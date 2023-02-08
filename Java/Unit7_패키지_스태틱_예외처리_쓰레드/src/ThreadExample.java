import java.util.ArrayList;

public class ThreadExample extends Thread {
    int seq;

    public ThreadExample(int seq){
        this.seq = seq;
    }
    
    public void run() { // 쓰레드 상속시 run 구현
        System.out.println(this.seq + " thread run.");
        try {
            Thread.sleep(1500); // 1.5초 대기
        } catch(Exception e){
        }
        System.out.println(this.seq+" thread end");
    }

    public static void main(String[] args){
        ArrayList<Thread> threads = new ArrayList<>();
        
        for (int i = 0 ; i < 10 ; i++){
            Thread t = new ThreadExample(i);
            t.start();
            threads.add(t); // 생성된 쓰레드 객체 리스트에 저장
        }

        for (int i = 0 ; i<threads.size() ; i++){
            Thread t = threads.get(i);
            try{
                t.join(); // 쓰레드가 종료할 때까지 메인 대기
            }catch(Exception e){}
        }

        System.out.println("== main end =="); // main 종료
    }
}

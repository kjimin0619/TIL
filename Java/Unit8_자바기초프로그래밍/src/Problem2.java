// 게시판 페이징
public class Problem2 {
    static int getTotalPage(int m, int n){
        if (m % n == 0){
            return  m / n;
        } else {
            return m / n + 1;
        }
    }
    public static void main(String[] args){
        System.out.println(getTotalPage(30,10));
    }
}

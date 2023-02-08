class FoolException extends Exception {
}

public class ExceptionTest {
    public void sayNick(String nick) throws FoolException {
        if("fool".equals(nick)) {
            throw new FoolException();
        }
        System.out.println("당신의 별명은 "+nick+" 입니다.");
    }

    public static void main(String[] args){
        int c;

        try {
            c = 4/0;
        } catch(ArithmeticException e){
            System.out.println("!!error!! : " + e);
            c = -1;
        } finally {
            System.out.println("반드시 실행");
        }

        System.out.println(c);

        ExceptionTest ex = new ExceptionTest();
        
        
        try {
            ex.sayNick("fool");
            ex.sayNick("genius");
        } catch (FoolException e){
            System.err.println("foolexception 발생");
        }
    }
}

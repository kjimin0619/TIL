import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.PrintWriter;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;

public class IO {
    public static void main(String[] args) throws IOException {
        InputStream in = System.in; // byte
        InputStreamReader reader = new InputStreamReader(in); // character
        BufferedReader br = new BufferedReader(reader); // String

        String a = br.readLine();
        System.out.println(a);

        Scanner sc = new Scanner(System.in);
        System.out.println(sc.next()); // next, nextLine, nextInt
        
        // 파일 입출력
        FileOutputStream output = new FileOutputStream("c:/자반연습용지워도됨.txt");
        // 파일쓰기 ; FileOutputStream 사용 버전
        for (int i = 1 ; i < 11 ; i++){
            String data = i + "번 \r\n";
            output.write(data.getBytes());
        }
       
        // 파일쓰기 ; FileWriter 사용 버전
        FileWriter fw = new FileWriter("c:/writer.txt");
        for (int i = 1 ; i < 11 ; i++) {
            String data = i + "line! \r\n";
            fw.write(data);
        }

        // 파일쓰기 ; PrintWriter 사용 버전. 일일이 \r\n 붙이지 않아도 됨
        PrintWriter pw = new PrintWriter("c:/pw.txt");
        for (int i = 0 ; i < 11 ; i++) {
            String d = i + "번째";
            pw.println(d);
        }

        output.close();
        fw.close();
        pw.close();

        // 파일쓰기 추가
        FileWriter fw2 = new FileWriter("c:/writer.txt", true);
        for (int i = 0 ; i < 3 ; i++){
            String data = "추가 \r\n";
            fw2.write(data);
        }
        fw2.close();

        // 파일 읽기(바이트 배열 이용)
        byte[] b = new byte[1024];
        FileInputStream ip = new FileInputStream("c:/writer.txt");
        ip.read(b);
        System.out.println(new String(b));
        ip.close();

        // 파일 읽기(라인 단위)
        System.out.println("===============");
        BufferedReader br2 = new BufferedReader(new FileReader("c:/writer.txt"));
        while(true) {
            String line = br2.readLine();
            if (line == null) {
                break;
            }
            System.out.println(line);
        }
        br2.close();
    }
}

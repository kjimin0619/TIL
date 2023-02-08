import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Scanner;

import java.io.IOException;
import java.util.ArrayList;

import java.io.FileWriter;

public class Example {
    public static void main(String[] args) throws IOException{
       
        // 1 정수 합 구하기
        // int a = 0;
        // int b = 0;
        // Scanner intScanner = new Scanner(System.in);
        // System.out.print("enter number 1 : ");
        // a = intScanner.nextInt();
        // System.out.print("enter number 2 : ");
        // b = intScanner.nextInt();

        // System.out.println("sum : " + (a+b));

        // 2 대문자 변환기
        // String input = " ";
        // while (!(input.equals("END"))){
        //     Scanner sc = new Scanner(System.in);
        //     input = sc.next();
        //     input = input.toUpperCase();
        //     System.out.println(input);
        // }

        // 3 오류 수정
        // FileWriter fw = new FileWriter("sample.txt");
        // fw.write("Write one, run anywhere");
        // fw.close();

        // BufferedReader bbr = new BufferedReader(new FileReader("sample.txt"));
        // String line = bbr.readLine();
        // System.out.println(line);
        // fw.close();
    
        // 4 사용자 입력파일 저장
        Scanner sc4 = new Scanner(System.in);
        FileWriter fw4 = new FileWriter("sample.txt", true);
        
        System.out.print("enter your words : ");
        String line = sc4.nextLine();
        fw4.write("\n"+line);
        fw4.close();
            
        // 5 파일 내용 바꾸어 저장
        BufferedReader br3 = new BufferedReader(new FileReader("sample.txt"));
        ArrayList<String> lines = new ArrayList<>();
        while (true) {
            String k = br3.readLine();
            if (k == null) break;
            lines.add(k);
        } 
        br3.close();

        System.out.println(lines);
        String text = String.join("\n", lines);
        text = text.replaceAll("python", "java");
       
        FileWriter fw5 = new FileWriter("sample.txt");
        fw5.write(text);
        fw5.close();
    }
}

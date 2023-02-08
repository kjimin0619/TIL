/**
 * 전문을 생성하고 파싱하는 프로그램
 * 전문 : 서로 약속한 규칙대로 주고받는 일반 텍스트 데이터
 * 파싱 : 전문을 길이대로 자르는 것
 */

 /*
  * 전문 규칙
  1. "이름+전화번호"를 보내면 응답 전문으로 "생일+주소"를 리턴한다
  2. "이름"은 20자리
  3. "전화번호"는 11자리

  4. "생일"은 8자리
  5. "주소"는 50자리
  */

// 전문에 필요한 요소
public class Item {
    // 속성 이름,값,길이
    private String name;
    private int length;
    private String value;

    // getter, setter 구현
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    // 전문 출력 (길이에 맞게 공백 포함)
    public String raw() {
        StringBuffer padded = new StringBuffer(this.value);
        
        // 자바는 한 모음,자음의 길이를 1로 계산
        // 따라서 바이트로 변환한 후 길이를 체크하는 것이 안전함
        while (padded.toString().getBytes().length < this.length) {
            padded.append(' ');
        }
        return padded.toString();
    }

    // 객체 생성 메서드
    public static Item create(String name, int length, String value){
        Item item = new Item();
        item.setLength(length);
        item.setName(name);
        item.setValue(value);
        return item;
    }

    public static void main(String[] args){
        Item item = new Item();
        item.setName("이름");
        item.setLength(20);
        item.setValue("홍길동");

        System.out.println("[" + item.raw() + "]");
    }
}


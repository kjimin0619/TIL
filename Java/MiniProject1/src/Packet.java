import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Packet {
    // 여러 개의 아이템을 포함
    private ArrayList<Item> items = new ArrayList<Item>();
    private HashMap<String, Item> nameAccess = new HashMap<>();

    public void addItem(Item item) {
        this.items.add(item);
        nameAccess.put(item.getName(), item);
    }

    public Item getItem(int index) {
        return nameAccess.get(name);
    }

    // packet 전문 출력
    public String raw() {
        StringBuffer result = new StringBuffer();
        for (Item item : items){
            result.append(item.raw());
        }
        return result.toString();
    }

    // 수신받은 전문(번호+주소) 파싱
    public void parse(String data){
        byte[] bdata = data.getBytes(); // 한글 데이터 가져오기
        System.out.println("파싱 시작 : " + Arrays.toString(bdata));
        
        int pos = 0;

        for (Item item : items){
            byte[] temp = new byte[item.getLength()];
            
            // arraycopy(소스, 소스시작위치, 대상, 대상시작위치, 복사할길이)
            System.arraycopy(bdata, pos, temp, 0, item.getLength()); // temp에 bdata 중 일부를 바이트만큼 옮겨 붙이기

            pos += item.getLength(); // 소스 시작위치 옮기기
            item.setValue(new String(temp)); // item의 value 멤버 값 설정
        }
    }

    public static void main(String[] args){
        // 송신할 전문
        Packet packet = new Packet();
        Item it1 = Item.create("이름", 20, "홍길동");
        Item it2 = Item.create("전화번호",11,"0109998888");

        packet.addItem(it1);
        packet.addItem(it2);
        System.out.println("["+packet.raw()+"]");
    
        // 수신반은 전문 
        Packet recvPacket = new Packet();
        recvPacket.addItem(Item.create("생일",8,null));
        recvPacket.addItem(Item.create("주소",50,null));
        
        recvPacket.parse("19801215서울시 송파구 잠실동 123-3");

        System.out.println(recvPacket.getItem(1).raw());



    
    }
}

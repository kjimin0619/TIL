import java.util.ArrayList;
import java.util.HashMap;

public class Packet {
    // 여러 개의 아이템을 포함
    private ArrayList<Item> items = new ArrayList<Item>();
    private HashMap<String, Item> nameAccess = new HashMap<String, Item>(); // key = 아이템이름, value = 아이템

    public void addItem(Item item) {
        this.items.add(item);
        // 동일한 이름으로 2개 이상의 아이템 항목 만들 수 없음
        if (nameAccess.containsKey(item.getName())) {
            throw new RuntimeException(
                "Duplicated item name : ["+item.getName()+"]"
            );
        }
        nameAccess.put(item.getName(), item);
    }

    public Item getItem(String name) {
        return nameAccess.get(name);
    }

    public Item getItem(int index) {
        return this.items.get(index);
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
    public void parse(String data) {
        byte[] bdata = data.getBytes();
        // System.out.println(bdata.length); // 58
        int pos = 0;
        // System.out.println(new String(bdata)); // 입력받은 data 값 출력

        for (Item item : items) {
            byte[] temp = new byte[item.getLength()];
            // (소스, 소스시작위치, 대상, 대상시작위치, 복사할 길이)
            System.arraycopy(bdata, pos, temp, 0, item.getLength());
            
            pos += item.getLength(); // 소스 시작위치 옮기기
            item.setValue(new String(temp)); // item의 value 멤버 값 업데이트
        }
    }

    public static void main(String[] args){
        // 송신할 전문
        Packet packet = new Packet();
        Item it1 = Item.create("이름", 20, "홍길동");
        Item it2 = Item.create("전화번호",11,"01099998888");

        packet.addItem(it1);
        packet.addItem(it2);
        System.out.println("["+packet.raw()+"]");
    
        // 수신한 전문 
        Packet recvPacket = new Packet();
        recvPacket.addItem(Item.create("생일", 8, null));
        recvPacket.addItem(Item.create("주소", 50, null));
        recvPacket.parse("19801215서울시 송파구 잠실동 123-3                        ");

        System.out.println(recvPacket.getItem("주소").raw());
        System.out.println(recvPacket.getItem("생일").raw());

    }
    
}

import junit.framework.TestCase;

public class SubdateTest extends TestCase {
    public static void main(String[] args) {
        junit.textui.TestRunner.run(SubdateTest.class);
    }

    // 테스트 코드
    // assertEquals(a,b) : a, b가 같은지 조사
    public void testGetYearDay() {
        assertEquals(0, SubDate.getYearDay(1));
        assertEquals(365, SubDate.getYearDay(2));

    }
    public void testLeapYear() {
        assertTrue(SubDate.isLeapYear(0));
        assertFalse(SubDate.isLeapYear(1));
        assertTrue(SubDate.isLeapYear(1200));
    }
    public void testGetMonthDay() {
        assertEquals(0, SubDate.getMonthDay(1, true));
        assertEquals(31, SubDate.getMonthDay(2, false));
        assertEquals(31+28, SubDate.getMonthDay(3, false));
    }
    public void testGetTotalDay(){
        assertEquals(1, SubDate.getTotalDay("00010101")); // 1
        assertEquals(366, SubDate.getTotalDay("00020101")); // 366
    }

    // 두 날짜의 차이 일자 구하기
    public void testSubDate() {
        assertEquals(1, SubDate.sub("20061231","20070101"));
    }
}
class SubDate {
    static final int[] monthDays = {
            31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };
    // 연도
    public static int getYearDay(int year) {
        int result = 0;
        for (int i = 1 ; i < year ; i++){
            if (isLeapYear(i)) result += 366;
            else result += 365;
        }
        return result;
    }

    // 윤년체크
    public static boolean isLeapYear(int year){
        if (year % 400 == 0) return true;
        if (year % 100 == 0) return false;
        if (year % 4 == 0) return true;
        return false;
    }

    // 월
    public static int getMonthDay(int month, boolean isLeap){
        int result = 0;
        for (int i = 1 ; i < month ; i++){
            result += monthDays[i-1];
        }

        if (isLeap && month >2) result += 1;
        return result;
    }

    // 합계
    public static int getTotalDay(String date) {
        int year = Integer.parseInt(date.substring(0,4));
        int month = Integer.parseInt(date.substring(4,6));
        int day = Integer.parseInt(date.substring(6,8));
        return getYearDay(year) + getMonthDay(month, isLeapYear(year)) + day;
    }

    // 차이
    public static int sub(String date1, String date2){
        return Math.abs(getTotalDay(date1) - getTotalDay(date2));
    }
}
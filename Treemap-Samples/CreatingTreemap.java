import java.util.TreeMap;

public class CreatingTreemap{
    public static void main(String args[]){
        TreeMap<Integer, String> myTreeMap = new TreeMap<>();

        myTreeMap.put(1, "DEF");
        myTreeMap.put(1, "DEF");
        myTreeMap.put(1, "DEF");

        System.out.println(myTreeMap);


    }
}
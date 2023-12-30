

import java.util.TreeMap;
import java.util.Comparator;

class CustomTreemap {
    public static void main(String[] args) {

    
        TreeMap<Integer, String> numbers = new TreeMap<>(new CustomComparator());

        numbers.put(1, "First");
        numbers.put(2, "Second");
        numbers.put(3, "Third");
        numbers.put(4, "Fourth");

        System.out.println("TreeMap: " + numbers);
    }


    public static class CustomComparator implements Comparator<Integer> {

        @Override
        public int compare(Integer number1, Integer number2) {
            if(number1>number2){
                return -1;
            }
            else if(number1==number2) return 0;
            else return 1;
        }
    }
}
 
import java.util.TreeMap;

public class TwoTreemap{
    public static String replaceFunction(String old){
        return old+"newValue";
    }
    public static void main(String[] args){
        TreeMap<Integer, String> tree = new TreeMap<>();
        tree.put(1, "abc");
        tree.put(4,"hii");
        tree.put(2,"wait");

        TreeMap<Integer, String> tree1 = new TreeMap<>();

        tree1.putAll(tree);

        System.out.println("Before: ");
        System.out.println(tree);
        System.out.println(tree1);

        tree1.putIfAbsent(1, "hello");

        System.out.println();
        System.out.println("After get Operations: ");
        System.out.println(tree.get(1));
        System.out.println(tree.getOrDefault(7, "nope"));
        System.out.println(tree.get(7));

        System.out.println("After Repplace Operations: ");

        // tree1.replace(1,"Hello");

        tree1.replace(1, "Hello", "Hello2");

        System.out.println("After Remove Operations: ");

        System.out.println(tree1.remove(2));
        System.out.println(tree1.remove(2, "hello"));
        System.out.println(tree1.remove(1, "abc"));


        // tree1.replaceAll(replaceFunction());

        // Using entrySet()
        System.out.println("Key/Value mappings: " + tree.entrySet());

        // Using keySet()
        System.out.println("Keys: " + tree.keySet());

        // Using values()
        System.out.println("Values: " + tree.values());


        System.out.println(tree.firstKey());
         System.out.println(tree.firstEntry());
         System.out.println(tree.lastKey());
        System.out.println(tree.lastEntry().getKey());



        System.out.println("After: ");
        System.out.println(tree);
        System.out.println(tree1);


    }
}

package JavaTreemap;

import java.util.TreeMap;

public class CreatingTreeMap {
    public static void main(String args[]){

        TreeMap<Integer, String> tree = new TreeMap<>();

        tree.put(1, "ABC");
        tree.put(3, "GHI");
        tree.put(2, "DEF");

        System.out.println(tree);

        TreeMap<Integer, String> tree2 = new TreeMap<>();

        tree2.putAll(tree);

        // System.out.println(tree2);

        tree.put(4, "PQA");
        
        tree.putIfAbsent(2, "asd");
        
        tree.put(3, "asd");
        
        System.out.println(tree);

    }
}

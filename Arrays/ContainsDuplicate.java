// 217. Contains Duplicate
import java.util.HashMap;

class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i :nums){
            if(map.containsKey(i)) return true;
            else map.put(i,1);
        }
        return false;
    }
    public static void main(String[] args){
        ContainsDuplicate cd = new ContainsDuplicate();
        System.out.println(cd.containsDuplicate(new int[]{1,2,3,1}));
    }
}
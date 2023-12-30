package DFS;

import java.util.ArrayList;
import java.util.List;

// // The problem is straightforward and can be solved by creating two separate arrays, 
// one containing leaves of the first tree and the other containing leaves of the second tree. 
// We can create this array using simple DFS (make sure to recurse to the left subtree before the right subtree - 
// this will give us the leaves strictly from left to right). Then we only have to compare these arrays. 
// Alternatively, instead of using arrays, we can store the leaves in a string separated by some sentinel value like a “#”.

class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
        this.right = right;
      }
    }


class LeafSimilar {
    ArrayList<Integer> a = new ArrayList<Integer>();
    ArrayList<Integer> b = new ArrayList<Integer>();

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        dfs(root1, a);
        dfs(root2, b);
        if(a.size()!=b.size()) return false;
        for(int i =0;i<a.size();i++){
            if(a.get(i)!=b.get(i)) return false;
        }
        return true;


    }
    public void dfs(TreeNode root, List<Integer> a){
        if(root==null) return;
        if(root.left==null && root.right==null){
            a.add(root.val);
            return;
        }
        dfs(root.left,a);
        dfs(root.right,a);
}
}
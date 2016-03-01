import java.util.*;

class MCSa extends MCQ {

    MCSa (int n,int[][]A,int[] degree,int style) {
	super(n,A,degree,style);
    }

    void search(){
	cpuTime                              = System.currentTimeMillis();
	nodes                                = 0;
	colourClass                          = new ArrayList[n];
	ArrayList<Integer> C                 = new ArrayList<Integer>(n);
	ArrayList<Integer> P                 = new ArrayList<Integer>(n);
	ArrayList<Integer> ColOrd            = new ArrayList<Integer>(n);
	for (int i=0;i<n;i++) colourClass[i] = new ArrayList<Integer>(n);
	orderVertices(ColOrd);
	expand(C,P,ColOrd);
    }

    void expand(ArrayList<Integer> C,ArrayList<Integer> P,ArrayList<Integer> ColOrd){
	if (timeLimit > 0 && System.currentTimeMillis() - cpuTime >= timeLimit) return;
	nodes++;
	int m = ColOrd.size();
	int[] colour = new int[m];
	numberSort(C,ColOrd,P,colour);
	for (int i=m-1;i>=0;i--){
	    int v = P.get(i);
	    if (C.size() + colour[i] <= maxSize) return;
	    C.add(v);
	    ArrayList<Integer> newP      = new ArrayList<Integer>(i);
	    ArrayList<Integer> newColOrd = new ArrayList<Integer>(i);
	    for (int j=0;j<=i;j++){
		int u = P.get(j);
		if (A[u][v] == 1) newP.add(u);
		int w = ColOrd.get(j);
		if (A[v][w] == 1) newColOrd.add(w);
	    }
	    if (newP.isEmpty() && C.size() > maxSize) saveSolution(C);
	    if (!newP.isEmpty()) expand(C,newP,newColOrd);
	    C.remove(C.size()-1);
	    P.remove(i);
	    ColOrd.remove((Integer)v);
	}
    }
}

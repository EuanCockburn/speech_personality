import java.util.*;

class MCQ extends MC {

    ArrayList[] colourClass;

    MCQ (int n,int[][]A,int[] degree,int style) {
	super(n,A,degree);
	this.style = style;
    }
    
    void search(){
	cpuTime                              = System.currentTimeMillis();
	nodes                                = 0;
	colourClass                          = new ArrayList[n];
	ArrayList<Integer> C                 = new ArrayList<Integer>(n);
	ArrayList<Integer> P                 = new ArrayList<Integer>(n);
	for (int i=0;i<n;i++) colourClass[i] = new ArrayList<Integer>(n);
	orderVertices(P);
	expand(C,P);
    }

    void expand(ArrayList<Integer> C,ArrayList<Integer> P){
	if (timeLimit > 0 && System.currentTimeMillis() - cpuTime >= timeLimit) return;
	nodes++;
	int m = P.size();
	int[] colour = new int[m];
	numberSort(P,P,colour);
	for (int i=m-1;i>=0;i--){
	    if (C.size() + colour[i] <= maxSize) return;
	    int v = P.get(i);
	    C.add(v);
	    ArrayList<Integer> newP = new ArrayList<Integer>(i);
	    for (int j=0;j<=i;j++){
		int u = P.get(j);
		if (A[u][v] == 1) newP.add(u);
	    }
	    if (newP.isEmpty() && C.size() > maxSize) saveSolution(C);
	    if (!newP.isEmpty()) expand(C,newP);
	    C.remove(C.size()-1);
	    P.remove(i);
	}
    }

    void numberSort(ArrayList<Integer> C,ArrayList<Integer> ColOrd,ArrayList<Integer> P,int[] colour){
	int colours = 0;
	int m = ColOrd.size();
	for (int i=0;i<m;i++) colourClass[i].clear();
	for (int i=0;i<m;i++){
	    int v = ColOrd.get(i);
	    int k = 0;
	    while (conflicts(v,colourClass[k])) k++;
	    colourClass[k].add(v);
	    colours = Math.max(colours,k+1);
	}
	P.clear();
	int i = 0;
	for (int k=0;k<colours;k++)
	    for (int j=0;j<colourClass[k].size();j++){
		int v = (Integer)(colourClass[k].get(j));
		P.add(v); 
		colour[i++] = k+1;
	    }
    }

    boolean conflicts(int v,ArrayList<Integer> colourClass){
	for (int i=0;i<colourClass.size();i++){
	    int w = colourClass.get(i);
	    if (A[v][w] == 1) return true;
	}
	return false;
    }

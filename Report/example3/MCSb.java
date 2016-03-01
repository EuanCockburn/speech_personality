import java.util.*;

class MCSb extends MCSa {

    MCSb (int n,int[][]A,int[] degree,int style) {
	super(n,A,degree,style);
    }

    void numberSort(ArrayList<Integer> C,ArrayList<Integer> ColOrd,ArrayList<Integer> P,int[] colour){
	int delta   = maxSize - C.size();
	int colours = 0;
	int m       = ColOrd.size();
	for (int i=0;i<m;i++) colourClass[i].clear();
	for (int i=0;i<m;i++){
	    int v = ColOrd.get(i);
	    int k = 0;
	    while (conflicts(v,colourClass[k])) k++;
	    colourClass[k].add(v);
	    colours = Math.max(colours,k+1);
	    if (k+1 > delta && colourClass[k].size() == 1 && repair(v,k)) colours--;
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

    int getSingleConflictVariable(int v,ArrayList<Integer> colourClass){
	int conflictVar = -1;
	int count       = 0;
	for (int i=0;i<colourClass.size() && count<2;i++){
	    int w = colourClass.get(i);
	    if (A[v][w] == 1){conflictVar = w; count++;}
	}
	if (count > 1) return -count;
	return conflictVar;
    }

    boolean repair(int v, int k){
	for (int i=0;i<k-1;i++){
	    int w = getSingleConflictVariable(v,colourClass[i]);
	    if (w >= 0)
		for (int j=i+1;j<k;j++)
		    if (!conflicts(w,colourClass[j])){
			colourClass[k].remove((Integer)v);
			colourClass[i].remove((Integer)w);
			colourClass[i].add(v);
			colourClass[j].add(w);
			return true;
		    }
	}
	return false;
    }
}

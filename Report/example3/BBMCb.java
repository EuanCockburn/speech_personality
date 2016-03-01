
    void orderVertices(){
	for (int i=0;i<n;i++){
	    V[i] = new Vertex(i,degree[i]);
	    for (int j=0;j<n;j++) 
		if (A[i][j] == 1) V[i].nebDeg = V[i].nebDeg + degree[j];
	}
        if (style == 1) Arrays.sort(V); 
	if (style == 2) minWidthOrder(V);    
	if (style == 3) Arrays.sort(V,new MCRComparator());
	for (int i=0;i<n;i++)
	    for (int j=0;j<n;j++){
		int u = V[i].index;
		int v = V[j].index;
		N[i].set(j,A[u][v] == 1);
		invN[i].set(j,A[u][v] == 0);
	    }
    }

    void saveSolution(BitSet C){
	Arrays.fill(solution,0);
	for (int i=0;i<C.size();i++) if (C.get(i)) solution[V[i].index] = 1;
	maxSize = C.cardinality();
    }
}

    
    void orderVertices(ArrayList<Integer> ColOrd){
	Vertex[] V = new Vertex[n];
	for (int i=0;i<n;i++) V[i] = new Vertex(i,degree[i]);
	for (int i=0;i<n;i++)
	    for (int j=0;j<n;j++) 
		if (A[i][j] == 1) V[i].nebDeg = V[i].nebDeg + degree[j];
	if (style == 1) Arrays.sort(V);
	if (style == 2) minWidthOrder(V);
	if (style == 3) Arrays.sort(V,new MCRComparator());
	for (Vertex v : V) ColOrd.add(v.index);
    }

     void minWidthOrder(Vertex[] V){
	ArrayList<Vertex> L = new ArrayList<Vertex>(n);
	Stack<Vertex> S = new Stack<Vertex>();
	for (Vertex v : V) L.add(v);
	while (!L.isEmpty()){
	    Vertex v = L.get(0);
	    for (Vertex u : L) if (u.degree < v.degree) v = u;
	    S.push(v); L.remove(v);
	    for (Vertex u : L) if (A[u.index][v.index] == 1) u.degree--;
	}
	int k = 0;
	while (!S.isEmpty()) V[k++] = S.pop();
    }
}

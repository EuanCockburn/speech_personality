import java.util.*;

public class Vertex implements Comparable<Vertex> {

    int index, degree, nebDeg;

    public Vertex (int index,int degree) {
	this.index  = index;
	this.degree = degree;
	nebDeg      = 0;
    }

    public int compareTo(Vertex v){
	if (degree < v.degree || degree == v.degree && index > v.index) return 1;
	return -1;
    }
}

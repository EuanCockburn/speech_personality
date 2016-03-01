import java.util.*;

public class RandomGraph { 
  
    public static void main(String[] args) throws Exception {
	int n      = Integer.parseInt(args[0]);
	double p   = Double.parseDouble(args[1]);
	Random gen = new Random();
	System.out.println("p edge "+ n + " 0");
	for (int i=0;i<n-1;i++)
	    for (int j=i+1;j<n;j++)
		if (p >= gen.nextDouble())
		    System.out.println("e "+ (i+1) +" "+ (j+1));
    }
}

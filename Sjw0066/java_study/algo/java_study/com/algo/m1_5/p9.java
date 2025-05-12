package java_study.com.algo.m1_5;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p9 {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a,b,c,d;
		a=3;
		b=3;
		c=8;
		d=3;
		
		int ans=(a*b)+(c*d);
		
		bw.write(ans+"");
		bw.flush();
		bw.close();
		
				
	}
}	

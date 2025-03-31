package java_study.com.algo.m1_5;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p7 {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a=10;
		int b=3;
		
		int mul=a*b;
		int div=a/b;
		
		bw.write("10 * 3 = ");
		bw.write(mul+"\n");
		bw.write("10 / 3 = ");
		bw.write(div+"");
		bw.flush();
		bw.close();
		
				
	}
}	

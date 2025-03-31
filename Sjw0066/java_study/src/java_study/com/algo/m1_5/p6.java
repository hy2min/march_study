package java_study.com.algo.m1_5;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p6 {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a,b,c;
		a=40;
		b=60;
		c=10;
		
		int g=a+c;
		int h=b-c;
		
		bw.write(g+"\n");
		bw.write(h+"\n");
		bw.flush();
		bw.close();
	}
}	

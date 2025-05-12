package java_study.com.algo.m1_5;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p4 {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a=10;
		
		bw.write("a의 값은 "+a+"입니다");
		bw.close();
	
	}
}	

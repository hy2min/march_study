package java_study.com.algo.m1_5;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p5 {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int bbq;
		bbq=5;
		
		bw.write("bbq의 값은 ");
		bw.write(bbq+"");
		bw.write("입니다");
		bw.flush();
		bw.close();
	}
}	

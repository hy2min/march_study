package java_study.com.algo.m1_5;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p5 {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int bbq;
		bbq=5;
		
		bw.write("bbq�� ���� ");
		bw.write(bbq+"");
		bw.write("�Դϴ�");
		bw.flush();
		bw.close();
	}
}	

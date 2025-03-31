package java_study.com.algo.m3;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p14 {

	public static void main(String[] args) throws IOException{
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		
		for(int i=-5;i<6;i++) {
			bw.write(i+" ");	
		}
		
		
		bw.close();
		
		
	}

}

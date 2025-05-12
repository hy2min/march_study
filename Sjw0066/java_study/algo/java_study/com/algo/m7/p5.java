package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p5{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a= Integer.parseInt(br.readLine());
		
		if (a>=80) {
			bw.write("수");
		}else if(a>=70) {
			bw.write("우");
		}else if(a>=60) {
			bw.write("미");
		}else {
			bw.write("재시도");
		}
				
		
		bw.close();
		br.close();
				
	}
}

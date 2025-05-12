package java_study.com.algo.m8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p11 {
	public static void main(String[] args)throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
		int a= Integer.parseInt(br.readLine());
		
		if (a>=3500 && a<=5000) {
			starBox(bw);
		}else if(a<3500 && a>=2500) {
			macDoll(bw);
		}else {
			copyBean(bw);
		}
		br.close();
		bw.close();
	}
	
	public static void starBox(BufferedWriter bw) throws IOException{
		for (int i = 1; i<20 ;i+=2) {
			bw.write(i+" ");
		}
	}
	
	public static void macDoll(BufferedWriter bw) throws IOException{
		for (int i = 72; i>64 ; i--) {
			bw.write((char) i +" " );
		}
	}

	public static void copyBean(BufferedWriter bw) throws IOException{
		for (int i = -5 ;i<6;i++) {
			bw.write(i+" ");
		}
	}
	
}

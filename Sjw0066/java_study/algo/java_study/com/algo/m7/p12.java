package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p12{
		
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a = Integer.parseInt(br.readLine());
		
		if (a==3 || a==5 || a==7) {
			for (int i =1;i<11;i++) {
				bw.write(i+"");
			}
		}else if (a==0 || a==8) {
			for (int i =10;i>0;i--) {
				bw.write(i+"");
			}
		}else {
			BBQ(a, bw);
		}
		
		br.close();
		bw.close();
	}
	
	public static void BBQ(int a,BufferedWriter bw) throws IOException {
		if (a>0 && a<5) {
			bw.write("초기값");
		}else if(a>6 && a<10) {
			bw.write("중간값");
		}else {
			bw.write("알수없는값");
		}
	}
	
}

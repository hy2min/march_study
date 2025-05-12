package java_study.com.algo.m8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p8 {
	static String[] arr1 = {"B","D","5","Q","A"};
	static String[] arr2 = {"Q","E","R","E","F"};
	public static void main(String[] args)throws IOException {
		
		String a= input();
		output(a);
	}
	
	public static String input() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		br.close();
		return a;
	}
	
	public static void output(String str1) throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		char[] chr1=str1.toCharArray();
		char ch=chr1[0];
		
		if (Character.isUpperCase(ch)) {
			for (int i = 0 ; i<5 ; i++) {
				bw.write(arr2[i]+"");
			}
		}else if (Character.isLowerCase(ch)) {
			for (int i = 0 ; i<5 ; i++) {
				bw.write(arr1[i]+"");
			}
		}else {
			for (int i = 72 ; i>64 ; i--) {
				bw.write((char) i+"");
			}
		}
		
		bw.close();
	}
}

package java_study.com.algo.m8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class p3 {

	public static void main(String[] args)throws IOException {
		int s=input();
		output(s);
	}
	
	public static int input() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int a=Integer.parseInt(st.nextToken()); 
		int b=Integer.parseInt(st.nextToken()); 
		
		br.close();
		return a+b;
	}
	
	public static void output(int Sum) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i = 5 ; i<=Sum;i++) {
			bw.write(i+" ");
		}
		bw.close();
	}
	
	
	
}

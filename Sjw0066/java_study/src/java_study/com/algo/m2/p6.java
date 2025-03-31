package java_study.com.algo.m2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p6 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st= new StringTokenizer(br.readLine());
		
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		int sum=a+b;
		int mul=a*b;
		int div=a/b;
		
		bw.write(a+"+"+b+"="+sum+"\n");
		bw.write(a+"*"+b+"="+mul+"\n");
		bw.write(a+"/"+b+"="+div+"\n");
		br.close();
		bw.close();
	}

}

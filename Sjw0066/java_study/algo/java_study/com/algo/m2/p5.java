package java_study.com.algo.m2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p5 {

	public static void main(String[] args) throws IOException{
		BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st= new StringTokenizer(br.readLine());
		int a= Integer.parseInt(st.nextToken()); 
		int b= Integer.parseInt(st.nextToken());
		
		int ans=a-b;
		
		bw.write("�� ������ ���� "+ans+" �Դϴ�.");
		bw.close();
		br.close();
	}

}

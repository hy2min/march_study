package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p2{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		int a= Integer.parseInt(st.nextToken());
		int b= Integer.parseInt(st.nextToken());
		
		if (a>b) {
			if ((a-b)%2==0) {
				bw.write("¦�����");
			
			}else {
				bw.write("����Ѵ�");
			}
		}else {
			if ((b-a)%2==0) {
				bw.write("¦�����");
			
			}else {
				bw.write("����Ѵ�");
			}
		}
		
		bw.close();
		br.close();
				
	}
}

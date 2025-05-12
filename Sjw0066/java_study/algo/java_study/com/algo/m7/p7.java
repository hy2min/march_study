package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p7{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int Max=Integer.MIN_VALUE;
		int Min=Integer.MAX_VALUE;
		
		for (int i = 0 ;i<3;i++) {
			int a= Integer.parseInt(st.nextToken());
			if(Max<a) {
				Max=a;
			}
			if(Min>a) {
				Min=a;
			}
		}
		bw.write("MAX="+Max+"\n");
		bw.write("MIN="+Min);
		bw.close();
		br.close();
				
	}
}

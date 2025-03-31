package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p9{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[] arr=new int[5];
		StringTokenizer st= new StringTokenizer(br.readLine());
		
		for (int i = 0 ; i<5 ; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		for (int i = 0 ; i<5 ; i++) {
			if (arr[i]>=70) {
				bw.write((i+1)+"번사람은"+arr[i]+"점PASS\n");
			}else if (arr[i]>=50) {
				bw.write((i+1)+"번사람은"+arr[i]+"점RETEST\n");
			}else {
				bw.write((i+1)+"번사람은"+arr[i]+"점FAIL\n");
			}
		}
	
		
		bw.close();
		br.close();
				
	}
}

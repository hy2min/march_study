package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p4{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[5];
		for (int i = 0 ; i<5 ;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int cnt=0;
		for (int i=0; i<5 ; i++) {
			if (arr[i]>=3 && arr[i]<=7) {
				cnt++;
			}
		}
		bw.write(cnt+"");
		
		bw.close();
		br.close();
				
	}
}

package java_study.com.algo.m8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class p4 {

	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[6];
		
		for (int i = 0 ; i<6 ;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		
		for (int i = 5 ; i>-1 ;i--) {
			if (arr[i] == 7) {
				bw.write(arr[i]+" ");	
				break;
			}else {
				bw.write(arr[i]+" ");	
			}
			
		}
		
		bw.close();
		br.close();
		
	}
}

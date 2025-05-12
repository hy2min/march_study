package java_study.com.algo.m18;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _2 {
	static StringTokenizer st;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[][] arr = new int[3][3];
		int[] dat=new int[10];
		
		for (int i = 0; i < 3; i++) {
			st= new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				dat[arr[i][j]]++; 
			}
		}
		
		for (int i = 1; i<10 ; i++) {
			if (dat[i]==0) {
				bw.write(i+" ");
			}
 		}
		bw.close();
		br.close();
	}

}

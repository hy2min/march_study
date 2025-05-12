package java_study.com.algo.m18;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _3 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		int arr[][] = {
			    {1, 3, 3, 5, 1},
			    {3, 6, 2, 4, 2},
			    {1, 9, 2, 6, 5}
			};
		
		int[] dat= new int[10];
		
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 5; j++) {
				dat[arr[i][j]]++ ;
			}
		}
		
		for (int i = 1; i<10;i++) {
			if (dat[i]==N) {
				bw.write(i+" ");
			}
		}
		
		bw.close();
		br.close();
	}

}

package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p3{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[][] arr = {
				{3,1,1},
				{2,3,2},
		};
		
		for (int i = 0 ; i <2 ; i++) {
			for (int j = 0 ; j <3 ;j++) {
				bw.write(arr[i][j]+"");
			}
		}
		bw.close();
		br.close();
				
	}
}

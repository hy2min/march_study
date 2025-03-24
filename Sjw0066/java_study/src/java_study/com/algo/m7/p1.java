package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p1{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a=Integer.parseInt(br.readLine());
		int[] arr1= {3,5,2,4,1};
		int[][] arr2= {
				{9,8},
				{7,1},
				{3,4},
		};
		
		if (a%2==0) {
			for (int i=0 ; i<3 ;i++) {
				for (int j = 0 ; j<2;j++) {
					bw.write(arr2[i][j]+"");
				}
				bw.write("\n");
			}
		}else {
			for (int i =0 ; i<5 ;i++) {
				bw.write(arr1[i]+"");
			}
		}
		bw.close();
		br.close();
				
	}
}

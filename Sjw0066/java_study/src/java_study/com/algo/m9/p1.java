package java_study.com.algo.m9;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p1 {

	public static void main(String[] args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		int[][] arr= new int[4][4];
		if (a%2==0) {
			for (int i = 0 ;i<4;i++) {
					arr[i][i] = i+1;
			}
		}else {
			for (int i = 0 ;i<4;i++) {
				arr[i][3-i] = i+1;
		}
		}
		
		for(int i = 0; i< 4; i++) {
			for(int j = 0 ; j<4;j++) {
				bw.write(arr[i][j]+" ");
			}
			bw.write("\n");
		}
		
		br.close();
		bw.close();
	}

}

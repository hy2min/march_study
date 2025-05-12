package java_study.com.algo.m8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p10 {
	static int[][] arr= {
			{4,3,1,1},
			{3,1,2,1},
			{0,0,1,2},
	};
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine());
		int cnt=0;
		for (int i = 0 ; i<3 ;i++) {
			for (int j = 0 ; j<4 ; j++) {
				if(a==arr[i][j]) {
					cnt++;
				}
			}
		}
		bw.write(cnt+"개 존재합니다");
		br.close();
		bw.close();
		
	}
}

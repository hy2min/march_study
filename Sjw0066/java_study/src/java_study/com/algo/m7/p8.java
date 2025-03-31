package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p8{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[][] arr= {
				{3,4,1},
				{2,1,4},
				{3,3,0},
		};
		int cnt1=0;
		int cnt2=0;
		
		for (int i = 0 ; i<3 ;i++) {
			for (int j =0;j<3;j++) {
				if (arr[i][j]%2==0) {
					cnt1++;
				}else {
					cnt2++;
				}
			}
		}
		bw.write("Â¦¼ö : "+cnt1+"\n");
		bw.write("È¦¼ö : "+cnt2+"\n");
		
		bw.close();
		br.close();
				
	}
}

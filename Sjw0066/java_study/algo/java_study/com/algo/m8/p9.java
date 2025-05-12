package java_study.com.algo.m8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p9 {
	static int[][] arr=new int[2][3];
	public static void main(String[] args)throws IOException {
		input();
		output();
	}
	
	public static void input() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st= new StringTokenizer(br.readLine());
		for (int i=0;i<2;i++) {
			for (int j = 0 ; j <3 ; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		br.close();
	}
	
	public static void output() throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int Sum=0;
		for (int i = 0 ; i<2; i++) {
			for (int j = 0 ; j<3 ;j++) {
				Sum+=arr[i][j];
			}
		}
		bw.write(Sum+"");
		bw.close();
	}
}

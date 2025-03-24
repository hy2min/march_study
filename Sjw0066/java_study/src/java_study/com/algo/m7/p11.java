package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p11{
		
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a = input(br);
		int[][] arr = Process(a);
		output(bw, arr);
		br.close();
		bw.close();
	}
	
	public static int input(BufferedReader br) throws IOException {
		int a = Integer.parseInt(br.readLine());
		return a;
	}
	
	public static int[][] Process(int a) {
		int[][] arr=new int[3][3];
		
		for (int i = 0 ;i<3 ;i++) {
			for (int j=0 ; j<3 ;j++) {
				arr[i][j] = a;
				a++;
			}
		}
		
		return arr;
	}
	
	public static void output(BufferedWriter bw , int[][] arr) throws IOException{
		for (int i = 0 ;i<3 ;i++) {
			for (int j=0 ; j<3 ;j++) {
				bw.write(arr[i][j]+" ");
			}
			bw.write("\n");
		}
	}
	
}

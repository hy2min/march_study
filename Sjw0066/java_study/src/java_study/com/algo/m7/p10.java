package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p10{
	
	
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[][] arr = new String[4][4];
		String a = br.readLine();
		Input1(a,arr);
		Output1(arr);
		br.close();
				
	}
	
	public static void Input1(String a,String[][] arr) {
		for (int i = 0;i<4;i++) {
			for (int j = 0 ; j<4 ; j++) {
				arr[i][j] = a;
			}
		}
	}
	
	public static void Output1(String[][] arr) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i = 0;i<4;i++) {
			for (int j = 0 ; j<4 ; j++) {
				bw.write(arr[i][j]+"");
			}
			bw.write("\n");
		}
		
		bw.close();
	}
	
}

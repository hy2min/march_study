package java_study.com.algo.m1;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class p1 {
	public static int[][] arr;
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		
		System.out.println(a);
		arr = new int[3][3] ; 
		for(int i=0;i<3;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j=0; j<3;j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
			System.out.println(Arrays.toString(arr[i]));
		};
		br.close();
	}
	
}

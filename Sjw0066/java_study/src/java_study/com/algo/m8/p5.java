package java_study.com.algo.m8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p5 {

	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[] arr = {3,4,1,6,7,5};
		int i = 0 ;
		while (i<6){
			bw.write(arr[i]+" ");
			i++;
		}
		
		bw.close();
		br.close();
		
	}
}

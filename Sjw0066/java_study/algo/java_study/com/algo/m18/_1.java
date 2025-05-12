package java_study.com.algo.m18;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _1 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[][] MAP = {
			    {65000, 35, 42, 70},
			    {70, 35, 65000, 1300},
			    {65000, 30000, 38, 42},
		};
		int[] dat = new int [65536];
		for (int i = 0; i < MAP.length; i++) {
			for (int j = 0; j < MAP[i].length; j++) {
				dat[MAP[i][j]] ++;
			}
		}
		
		int maxIdx=-1;
		int maxVal=Integer.MIN_VALUE;
		
		for (int i = 0; i < dat.length; i++) {
			if(maxVal<dat[i]) {
				maxVal = dat[i];
				maxIdx = i;						
			}
		}
		bw.write(maxIdx+"");
				
		bw.close();

	}

}

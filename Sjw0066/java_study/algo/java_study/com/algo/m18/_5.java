package java_study.com.algo.m18;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _5 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		char[] cardlist= br.readLine().toCharArray();
		
		int[] dat=new int[26];
		
		for (int i = 0; i < cardlist.length; i++) {
            int idx = cardlist[i] - 'A';  
            dat[idx]++;
        }
		
		int cnt=0;
		
		for (int i = 0; i < cardlist.length; i++) {
			if(dat[i]>0) {
				cnt++;
			}
        
        }
		
		bw.write(cnt+"°³");
		
		bw.close();
		br.close();
	}

}

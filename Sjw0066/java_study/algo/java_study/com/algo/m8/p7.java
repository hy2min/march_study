package java_study.com.algo.m8;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class p7 {
	public static void main(String[] args)throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] arr = {"#","_","#","_","#","#"};
		
		for (int i = 0 ; i<6 ;i++) {
			if(arr[i].equals("#")) {
				bw.write("¼¥");
			}else {
				bw.write("¹«");
			}
		}
		bw.close();
		
	}
}

package java_study.com.algo.m7;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p6{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i =0;i<4;i++) {
			int a= Integer.parseInt(st.nextToken());
			if (a<20) {
				bw.write("�� ū���� �Է��ϼ���\n");
			}else if (a>20) {
				bw.write("�� �������� �Է��ϼ���\n");
			}else {
				bw.write("�����Դϴ�\n");
			}
		}
		
		bw.close();
		br.close();
				
	}
}

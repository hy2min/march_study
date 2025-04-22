package java_study.com.back;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class _1038 {
	static int N;
	static long ans=-1;
	static int cnt=0;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N=Integer.parseInt(br.readLine());
		Queue<long[]> q=new LinkedList<>();
		// now,before
		
		for (int i=0; i<10;i++) {
			q.add(new long[] {i,cnt}) ;
			cnt++;
		}
		
		while (!q.isEmpty()) {
			long[] temp=q.poll();
			
			if (temp[1] == N) {
				ans=temp[0];
				break;
			}
			
			for (long i = 0;i<(temp[0]%10);i++) {
				long next = Long.parseLong(temp[0]+""+i);
				
				q.add(new long[] {next,cnt});
				cnt++;
			}
			
		}
		
		
		bw.write(ans+"\n");
		
		bw.close();
		br.close();
	}
	
	
	
}

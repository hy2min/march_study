package java_study.com.swea;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class swea1494 {
	static long ans;
	static boolean[] visited ;
	static int N;
	static int[][] arr;
	
	static void dfs(int now,int cnt) {
		 if (cnt ==	N/2) {
	            long x=0,y=0;
	            for (int i =0; i<N; i++) {
	            	if (visited[i]) {
	            		x+=arr[i][0];
	            		y+=arr[i][1];
            		}else {
            			x-=arr[i][0];
            			y-=arr[i][1];
            		}
	            }
	            
	            ans = Math.min(ans, x*x+y*y);
	            return;
	        }
		 
		 for (int i =now; i<N;i++) {
			 if(!visited[i]) {
				 visited[i]=true;
				 dfs(i,cnt+1);
				 visited[i]=false;
			 }
		 }
		 
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<T+1;tc++) {
			N = Integer.parseInt(br.readLine());
			arr = new int[N][2];
			ans = Long.MAX_VALUE;
			visited= new boolean[21];
			for (int i = 0; i<N;i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());	
				arr[i][0] = Integer.parseInt(st.nextToken());
				arr[i][1] = Integer.parseInt(st.nextToken());
			}
			
			dfs(0,0);
			bw.write("#"+tc+" "+ans+"\n");
			
		}
		
		br.close();
		bw.close();
	}

}

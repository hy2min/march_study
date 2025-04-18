import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class swea3 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<T+1;tc++) {
			int N = Integer.parseInt(br.readLine());
			int[] dat=new int[10];
			for (int i =0; i<10; i++) {
				dat[i]=0;
			}
			
			int k=1;
			while (true) {
				String temp=String.valueOf(k*N);
				
				for (String t : temp.split("")) {
					dat[Integer.parseInt(t)] += 1;
				}
				
				boolean flag=true;
				for (int i =0; i<10; i++) {
					if (dat[i]==0) {
						flag=false;
					}
				}
				if (flag) {
					break;
				}
				k++;
			}
			
			bw.write("#"+tc+" "+k*N+"\n");
		
		}
		bw.close();
		br.close();		
	}
}

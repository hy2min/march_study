import java.io.*;
import java.util.*;

public class _1759 {
    static StringTokenizer st;
    static int L;
    static int C;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        String[] arr = br.readLine().split(" ");
        String[] vowels = {"a", "e", "i", "o", "u"};
        ArrayList<String> vowel=new ArrayList<>();
        ArrayList<String> =new ArrayList<>();
        Set<String> vowelSet = new HashSet<>(Arrays.asList(vowels));

        for (int i = 0; i < arr.length; i++) {
            if (vowelSet.contains(arr[i])) {
                
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}

package week1;

import java.util.*;
import java.io.*;
import java.net.*;

public class Anagram1 {
	private static ArrayList<String> dictionary;
	private static ArrayList<String> anadictionary;
	
	public static void main(String[] args) throws IOException{
		dictionary = new ArrayList<String>();
		anadictionary = new ArrayList<String>();
		
		URL dicturl = new URL("https://icanhazwordz.appspot.com/dictionary.words");
		BufferedReader in = new BufferedReader(new InputStreamReader(dicturl.openStream()));
		
		String word;
		
		while(true) {
			word = in.readLine();
			if(word==null) break;
		
			dictionary.add(word);
			anadictionary.add(alphabetize(word));		
		}
		in.close();
		
		Scanner sc = new Scanner(System.in);
		String inputWord = sc.nextLine();
		
		for(int i =0; i<anadictionary.size(); i++) {
			if(alphabetize(inputWord).equals(anadictionary.get(i))) {
				System.out.println(dictionary.get(i));
			}
		
	}
}
	

	public static String alphabetize(String word) {
		char[] alphword = word.toCharArray();
		Arrays.sort(alphword);
		word = new String(alphword);
		
		return word;		
		
	}
	
	
}

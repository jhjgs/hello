package week2;

import java.util.Random;
import java.util.Scanner;

public class Matrixtime {

	private static Scanner sc;

	public static void main(String[] args) {
		sc = new Scanner(System.in);
		System.out.println("Input n: ");
		int n = sc.nextInt();
				
		int [][]a = new int [n][n];
		int [][]b = new int [n][n];
		
		Random rand = new Random();
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				a[i][j] = rand.nextInt(10);
				b[i][j] = rand.nextInt(10);
			}
		}
		
		System.out.println("a= ");
	    print(a);
		System.out.println("b= ");
		print(b);
		
		System.out.println("a*b= ");
		
		long start = System.nanoTime();
		print(times(a,b,n));
		long time = System.nanoTime() - start;
		
		System.out.println("Execution time: "+time);
		
	}
	public static void print(int[][] M){
		for(int i=0; i<M.length; i++) {
			for(int j=0; j<M[0].length; j++) {
				System.out.print(M[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	public static int[][] times(int[][] a, int [][] b, int n){
		
		int [][] T = new int [n][n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				 int t=0;
				 
				for(int k=0; k<n; k++) {
					t += a[i][k]*b[k][j];
				}
				
				T[i][j]=t;
			}
		}
		return T;
	}

}

#include<iostream>
#include<cstdlib>
#include<ctime>
#include<fstream>
using namespace std;
int insertion(int a[],int n);
int mergesort(int a[],int low,int high);
int quicksort(int a[],int low,int high);
int main()
{
	fstream writeout;                   // to write output in text file
	srand(time(0));
	int j,minArray,maxArray,arrayGap,k,cases,*arrayInsertion,*arrayMerge,*arrayQuick;
	double totalInsertion=0,totalMerge=0,totalQuick=0;
	writeout.open("comparisons.txt",ios::out|ios::in|ios::trunc);
	minArray=10;                            //smallest size of array to be generated
	maxArray=1000;                          //largest size of array to be generated
	arrayGap=10;                            //incrementation in size of an array at each iteration
	writeout<<"S.no.,No. of elements,insertion sort,merge sort,quick sort\n";
	for(cases=0;cases<=((maxArray-minArray)/arrayGap);cases++)
	{
		for(k=0; k<20; k++)                                             //number of iterations for each size of array
		{
			arrayInsertion=new int[minArray+(arrayGap*cases)];          //array for insertion sort
			arrayMerge=new int[minArray+(arrayGap*cases)];              //array for merge sort
			arrayQuick=new int[minArray+(arrayGap*cases)];              //array for quick sort
			for(j=0;j<minArray+(arrayGap*cases);j++)
				arrayInsertion[j]=arrayMerge[j]=arrayQuick[j]=(rand()%10000);   //storing random values between 0 and 9999 in all the arrays
			totalInsertion+=insertion(arrayInsertion,minArray+(arrayGap*cases));    //summing up all the comparisons
			totalMerge+=mergesort(arrayMerge,0,minArray+(arrayGap*cases)-1);        //in each type of the sort
			totalQuick+=quicksort(arrayQuick,0,minArray+(arrayGap*cases)-1);
			delete[] arrayInsertion;
			delete[] arrayMerge;                                        //releasing memory
			delete[] arrayQuick;
		}
        writeout<<cases+1<<","<<minArray+(arrayGap*cases)<<","<<totalInsertion/20.0<<","<<totalMerge/20.0<<","<<totalQuick/20.0<<"\n";  //division by 20.0 to find the average value in each iteration
	}
	writeout.close();
	system("comparisons2.xlsx");
	return 0;
}
int insertion(int a[],int n)                            //Insertion sort
{
	int i,flag;
	int comparisons=0;
	for(i=1;i<n;i++)
	{
		flag=0;
		int j=i-1,temp=a[i];
		while(a[j]>temp && j>=0)
		{
			comparisons++;
			a[j+1]=a[j];
			j--;
			flag=1;
		}
		a[j+1]=temp;
	}
	return comparisons;
}
int merge(int a[],int low,int mid,int high)                 //merging function in merge sort
{
	int i=low,j=mid+1,k=0;
	int *temp=new int[high-low+1];
	int comparisons=0;
	while(i<=mid&&j<=high)
	{
		comparisons++;
		if(a[i]<=a[j])
		{
			temp[k]=a[i];
			k++;
			i++;
		}
		else
		{
			temp[k]=a[j];
			k++;
			j++;
		}
	}

	while(i<=mid)
	{
		temp[k]=a[i];
		k++;
		i++;
	}
	while(j<=high)
	{
		temp[k]=a[j];
		k++;
		j++;
	}

	for(int i=low,j=0;i<=high&&j<k;i++,j++)
	{
		a[i]=temp[j];
	}
	delete []temp;
	return comparisons;
}
int mergesort(int a[],int low,int high)                 //merge sort
{
	int comparisons=0;
	if(low<high)
	{
		int mid=(low+high)/2;
		comparisons+=mergesort(a,low,mid);
		comparisons+=mergesort(a,mid+1,high);
		comparisons+=merge(a,low,mid,high);
	}
	return comparisons;
}
int* partition(int a[],int low,int high)            //partition function in quick sort
{
	int comparisons=0;
	int lb=low;
	int ub=high;
	int pivot=a[lb];
	while(lb<ub)
	{
		while(a[lb]<=pivot&&lb<ub)
		{
			lb++;
			comparisons++;
		}
		while(a[ub]>pivot)
		{
			ub--;
			comparisons++;
		}
		if(lb<ub)
		{
			int temp=a[lb];
			a[lb]=a[ub];
			a[ub]=temp;
		}
	}
	a[low]=a[ub];
	a[ub]=pivot;
	int result[2];                              //result having number of comparisons and the actual position of pivot in the array.
	result[0]=ub;
	result[1]=comparisons;
	return result;
}
int quicksort(int a[],int low,int high)             //quick sort
{
	int comparisons=0;
	if(low>=high)
        return comparisons;
	int* x=partition(a,low,high);
	comparisons+=x[1];
	comparisons+=quicksort(a,low,x[0]-1);
	comparisons+=quicksort(a,x[0]+1,high);
	return comparisons;
}

package week_051622;

import java.util.LinkedList;


public class Driver {

	public static void main(String[] args) {
		
		int num1 = 617;
		LinkedList<Integer> list1 = AddList.makeList(num1);
		int num2 =295;
		LinkedList<Integer> list2 = AddList.makeList(num2);
		System.out.println("sum lists:\n  " + list2);
		LinkedList<Integer> sumList = AddList.add(list1, list2);
		System.out.println("+ " + sumList + " = " + AddList.makeNum(sumList)+ "\n\n");

		System.out.println("Running Stack Min");
		StackMin stack = new StackMin();
		System.out.println("Push 3, 6");
		stack.add(3);
		stack.add(6);
		System.out.println("Min " + stack.getMin());
		System.out.println("Push 2");
		stack.add(2);
		System.out.println("Min " + stack.getMin());
		System.out.println("Pop " + stack.remove());
		System.out.println("Min " + stack.getMin());
		
		StackMin stack2 = new StackMin();
		stack2.add(9);
		stack2.add(1);
		System.out.println("stack min:\nMin " + stack2.getMin());
		stack2.add(2);
		System.out.println("   Min = " + stack2.getMin());
		System.out.println("Remove = " + stack2.remove());
		System.out.println("   Min = " + stack2.getMin());
	}
}
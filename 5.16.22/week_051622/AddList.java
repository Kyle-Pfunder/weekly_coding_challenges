package week_051622;

import java.util.LinkedList;

public class AddList {
	
	public static LinkedList<Integer> makeList(int num) {
		LinkedList<Integer> convertList = new LinkedList<>();
		while (num > 0) {
			convertList.add(num % 10);
			num = num / 10;
		} return convertList;
	}
	
	public static int makeNum(LinkedList<Integer> convertList) {
		int num = 0;
		while (!convertList.isEmpty()) {
			num *= 10;
			num += convertList.pollLast();
		} return num;
	}
	
	public static LinkedList<Integer> add(LinkedList<Integer> list1, LinkedList<Integer> list2) {
		LinkedList<Integer> sum = makeList(makeNum(list1) + makeNum(list2));
		return sum;
	}
}
package week_051622;

import java.util.Stack;


public class StackMin {
	
	private Stack<Node> stack;

	
	public StackMin() {
		super();
		this.stack = new Stack<>();
	}
	

public void add(int val) {
	if (stack.empty()) {
		stack.push(new Node(val,val));
	}
	else if (val < stack.peek().min) {
		stack.push(new Node(val,val));
	}
	else {
        stack.push(new Node(val, stack.peek().min));
	}
}

public int remove() {
	return this.stack.pop().min;
}

public int getMin() {
    return this.stack.peek().min;
}

public int getValue() {
    return this.stack.peek().value;
	}
}
class MyQueue {

    Stack<Integer> queueStack;
    Stack<Integer> tempStack;

    // attempted method: is to invert the stack every time,
    // place at the end, then invert it back

    public MyQueue() {
        queueStack = new Stack();
        tempStack = new Stack();
    }

    // put new element
    public void push(int x) {
        if(queueStack.empty()) {
            queueStack.push(x);
        } else {
            while (!queueStack.empty()) {
                int temp = queueStack.pop();
                tempStack.push(temp);
            }
            queueStack.push(x);
            while (!tempStack.empty()) {
                int temp = tempStack.pop();
                queueStack.push(temp);
            }
        }
    }

    public int pop() {
        return queueStack.pop();
    }

    public int peek() {
        return queueStack.peek();
    }

    public boolean empty() {
        return queueStack.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
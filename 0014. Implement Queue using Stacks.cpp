// time = Amortized O(1)
// space = O(n)

class MyQueue {
private:
    stack<int> in;
    stack<int> out;
public:
    void push(int x) {
        in.push(x);
    }
    
    int pop() {
        int val = peek();
        out.pop();
        return val;
    }
    
    int peek() {
        if (out.empty()) {
            while (!in.empty()) {
                out.push(in.top());
                in.pop();
            }
        }
        return out.top();
    }
    
    bool empty() {
        return out.empty() && in.empty();
    }
};
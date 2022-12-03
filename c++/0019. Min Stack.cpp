// time = O(1)
// space = O(n)

// vanilla linked list

struct Node {
    int val;
    int min;
    Node* prev;

    Node(int val, int min, Node* prev){
        this->val = val;
        this->min = min;
        this->prev = prev;
    }
};

class MinStack {
    Node* head = nullptr;
public:
    void push(int val) {
        if (!head || val < head->min) {
            head = new Node(val, val, head);
        } else {
            head = new Node(val, head->min, head);
        }
    }
    
    void pop() {
        Node* to_pop = head;
        head = head->prev;
        delete to_pop;
    }
    
    int top() {
        return head->val;
    }
    
    int getMin() {
        return head->min;
    }
};

// single stack
class MinStack {
private:
    stack<pair<int,int>> min_stack;
public:
    void push(int val) {
        if (min_stack.empty() || val < min_stack.top().second) {
            min_stack.push({val, val});
        } else {
            min_stack.push({val, min_stack.top().second});
        }
    }
    
    void pop() {
        min_stack.pop();
    }
    
    int top() {
        return min_stack.top().first;
    }
    
    int getMin() {
        return min_stack.top().second;
    }
};
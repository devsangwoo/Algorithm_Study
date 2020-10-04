class MyQueue {
  constructor() {
    this.stack = [];
    this.stackTemp = [];
  }

  push(x) {
    this.stack.push(x);
  }

  pop() {
    while (this.stack.length !== 0) {
      this.stackTemp.push(this.stack.pop());
    }
    let pop = this.stackTemp.pop();
    while (this.stackTemp.length !== 0) {
      this.stack.push(this.stackTemp.pop());
    }
    return pop;
  }

  peek() {
    while (this.stack.length !== 0) {
      this.stackTemp.push(this.stack.pop());
    }
    let pop = this.stackTemp.pop();
    this.stackTemp.push(pop);
    while (this.stackTemp.length !== 0) {
      this.stack.push(this.stackTemp.pop());
    }
    return pop;
  }

  empty() {
    return this.stack.length === 0 ? true : false;
  }
}

let myQueue = new MyQueue();
myQueue.push(1);
myQueue.push(2);
myQueue.push(3);
console.log('myQueue', myQueue);
let removeValue = myQueue.pop();
console.log('removeValue', removeValue);
console.log('myQueue', myQueue);
let getValue = myQueue.peek();
console.log('getValue', getValue);
console.log('myQueue', myQueue);
let existenceConfirm = myQueue.empty();
console.log('existenceConfirm', existenceConfirm);

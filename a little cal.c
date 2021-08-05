#include <stdio.h>
#include <stdbool.h>

#define SIZE 10
#define EMPTY (-1)
#define FULL SIZE-1

bool isEmpty();
bool isFull();
bool push(int);
int pop();
int peek();
bool showMyStack();

int top = EMPTY,my_stack[SIZE];


bool main(){
  push(12);
  push(56);
  push(78);
  push(11);
  pop();
  showMyStack();
  return true;
}

bool isEmpty(){
  if(top==EMPTY)
    return true;
  return false;
}

bool isFull(){
  if(top==FULL)
    return true;
  return false;
}

bool push(int item){
  if(isFull())
    return false;
  my_stack[++top] = item;
  return true;
}

int pop(){
  if(isEmpty())
    return EMPTY;
  return my_stack[top--];
}

int peek(){
  if(isEmpty())
    return EMPTY;
  return my_stack[top];
}

bool showMyStack(){
  if(isEmpty())
    return false;
  for(int i = top;i>EMPTY;--i){
    printf("%d\n",my_stack[i]);
  }
  return true;
}
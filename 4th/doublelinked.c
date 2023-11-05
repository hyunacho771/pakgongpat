#include <stdio.h>
#include <stdlib.h>
#define _CRT_SECURE_NO_WARNINGS

//노드 structure 정의
struct Node {
	int data;
	struct Node* next;
	struct Node* prev;
};//더블 링크드 리스트이므로 처음과 끝 모두 정의
//리스트 정의
struct DoubleLinkedList {
	struct Node* head;
	struct Node* tail;
};
//초기화
void init(struct DoubleLinkedList* list) {
	list->head = NULL;
	list->tail = NULL;
}
//노드 생성 코드
struct Node* createNode(int data) {
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = data;
	newNode->prev = NULL;
	newNode->next = NULL;
}
//노드 추가 코드
void append(struct DoubleLinkedList* list, int data) {
	struct Node* newNode = createNode(data);
	if (list->tail == NULL) {//만약 노드가 처음 상태라면
		list->head = newNode;//처음과 끝 모두 자기자신으로 설정
		list->tail = newNode;
	}
	else {
		list->tail->next = newNode;
		newNode->prev = list->tail;
		list->tail = newNode;
	}
}
//리스트 출력 코드
void printlist(struct DoubleLinkedList* list) {
	struct Node* current = list->head;
	while (current != NULL) {
		printf("%d -> ", current->data);
		current = current->next;
	}
	printf("NULL\n");
}

int main() {
	struct DoubleLinkedList myList;
	init(&myList);
	int a, b, c;
	printf("첫번째 노드 값: ");
	scanf("%d", &a);
	printf("두번째 노드 값: ");
	scanf("%d", &b);
	printf("세번째 노드 값: ");
	scanf("%d", &c);
	append(&myList, a);
	append(&myList, b);
	append(&myList, c);
	printlist(&myList);
	return 0;
}
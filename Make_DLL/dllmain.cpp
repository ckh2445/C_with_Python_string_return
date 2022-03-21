// dllmain.cpp : DLL 애플리케이션의 진입점을 정의합니다.

#include "pch.h"
#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define EXPORT extern "C" __declspec(dllexport)

EXPORT int plus(int nA, int nB);

//BOOL APIENTRY DllMain(HANDLE hModule,
//	DWORD ul_reason_for_call,
//	LPVOID lpReserved)
//{
//	return TRUE;
//}

EXPORT int plus(int a, int b)
{
	return a + b;
}

EXPORT char* Login(char* id)
{
	char* my_id = (char*) malloc(sizeof(char) * (strlen(id)));

	strcpy_s(my_id, sizeof(char) * (strlen(id)),id);
	
	//char* my_pw = (char*) malloc(sizeof(char) * (strlen(pw)));
	//strcpy_s(my_pw, sizeof(char) * (strlen(id)), pw);
	
	/*char my_id[20];

	strcpy_s(my_id, 20, id);*/

	return my_id;
}

EXPORT char* strTest(char* str1) {
	char* new_str = (char*)malloc(sizeof(char) * (strlen(str1)));
	strcpy_s(new_str, sizeof(char) * (strlen(str1)),str1);

	return new_str;
}
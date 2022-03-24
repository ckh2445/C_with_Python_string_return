// dllmain.cpp : DLL 애플리케이션의 진입점을 정의합니다.

#include "pch.h"
#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define EXPORT extern "C" __declspec(dllexport)

EXPORT int plus(int nA, int nB);
EXPORT char* Login(char* id, char* pw);
EXPORT char* strTest(char* nStr1);

BOOL APIENTRY DllMain(HANDLE hModule,
	DWORD ul_reason_for_call,
	LPVOID lpReserved)
{
	return TRUE;
}

EXPORT int plus(int a, int b)
{
	return a + b;
}

EXPORT char* Login(char* id,char* pw)
{
	char* my_id = (char*) malloc(sizeof(char) * (strlen(id)));
	char* my_pw = (char*)malloc(sizeof(char) * (strlen(id)));

	strcpy(my_id,id);
	strcpy(my_pw, pw);

	return my_id;
}

EXPORT char* strTest(char* str1) {
	printf(str1);
	char* new_str = (char*)malloc(sizeof(char) * (strlen(str1)));
	printf("\n");
	
	strcpy(new_str,str1);
	printf(new_str);

	return new_str;
}


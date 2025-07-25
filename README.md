# 프로젝트 보고서


## 아이템 선정 동기
최근 Cursor, Entropic, OpenAI 등 여러 플랫폼이 MCP(Multi-agent Communication Protocol)를 표준으로 채택하며 AI 기술이 빠르게 진화하고 있습니다.  

이러한 변화 속에서 저를 포함한 많은 개발자와 학습자들이 어디서부터 시작해야 할지 막막함을 느끼는 것을 보고, MCP의 기본 개념과 활용법을 누구나 쉽게 이해할 수 있는 강의를 기획하고자 하였으며,
특히, 당장 저의 주변 학생들 중 해당 주제에 관한 관심을 보이는 친구들이 많았다는 점에서 강의 대상으로 채택하게 되었습니다.

강의 내용으로는 MCP의 구조와 작동 원리에 대한 전반적인 이해를 포함하여, 단순한 GitHub API 호출 실습을 넘어, AI 에이전트와 다양한 외부 서비스를 통합하고 자동화하는 경험을 제공하고자 했습니다.  

이를 통해, MCP가 단순히 '요즘 떠오르는 도구'가 아니라 당장 나의 문제 상황에 적용할 수 있는 **플랫폼 간 커넥터**라는 본질을 수강생들이 직접 체감하도록 돕는 것이 목표였습니다.

## 개발하면서 발생했던 문제점
강의 설계를 FastMCP 1.0 버전을 기준으로 시작했으나, 2.0으로 메이저 버전이 업그레이드되었습니다.

이로 인해 변경된 데코레이터 API와 CLI 사용법의 차이점을 분석하는 데 예상보다 많은 시간이 소요되었습니다.

특히 한 번은 아무리 디버깅을 해도 문제점을 발견하지 못하였었는데, 알고 보니 버전이 업데이트되며 함수의 인자명이 변경된 것임을 깨닫고 상당히 허탈했습니다. 

또, 모델이 `getWeather(city=서울)`처럼 한글 매개변수를 직접 넘기는 것인지, 일부 API 툴이 한글 인코딩을 지원하지 않아 JSON-RPC 에러가 발생하여, 원인을 파악하기 위해 여러 차례 로깅과 디버깅을 반복하면서 난항을 겪었습니다.

## 감상
본 프로젝트는 제게 단순히 MCP 프로토콜과 FastMCP 사용법을 전달하는 것을 넘어, **지식 인출 및 정리**와 **오류 상황 해결** 과정을 겪으며 스스로 성장하는 계기가 되었습니다.

또한, GitHub 실습을 간단하게 구성하면서도 MCP 자체를 깊이 있게 체감하도록 설계하였는데,
이것이 **입문자**에게는 Github를 통한 단순 '사용' 예제를,  **전공자**에게는 ‘자체 MCP 서버 구축’으로 확장 가능한 구조를 제시하며, 초심자와 중급자 모두를 위한 균형을 맞출 수 있으리라 생각하기에 뿌듯합니다.

## 기대 (수강자들에 대한)
MCP를 단순한 ‘툴 호출’ 기능이 아닌 **표준 프로토콜**로 제대로 이해하고,
“API를 어디서부터 어떻게 다루어야 할지”에 대한 막막함을 극복하는 계기가 되었으면 좋겠습니다.

강의의 말미에 언급하였듯, FastMCP와 같은 오픈소스 라이브러리를 직접 제어하며, ‘나만의 MCP 서버’를 구현해 보고, 
AI 모델과 에이전트를 보다 효율적으로 사용하는 **확장 가능한 워크플로우**를 설계·개발할 수 있기를 희망합니다.

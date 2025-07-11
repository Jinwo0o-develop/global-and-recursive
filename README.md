# global-and-recursive
> global 전역변수와 재귀함수 사용<br>
> 
' global ' <br>
저번에 했던 함수에 이어서 global 전역변수를 사용해보기로 했다.<br>
지역변수 오류때문에 알았던 방법인데, 생각보다 너무 쉽게 풀렸다.<br>
![한번에 성공](https://github.com/user-attachments/assets/14746913-e0ff-4d68-89e8-3f60d0900af0)<br>
정말 한번에 global을 선언하니, 문법오류가 뜨지도 않고, 코드는 정상작동했다.<br>
그렇다면, global과 클래스 중에 뭐가 더 좋을까 ?<br>
사실 이미 답을 알고 있다.<br>
현재 정보처리기사 자격증을 같이 병해하는 중인데, 객체지향 파트를 배우며, 캡슐성, 다형성, 상속성 등에 대해 배웠다.<br>
즉, global보다 재사용성이 좋은 클래스가 훨씬 좋다는 것.<br>
그럼에도 AI에게 물어보았다.<br>
> 정리
작고 단순한 스크립트에서는 global가 편할 수 있지만, 실무, 협업, 유지보수 관점에서는 클래스가 훨씬 더 적합하다는 것.<br>
global은 코드의 가독성도 저하되고, 만약 함수 하나가 값을 바꿨는데, 다른 함수도 그 변수에 의존하고 있으면 버그 발생 위험이 증가하며, 확장성 부족을 이야기 해주었다.<br>
내가 편한 것이 아닌, 다른 협업자가 나의 코드를 편하게 볼 수 있어야 한다는 것이 오늘의 내가 마음에 품어두어야 할 점이다.<br>
<br>
> 재귀함수(recursiv)
반복문을 사용하지 않고, 반복할 수 있는 방법으로 알게 된 재귀함수<br>
그렇기에 함수의 사용법부터 물어보았다.<br>

![GPT가 알려준 재귀함수 사용법(1)](https://github.com/user-attachments/assets/c44a1405-0dd4-434c-8f49-9aadca50cc38)<br>
그대로 사용해본다.<br>
![초반 재귀함수](https://github.com/user-attachments/assets/a3325c8e-12e4-4314-adcc-f1352bc95282)<br>
return에 사용할 값은 아직 모르겠고, sum_and_count 함수를 변수에 저장해서 값을 출력할 것이다.<br>
그렇다면 어디서 합계변수 sum을 더할 것이고 어디서 횟수 n을 올릴것인가 ?<br>
if문에서 현재횟수와 목표횟수가 같으면 return, 즉 함수의 종료이기 때문에, else 부분에 숫자 num을 input으로 받는다.<br>
또, sum 변수를 num안에 넣을 것인데, 이 sum은 정의되어 있지 않던 변수, 즉, 값이 할당되어 있던 변수가 아니다.<br>
큰 틀을 잡는것과 더불어 혹시나 될까? 하는 마음에 일단 넣어두었다.<br>
![중간과정](https://github.com/user-attachments/assets/007f07b0-b67b-42ef-b891-5f08b97b6d3c)<br>
n이 0이 되면 조건문을 종료하고, 그 값을 sum과 n에 반환하여 밖으로 값을 빼주려고 하였다.<br>
또, 함수의 결과값은 sum과 n에 저장하려 했는데, 여기서 코드의 오류를 발견한다.<br>
함수가 종료한 시점에서 n은 무조건 0, 즉, 분모가 0이 되어버리기 때문에 연산 자체가 불가능 하다는 것이다.<br>
3개의 숫자 평균을 구하는 것이 목표기 때문에, 목표횟수 n == 3으로 지정하고, 변수 sum은 역시 가능하지 않았다.<br>
함수바깥에 sum을 선언하고, 안에서 sum을 수정하므로, 지역변수 오류를 방지하기 위해 global을 선언한다.<br>
이번 문제도 해결했는데, 아직은 파이썬에 자신감이 없어서 중간에 sum과 n의 값을 출력해서 값을 확인하는 습관이 있다.<br>
근데, sum/n의 값 소수점이 너무 많아 보기 좋지 않고, 또, sum과 n의 값이 중간에 출력되는게 거슬렸다.<br>
![재귀함수 끝](https://github.com/user-attachments/assets/dc915adb-e32d-45ae-b520-7b80fcfbcbcd)<br>
오히려 가독성을 높이고, round라는 함수를 하나 배워서, 소수점 정리도 해주었다.<br>
훨씬 보기 깔끔하고 한번에 시각정보가 들어온다.<br>
![재귀함수 끝 결과](https://github.com/user-attachments/assets/8daa722e-adce-4373-b98c-f34adc9c54b2)<br>
근데, 함수부분을 조금만 건드리면 내가 원하는 만큼 숫자를 입력할 수 있을 것 같아 일반화까지 도전해보았다.<br>
![재귀함수 일반화](https://github.com/user-attachments/assets/56fa5a3b-6825-4c9e-beda-608f015725fe)<br>
![일반화한 재귀함수 결과](https://github.com/user-attachments/assets/16763c1b-c5a8-4082-9b52-40f2b932820b)<br>
물론, 입력갯수가 불분명하다는 조건하에 GPT는 어렵다고 했지만, 다른 방법으로 구현했다.<br>
이 문제를 풀 때 부터, 최종적으로 나의 목표는 sum_and_count 함수에 숫자를 넣으면 그 숫자 만큼 반복되게 만드는 것이였고, 지금의 코드이며 저번에 성공못한 일반화까지 성공한 것이 좋았다.<br>
<br>
근데, 이번 문제들은 스스로 꼬아서 찾았던 문제이기 때문에 근본적인 질문이 하나 든다.<br>
사실 클래스를 만들어서도 문제를 풀 수 있고, len함수와 for 등의 반복문을 사용해도 문제는 풀렸을 것이다.<br>
그렇다면 지금의 방법이 효율적인가? 라는 의문이 생긴다.
### 첫번째)
for 반복문 + len 함수를 이용하는 것이 가장 효율적이고, 속도도 빠르며, 메모리 적절, 가독성 우수, 사용 편리, 실무에서 많이 쓰임 등의 장점이 있다.<br>
### 두번째)
global은 확장성은 없지만 단순한 스크립트에선 편리하며, 클래스는 단순한 문제에서는 과한 감이 있지만, 확장성을 얻을 수 있음.<br>
### 세번째)
함수사용은 재사용도 가능하고 메모리도 적절하며 실무에서 자주 사용하기에 괜찮은 선택이였다.<br>
특히, 재귀는 반복문보다 효율성이 떨어지지만, 문제 자체가 재귀하는 경우는 괜찮다고 한다.<br>
<br>
## 내장함수
지금의 방법이 효율적이였는가? 라는 질문엔 그렇지 않다.<br>
당연히 내가 깊게 공부하고 싶었기 때문에 멀리 돌아온것이지만, 내장함수는 C언어로 구성되어있다고 한다.<br>
이 뜻은, 속도가 빠르고 검증되어 있다는 뜻이다.<br>
그 외에도, 호환성, 협업성, 메모리 최적화, 가독성 등 여러 장점이 있다.<br>
정리하자면 특별한 일이 없다면 내장함수를 사용하는 것이 무조건적으로 이득이라는 뜻 !<br>
다음에는 조건문을 갖고 연구해보겠습니다 ! <br>

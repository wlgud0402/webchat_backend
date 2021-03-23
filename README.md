# EyeLikeMeeting ( 온라인 미팅 서비스)
## Backend
https://eyelikemeeting.com/

한줄소개 : WebRTC 기반의 화면, 카메라, 마이크를 사용한 실시간 온라인 미팅 서비스입니다

Github Backend: [https://github.com/wlgud0402/webchat_backend](https://github.com/wlgud0402/webchat_backend)

Github Frontend: [https://github.com/wlgud0402/webchat_frontend](https://github.com/wlgud0402/webchat_frontend)

<회의실 생성 후 실시간으로 카메라, 마이크, 화면공유 및 채팅>


<메인페이지>
<img width="1792" alt="스크린샷 2021-03-21 오후 10 04 43" src="https://user-images.githubusercontent.com/61821825/112181386-c15f2b00-8c3f-11eb-87fe-28f20d68ec80.png">



<방 리스트>
<img width="1792" alt="스크린샷 2021-03-21 오후 10 11 28" src="https://user-images.githubusercontent.com/61821825/112180410-e30be280-8c3e-11eb-8bc1-925ce0fd3e90.png">

<방 안>
<img width="1792" alt="스크린샷 2021-03-23 오후 9 07 42" src="https://user-images.githubusercontent.com/61821825/112181482-d3d96480-8c3f-11eb-8204-07378f01d8d6.png">



### 주요 개발 부분

- Django 를 사용한 Backend 구현
- React 를 사용한 Frontend 구현
- WebRTC Client 및 WebRTC Server 구축으로 P2P 구현
- Redis pub/sub을 이용한 채팅 이벤트 관리 구현
- python scheduler를 이용한 방 상태, 모델 관리
- AWS를 이용한 인프라 구성
- Google React 와 JWT 기반 인증 구현

### **인스턴스 내부구조**

![Untitled Diagram](https://user-images.githubusercontent.com/61821825/112181270-9d034e80-8c3f-11eb-8f10-3f8cf9e15c17.png)


- NGINX를 사용한 리버스 프록싱
- /API 요청 ⇒ Django
- /static ⇒ React

### **서비스 시퀀스 다이어그램**

![김지형 포트폴리오](https://user-images.githubusercontent.com/61821825/112181332-b0aeb500-8c3f-11eb-9858-0235b9673f00.png)


- Google Oauth를 통한 JWT기반 인증구현
- 방 상세정보의 Push Server와 Media Server 정보로 각각 웹소켓 연결 후 입장 처리
- WebRTC 미디어 서버를 이용한 화면, 카메라, 오디오 스트리밍
- 채팅 액션 발생 시 Api server에서 Push(broker) 서버에 publish를 통한 이벤트 전달
<img width="1791" alt="스크린샷 2021-03-24 오전 1 15 00" src="https://user-images.githubusercontent.com/61821825/112181184-89f07e80-8c3f-11eb-8a39-30f1210da4f9.png">
- 방 나가기 이벤트 발생시 방 내부 인원수를 체크 ⇒ 인원이 없을시 스케쥴러를 통한 데이터 최적화
- 스케쥴러 처리 후 Push(broker) 서버에 publish를 통해 상태를 알림 ⇒ 모든 사용자에게 상태 전달
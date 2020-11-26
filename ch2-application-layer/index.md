# 2.1 Principles of Network Applications
## Checkout
### 5개의 Internet Applications와 그들이 사용하는 Application-Layer Protocol을 나열하라.
### 네트워크 아키텍쳐와 application 아키텍쳐의 차이점을 설명하라.
네트워크 아케텍쳐는 어플리케이션에 특정한 서비스를 제공하게끔 디자인되어있다. 어플리케이션 아키텍쳐는 각각의 end system에서 각각의 어플리케이션이 어떻게 구성되어 있는지에 초점이 맞춰진다. 따라서 이 둘은 구분되서 설계되어야한다. (물론 내가 만들려는 어플리케이션의 구조에 따라 선택해야되는 네트워크 아케텍쳐가 있어 둘은 분리되지만 상호 연관이 되어있다고 할 수 있다.)
### 두 프로세스간의 communication 시각에서 보았을 때, 어떤 프로세스가 서버이고 어떤 프로세스가 클라이언트인가
communication을 시작하는 프로세스가 클라이언트이고, 세션을 시작하기위해 연결되기를 기다리는 프로세스가 서버이다.
### P2P(Peer to Peer) application은 일반적인 client-server application과 다름에도 왜 서버, 클라이언트라는 용어가 사용되는가
P2P application은 각각의 peer가 모두 클라이언트가 될 수 있고 서버가 될 수 있다. 예를 들어, P2P File Sharing System에서 보면 하나의 Peer가 파일을 다운로드 받을 때는 클라이언트가 되는 것이고 파일을 업로딩할 떄는 서버가 된다. 이렇게 특정 맥락에서는 P2P application에서 클라이언트와 서버라는 개념은 여전히 유효하다.
### 프로세스간에 communication을 할 때(서로 다른 host에 존재하는 프로세스라 가정), 하나의 프로세스가 다른 host에 존재하는 프로세스를 구별해내기 위해 어떤 정보를 사용하는가?
Port 번호를 사용한다. 포트번호를 통해서 구별해낸다.
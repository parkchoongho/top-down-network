# 2.1 Principles of Network Applications
## Checkout
## 5개의 Internet Applications와 그들이 사용하는 Application-Layer Protocol을 나열하라.
Facebook, Twitter, Gmail, Instagram, Netflix</br>
HTTPS, HTTP, SMTP, FTP, TELNET
## 네트워크 아키텍쳐와 application 아키텍쳐의 차이점을 설명하라.
네트워크 아키텍쳐는 어플리케이션에 특정 서비스를 제공하게 끔 디자인 되어있다. 반면에, 어플리케이션 아키텍쳐는 각각의 end system에 존재하는 어플리케이션에 집중한다. 따라서 이 둘은 구분해서 설계해야 한다. (물론 만들려는 어플리케이션 구조에 따라 선택하는 네트워크 아키텍쳐가 있다. 따라서 둘은 분리되지만 상호 연관된다.)
## 두 프로세스간의 communication 시각에서 보았을 때, 어떤 프로세스가 서버이고 어떤 프로세스가 클라이언트인가
Communication을 시작하는 프로세스가 클라이언트이고, 세션을 시작하기위해 연결되기를 기다리는 프로세스가 서버이다.
## P2P(Peer to Peer) application은 일반적인 client-server application과 다름에도 왜 서버, 클라이언트라는 용어가 사용되는가
P2P application은 각각의 peer가 모두 클라이언트가 될 수 있고 서버가 될 수 있다. 예를 들어, P2P File Sharing System에서 보면 하나의 Peer가 파일을 다운로드 받을 때는 클라이언트가 되는 것이고 파일을 업로드할 때는 서버가 된다. 이렇게 특정 맥락에서는 P2P application도 클라이언트, 서버 개념이 여전히 유효하다.
## 프로세스간에 communication을 할 때(서로 다른 host에 존재하는 프로세스라 가정), 하나의 프로세스가 다른 host에 존재하는 프로세스를 구별해내기 위해 어떤 정보를 사용하는가?
Port 번호를 사용한다. 포트번호를 통해서 구별한다.
## HTTP가 가지는 network application에서의 역할은 무억인가? 그리고 web application을 완성시키기위해 필요한 다른 요소들에는 어떤 것들이 있나?
HTTP는 Application Layer Protocol로 기능한다. 서로 다른 host system에 위치한 프로세스간 정보를 주고 받는 방법에는 소켓이 있다. 소켓이 메세지를 어떻게 구성하고  메세지 조각들 의미를 어떻게 할 것인지에 대한 약속이 결국 HTTP이다. Web application을 완성하기 위한 다른 요소들로는 Transport Layer, Network Layer, Physical Layer가 있다. Transport Layer에서 사용하는 프로토콜에는 대표적으로 TCP, UDP가 있고 Network Layer에는 IP, Physical Layer에는 ARP등이 존재한다.
## Transport Layer에서 큰 범위의 4가지 서비스 개념에는 어떤 것들이 있는가?
### Reliable Data Transfer
전송된 패킷은 네트워크 상에서 유실될 위험을 안고  있다. 만약 카카오 뱅크에서 토스 계좌로 송금하는데 데이터가 유실되었다면?. 정말 끔찍한 일이 아닐 수 없다. 따라서 다른 host에서 보낸 데이터가 완전히 그리고 정확하게 보내려 했던 host에 전달됨을 보장해야 한다. 만약 프로토콜이 이러한 서비스를 제공한다면, **reliable data transfer**를 제공한다고 할 수 있다. 대표적으로 TCP가 이를 제공한다. 만약 Transfer Layer 프로토콜이 reliable data transfer를 제공하지 않는다면, 이 경우는 **loss-tolerant applications**에 많이 사용된다. 이러한 application들로는 오디오 비디오 같은 multimedia application등이 대표적이다.
### Throughput
프로세스간에 communication하는 과정에서 보낼 수 있는 비트의 비율을 **available throughput**이라 한다. 이러한 available throughput은 여러가지 session들이 같은 network path상 bandwidth를 공유하고 있기에 시시각각 변한다. 특정 application이 r bits/sec throughput을 보장받기를 원한다면 이를 transport layer에서 해결할 수 있다. 이렇게 throughput을 보장받기를 원하는 application들을 **bandwidth-sensitive applications**라 한다. 여러 multimedia application들이 비디오나 오디오를 압축하는 기술을 사용하여 현재 가능한 throughput내에 맞추려고 함에도 불구하고, 많은 multimedia application들이 bandwidth에 민감하다. Bandwidth에 sensitive한 application들과는 반대로 최대한 적은 throughput을 사용하려고 하는 **elastic application**도 존재한다.
### Timing
Transport Layer는 또한 timing을 보장하기도 한다. 예를 들어 전송자가 소켓을 통해 보낸 모든 비트들이 수신자 소켓에 100msc내에 전달되는 것 등이 이에 해당한다. 리얼타임 채팅이나 게임의 경우 이러한 timing을 보장하는 것이 중요하다. 이와는 반대로 non-real-time application의 경우에는 이러한 tight한 timing constraint가 상대적으로 덜하다.
### Security
Transport Layer에서는 security service까지 제공할 수 있다. 예를 들어 transport layer protocol이 데이터를 전송하는 프로세스에서 보내는 data를 모두 암호화하고 데이터를 받는 프로세스가 데이터를 받기전에 해당 데이터를 복호화할 수 있다.

## SSL은 Transport Layer, Application Layer 둘 중 어디서 작동하는가? 만약 개발자가 TCP를 SSL까지 확장하고 싶다면 어떤 조치를 취해야 하나
![ssl 과정](https://user-images.githubusercontent.com/34790763/101268034-6f82ba00-37a2-11eb-87ef-e365e34380b1.jpg)
password와 같은 민감한 정보들을 암호화없이 그냥 보내게 된다면 스니핑과 같은 해킹에 무방비로 노출된다. 이러한 상황을 방지하고자 **SSL(Secure Sockets Layer)**라는 TCP 확장자가 개발되었다. **TCP-enhanced-SSL**은 원래 TCP 역할 뿐만 아니라 프로세스간 커뮤니케이션에서 필요한 여러 security service들을 제공한다(encryption, data integrity, end-point authentication). SSL은 Transport Layer Protocol가 아닌 TCP의 확장이다. (중요한건 SSL은 Transport Layer Protocol이 아니라는 사실 + Application Layer와 Transport Layer 사이를 잇는다.) SSL을 사용하고 싶으면 클라이언트와 서버 모두 SSL code를 포함해야한다. SSL은 TCP socket API와 유사한 자신만의 socket API를 가지고 있다. Application이 SSL을 사용하면, 전송 프로세스는 데이터를 SSL socket에 전송한다. SSL이 이 받은 데이터를 암호화하고 이를 TCP socket에 보낸다. 이 암호화된 데이터는 송신 프로세스의 TCP 프로세스에 가게되고 이를 다시 송신 프로세스의 SSL socket으로 보낸다. 여기서 복호화를 진행하고 이를 다시 송신 process로 보낸다.

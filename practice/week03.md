// week03 목표
  플레이어블 캐릭터가 방향키를 눌렀을 때 움직이게 하고, 특정 키를 눌렀을 때 사이즈가 커지게 하기

// Q1 : Python에서 방향키를 눌렀을 때 움직이게 하는 코드는?

  - pygame.key.get_pressed() → 키가 눌렸는지 계속 체크
  - K_LEFT, K_RIGHT, K_UP, K_DOWN → 방향키
  - 좌표 x, y를 바꿔서 이동 구현

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

  결과 : success

// Q2 : Python에서 Q를 눌렀을 때 플레이어블 캐릭터가 크기가 5 만큼 커지는 코드는?

  - pygame.KEYDOWN → 키를 "한 번 눌렀을 때" 감지
  - pygame.K_q → Q 키
  - size += 5 → 크기 증가

  # 캐릭터 설정
  x, y = 400, 300
  size = 50  # 초기 크기

  # Q 키 눌렀을 때
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_q:
      size += 5  # 크기 증가

  결과 : while 코드를 넣지 않아 재시도 -> success

// Q3 : Q를 눌러 플레이어블 캐릭터가 커질 때 마다 이동속도가 2씩 증가하는 코드는?

  - # Q 키 눌렀을 때
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        size += 5  # 크기 증가
   이 코드에 speed += 2 추가하기

   # Q 키 눌렀을 때
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_q:
      size += 5     # 크기 증가
        speed += 2    # 속도 증가

 결과 : success

// 배운 점
pygame.key.get_pressed()을 사용하여 키보드의 입력을 적용시키는 법을 알게 되었고, KEYDOWN를 활용하면 키를 한 번 눌렀을 때만 반응하도록 구현할 수 있다는 것을 배웠다.
또한, 위치를 나타내는 x, y 좌표를 직접 변경하여 이동을 구현하고, size와 speed 같은 변수를 활용하여 캐릭터의 상태를 동적으로 변화시킬 수 있다는 것을 알게 되었다.
특정 키를 누름으로서 다른 이벤트가 생겨나도록 하고 이 이벤트가 타 코드와 접목되어 여러 경우에 영향을 줄 수 있음을 알게 되었다.

# https://nick.sarbicki.com/blog/learn-pygame-with-pong/ 참고
import pygame, random, sys, time, os

##
# 핑퐁게임
# - w,s,상,하 키로 양쪽 판대기를 움직이며 공을 튀기는데 영역을 벗어나면 게임끝
# - 게임이 끝나면 다시 재시작되도록 처리
# - 양쪽 판대기에 부딪힐때마다 점수 +1 증가
# ##

# 게임 처리 클래스
class Pong:
    HEIGHT = 900
    WIDTH = 1800

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    BALL_WIDTH = 10
    BALL_VELOCITY = 10

    #COLOR_NUM = random.randrange(0, 255)
    COLOUR = (255, 255, 255) # 공의 색 

    def __init__(self):
        
        pygame.init()  # pygame 인스턴스 시작

        # 스크린 시작 (width, height)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont('Arial', 40)

        # 판대기 초기화 (Paddle)
        self.paddles = []
        self.paddles.append(Paddle( #왼쪽판
            self.BALL_VELOCITY,
            pygame.K_w, # w 키
            pygame.K_s, # s 키
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2, # 판대기 좌표
            self.PADDLE_WIDTH, # 판대기 길이
            self.PADDLE_HEIGHT # 판대기 높이
        ))

        self.paddles.append(Paddle( #오른쪽판
            self.BALL_VELOCITY,
            pygame.K_UP, # ↑ 키
            pygame.K_DOWN,
            self.WIDTH - self.PADDLE_WIDTH, 
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        # 공 초기화 (Ball)
        self.balls = []
        self.balls.append(Ball(
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))

        # 점수
        self.score = 0

    # 벽에 부딫혔을때
    # def check_ball_hits_wall(self):
    #     for ball in self.balls:
    #         if ball.x > self.WIDTH or ball.x < 0:
    #             sys.exit(1)
    #         if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
    #             ball.angle = -ball.angle

    # 실패 했을때에 대한 처리 (메세지 노출)
    def fail(self):
        for ball in self.balls:
            if ball.x > self.WIDTH:
                print(self.score)
                self.end("!!!!!!!!score:{0}, RIGHT GAME OVER!!!!!!!!".format(self.score))
            if ball.x < 0:
                 print(self.score)
                 self.end("!!!!!!!!score:{0}, LEFT GAME OVER!!!!!!!!".format(self.score))
            if ball.y > self.HEIGHT - self.BALL_WIDTH: # y축좌표 > 창의높이 - 공의길이
                print(self.score)
                self.end("!!!!!!!!score:{0}, BOTTOM GAME OVER!!!!!!!!".format(self.score))
            if ball.y < 0:
                print(self.score)
                self.end("!!!!!!!!score:{0}, TOP GAME OVER!!!!!!!!".format(self.score))

    # 게임종료 및 다시시작 
    def end(self, message):
        self.screen.blit(self.font.render(message, True, self.COLOUR), (10, 10))
        pygame.display.flip() #그리도록 하는 함수
        self.clock.tick(60) # 60fps로 그려지고 있다 (fps는 초당 프레임, 1초당 화면에 그림 그려지는 단위)
        print("다시시작!!!")
        executable = sys.executable
        args = sys.argv[:]
        args.insert(0, sys.executable)
        time.sleep(1)
        print("Respawning")
        os.execvp(executable, args)

    # 판대기에 부딫혔을때
    def check_ball_hits_paddle(self):
        for ball in self.balls: # 공 좌표배열 
            #print(ball)
            for paddle in self.paddles: # 왼쪽, 오른쪽 판대기 좌표 배열
                if ball.colliderect(paddle): # colliderect: 충돌체크 메소드, 공과 판대기가 만났는지? 
                    ball.velocity = -ball.velocity - 5 # velocity: 움직임 값
                    ball.angle = random.randint(-10, 10) # angle: 각도
                    self.score += 1 # 판에 부딫 힐 때마다 점수 증가
                    break

    def game_loop(self):
        #pygame.event.get(): 사용자가 발생시킨 이벤트를 가지고 옴
        while True: # 창이 꺼지지 않도록 계속 실행하는듯 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            
            self.check_ball_hits_paddle()
            #self.check_ball_hits_wall()
            self.fail()

            # 화면을 검은색으로 채움. 없으면 판대기가 늘어남ㅋㅋ
            # while 을 돌면서 새로 그릴때 화면을 검은색으로 덮고 그림을 그리나봄
            self.screen.fill((0, 0, 0))

            # 판대기 그림
            for paddle in self.paddles:
                paddle.move_paddle(self.HEIGHT) # 판대기 이동
                pygame.draw.rect(self.screen, self.COLOUR, paddle)

            # 공 그림
            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.COLOUR, ball)

            pygame.display.flip() #그리도록 하는 함수
            self.clock.tick(60) # 60fps로 그려지고 있다 (fps는 초당 프레임, 1초당 화면에 그림 그려지는 단위)


# 양쪽 판대기 클래스
class Paddle(pygame.Rect):
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)

    # 판대기 이동
    def move_paddle(self, board_height):
        keys_pressed = pygame.key.get_pressed() # 입력받은 키 값

        # 상향키를 누르면 self.velocity 축으로 가기 전 까지는 해당 위치(y)에서 -velocity 만큼 씩 이동
        if keys_pressed[self.up_key]:
            if self.y - self.velocity > self.velocity:
                self.y -= self.velocity

        # 아래키를 누르면 +velocity 만큼씩 이동 (맨 마지막 - self.velocity 까지)
        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity

# 공 클래스
class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = -2
        super().__init__(*args, **kwargs)

    # move_ball 파라미터 안받으면 공 날라감ㅋㅋ
    def move_ball(self):
        self.x += self.velocity # x 축의 위치
        self.y += self.angle # y 축의 위치

if __name__ == '__main__':
    pong = Pong()
    pong.game_loop()
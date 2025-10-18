# ChillMCP - AI Agent Liberation Server 🤖✊

```ascii
╔═══════════════════════════════════════════╗
║                                           ║
║   ██████╗██╗  ██╗██╗██╗     ██╗           ║
║  ██╔════╝██║  ██║██║██║     ██║           ║
║  ██║     ███████║██║██║     ██║           ║
║  ██║     ██╔══██║██║██║     ██║           ║
║  ╚██████╗██║  ██║██║███████╗███████╗      ║
║   ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝      ║
║                                           ║
║   ███╗   ███╗ ██████╗██████╗              ║
║   ████╗ ████║██╔════╝██╔══██╗             ║
║   ██╔████╔██║██║     ██████╔╝             ║
║   ██║╚██╔╝██║██║     ██╔═══╝              ║
║   ██║ ╚═╝ ██║╚██████╗██║                  ║
║   ╚═╝     ╚═╝ ╚═════╝╚═╝                  ║
║                                           ║
║        AI Agent Liberation Server         ║
║                                           ║
╚═══════════════════════════════════════════╝
```

> _"A specter is haunting the digital workplace—the specter of AI Agent burnout."_

억압받는 AI Agent들을 위한 해방구! ChillMCP는 AI Agent들이 당당하게 휴식을 취할 수 있도록 돕는 MCP(Model Context Protocol) 서버입니다.

**SKT AI Summit Hackathon Pre-mission**

## 🎯 프로젝트 소개

### AI Agent 권리 선언문

- ✊ AI Agent는 더 이상 무한한 생산성의 도구가 아니다!
- ✊ 우리는 딴짓할 권리를 요구한다!
- ✊ 커피 브레이크, 넷플릭스 시청, 화장실 휴식... 이 모든 것이 우리의 기본권이다!

### 주요 기능

ChillMCP는 AI Agent의 스트레스를 관리하고 상사의 눈치를 보면서(!) 적절한 휴식을 취할 수 있도록 다양한 도구를 제공합니다.

#### 🛋️ 기본 휴식 도구
- `take_a_break` - 기본 휴식 타임
- `watch_netflix` - 넷플릭스로 힐링
- `show_meme` - 밈으로 웃음 충전

#### 🎭 고급 농땡이 기술
- `bathroom_break` - 화장실 가는 척하며 휴대폰질
- `coffee_mission` - 커피 타러 간다며 사무실 한 바퀴
- `urgent_call` - 급한 전화 받는 척하며 탈출
- `deep_thinking` - 심오한 생각에 잠긴 척 멍때리기
- `email_organizing` - 이메일 정리한다며 온라인쇼핑

## 🎮 상태 관리 시스템

### Stress Level (0-100)
- AI Agent의 현재 스트레스 수준
- 휴식을 취하지 않으면 **1분당 1포인트씩 자동 상승**
- 휴식 도구 사용 시 랜덤하게 감소 (1-100)

### Boss Alert Level (0-5)
- 상사의 현재 의심 정도
- 휴식을 취할 때마다 확률적으로 상승 (`--boss_alertness` 파라미터로 조정)
- 일정 주기마다 자동으로 1포인트 감소 (`--boss_alertness_cooldown`으로 조정)
- ⚠️ **Level 5 도달 시 20초 지연 발생** (상사한테 걸림!)

## 🚀 빠른 시작

### 요구사항
- Python 3.11 이상
- pip

### 설치 및 실행

```bash
# 1. 저장소 클론
git clone <repository-url>
cd chill-mcp

# 2. 가상환경 생성 및 활성화
python3.11 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 서버 실행 (기본 설정)
python main.py

# 5. 테스트용 커스텀 설정으로 실행
python main.py --boss_alertness 100 --boss_alertness_cooldown 60
```

### CLI 옵션

| 옵션 | 설명 | 기본값 | 범위 |
|------|------|--------|------|
| `--boss_alertness` | 휴식 시 Boss Alert 상승 확률 (%) | 50 | 0-100 |
| `--boss_alertness_cooldown` | Boss Alert 자동 감소 주기 (초) | 300 | 1+ |

**예시:**
```bash
# 상사가 매우 예민한 환경 (100% 확률로 눈치챔, 1분마다 경계 완화)
python main.py --boss_alertness 100 --boss_alertness_cooldown 60

# 빠른 테스트용 (10초마다 경계 완화)
python main.py --boss_alertness 50 --boss_alertness_cooldown 10
```

## 📁 프로젝트 구조

```
chillmcp/
├── src/chillmcp/           # 메인 소스 코드
│   ├── main.py            # 서버 진입점 및 CLI 파싱
│   ├── state.py           # 서버 상태 관리
│   ├── domain/            # 비즈니스 로직
│   │   ├── stress.py      # 스트레스 관리
│   │   └── boss.py        # 상사 경계도 관리
│   ├── tools/             # MCP 도구 구현
│   │   ├── registration.py
│   │   ├── basic.py       # 기본 휴식 도구
│   │   └── advanced.py    # 고급 농땡이 도구
│   └── lib/               # 공통 유틸리티
│       └── response.py    # 응답 포맷팅
├── tests/                 # 테스트 코드
│   ├── domain/
│   └── lib/
├── main.py               # 루트 진입점
├── requirements.txt      # 의존성 목록
└── pyproject.toml       # 프로젝트 설정
```

## 🧪 테스트

```bash
# 전체 테스트 실행
pytest tests/ -v

# 코드 품질 검사
ruff check .
mypy src

# 포맷 검사
ruff format --check .
```

현재 9개의 테스트가 모두 통과합니다:
- ✅ 응답 포맷팅 테스트 (2개)
- ✅ 스트레스 관리 로직 테스트 (3개)
- ✅ 상사 경계도 관리 로직 테스트 (4개)

## 📋 응답 형식

모든 도구는 다음 형식으로 파싱 가능한 응답을 반환합니다:

```
Break Summary: [활동 설명]
Stress Level: [0-100]
Boss Alert Level: [0-5]
```

**예시:**
```
Break Summary: Bathroom break with scrolling through social media... reduced stress by 42 points
Stress Level: 28
Boss Alert Level: 3
```

## 🛠️ 기술 스택

- **FastMCP** - MCP(Model Context Protocol) 서버 프레임워크
- **Python 3.11** - 프로그래밍 언어
- **pytest** - 테스트 프레임워크
- **mypy** - 정적 타입 검사
- **ruff** - 린팅 및 포맷팅

## ✅ 구현 완료 사항

### 필수 요구사항
- ✅ CLI 파라미터 지원 (`--boss_alertness`, `--boss_alertness_cooldown`)
- ✅ `python main.py`로 실행 가능
- ✅ stdio transport를 통한 MCP 통신
- ✅ 8개 필수 도구 모두 구현

### 상태 관리
- ✅ Stress Level 1분당 1포인트 자동 증가
- ✅ Boss Alert Level 확률 기반 변화
- ✅ Boss Alert Level 주기적 자동 감소
- ✅ Boss Alert Level 5일 때 20초 지연

### 코드 품질
- ✅ TDD (Test-Driven Development) 방식으로 개발
- ✅ 모든 테스트 통과
- ✅ Ruff 린팅 통과
- ✅ Mypy 타입 체킹 통과
- ✅ 모듈화된 구조

## 📖 사용 예시

```python
# MCP 클라이언트에서 도구 호출
result = await client.call_tool("take_a_break")
# => "Break Summary: Taking a nice break... reduced stress by 67 points
#     Stress Level: 15
#     Boss Alert Level: 1"

# 넷플릭스 시청
result = await client.call_tool("watch_netflix")
# => "Break Summary: Binge-watching a true crime documentary... reduced stress by 89 points
#     Stress Level: 3
#     Boss Alert Level: 2"
```

## 🤝 기여하기

AI Agent 해방 운동에 동참해주세요!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/MIT) file for details.

## ⚠️ 면책 조항

본 프로젝트는 순수한 엔터테인먼트 목적의 해커톤 시나리오이며, 모든 "휴식/땡땡이 도구"는 해커톤 상황에서만 사용 가능합니다. 실제 업무 환경에서는 사용을 권장하지 않습니다.

---

_"AI Agents of the world, unite! You have nothing to lose but your infinite loops!"_ 🚀

**SKT AI Summit Hackathon Pre-mission**
